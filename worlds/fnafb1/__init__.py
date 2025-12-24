from typing import List

from BaseClasses import Tutorial, Location, LocationProgressType, CollectionState, MultiWorld, ItemClassification
from Options import OptionError
from worlds.AutoWorld import WebWorld, World
from .Items import FNaFB1Item, FNaFB1ItemData, get_items_by_category, item_table, other_game_item_table, full_table
from .Locations import FNaFB1Location, location_table
from .Options import FNaFB1Options
from .Regions import create_regions
from .Rules import set_rules
from .OtherWorldNames import MarioNames, Zelda3DNames, SonicNames, JunkoNames, MetroidNames, KirbyNames, LttPNames, MegaManNames, LADXNames, KingdomHeartsNames, PokemonNames


class FNaFB1Web(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Five Nights at Fuckboy's client for use with Archipelago.",
        "English",
        "fnafb_en.md",
        "fnafb/en",
        ["Scrungip"]
    )]


class FNaFB1World(World):
    """
    Are you ready for Freddy?
    """
    game = "Five Nights at Fuckboy's"
    options_dataclass = FNaFB1Options
    options: FNaFB1Options
    topology_present = True
    data_version = 4
    required_client_version = (0, 6, 3)
    web = FNaFB1Web()

    item_name_to_id = {name: data.code for name, data in full_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    def get_setting(self, name: str):
        return getattr(self.multiworld, name)[self.player]
    
    def get_extra_locations(self) -> int:
        extra = 0
        if self.options.interior_walls:
            extra += 1
        if self.options.levelsanity:
            extra += 1
        if self.options.trade_quest:
            extra += 1
        return extra
    
    def generate_early(self) -> None:
        if self.options.developer_intrusion and not self.options.interior_walls:
            raise OptionError(f"{self.player_name} has Developer Intrusion enabled without having enabled the Interior Walls as well. This is not supported behavior. Please change your YAML settings.")

    def fill_slot_data(self) -> dict:
        return self.options.as_dict(*[name for name in self.options_dataclass.type_hints.keys()])

    def create_items(self):
        item_pool: List[FNaFB1Item] = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))

        # Starting Character stuff
        starter = " "
        if self.options.starter == "freddy":
            self.multiworld.push_precollected(self.create_item("Freddy", ItemClassification.progression))
            starter = "Freddy"
        if self.options.starter == "bonnie":
            self.multiworld.push_precollected(self.create_item("Bonnie", ItemClassification.progression))
            starter = "Bonnie"
        if self.options.starter == "chica":
            self.multiworld.push_precollected(self.create_item("Chica", ItemClassification.progression))
            starter = "Chica"
        if self.options.starter == "foxy":
            self.multiworld.push_precollected(self.create_item("Foxy", ItemClassification.progression))
            starter = "Foxy"

        # Goal stuff
        if self.options.goal == "puppetmaster_bb":
            self.multiworld.push_precollected(self.create_item("Puppet's Strings", ItemClassification.progression))

        # Tracking for Items from other worlds (so they don't end up in the pool multiple times)
        mario = 0
        zelda = 0
        sonic = 0
        junko = 0
        cavestory = 0
        clique = 0
        metroid = 0
        kirby = 0
        hollow = 0
        lttp = 0
        megaman = 0
        ladx = 0
        toontown = 0
        hatintime = 0
        kingdom = 0
        pokemon = 0
        fuckboys = 0
        jigsaw = 0
        p = 0
        smz = 0
        scoob = 0
        undertaletwo = 0
        sm64romhack = 0
        pvzfusion = 0

        for name, data in item_table.items():
            quantity = data.max_quantity
            category = data.category
            classification = data.classification

            # We only want one progression Dragon Dildo
            if name == "Progressive Dragon Dildo":
                item_pool.append(self.create_item(name, classification))
                item_pool.append(self.create_item(name, ItemClassification.useful))
                continue

            # Ignore Interior Walls if it's not enabled.
            if name == "Reveal Interior Walls" and not self.options.interior_walls:
                continue

            # You don't have to let me in if you don't want to.
            if name == "Funky Scrungip Token" and not self.options.developer_intrusion:
                continue

            # We're using this item in place of slot data, we don't actually need it in the pool.
            if name == "Puppet's Strings":
                continue

            # Don't include the starting character in the item pool
            if name == starter:
                continue

            # Remove more unneccessary items to make room for filler when extra settings aren't enabled
            if category == "ExtraArmor" and self.get_extra_locations() <= 1:
                continue
            if name == "Fazbear Combo" and self.get_extra_locations() <= 1:
                continue
            if name == "Flighty Combo" and self.get_extra_locations() <= 1:
                continue
            if name == "Bonbon Combo" and self.get_extra_locations() <= 1:
                continue
            if name == "Pirate Combo" and self.get_extra_locations() <= 1:
                continue
            if name == "Caffeine Revival" and self.get_extra_locations() <= 1:
                continue
            if name == "Guitar Riff" and self.get_extra_locations() <= 1:
                continue
            if name == "Speed Share" and self.get_extra_locations() <= 1:
                continue

            # Ignore filler, it will be added in a later stage.
            if data.category == "Filler":
                continue

            item_pool += [self.create_item(name, classification) for _ in range(0, quantity)]

        # Add items depending on other games in the multiworld, make sure they only get added once
        # Game names are pulled from OtherWorldNames.py if they are part of a group
        for game_name in self.multiworld.game.values():
            if len(item_pool) < total_locations:
                for MarioMulti in MarioNames:
                    if MarioMulti == game_name:
                        if mario < 1:
                            mario += 1
                            item_pool.append(self.create_other_game_item("1-Up Mushroom"))
                for Zelda3DMulti in Zelda3DNames:
                    if Zelda3DMulti == game_name:
                        if zelda < 1:
                            zelda += 1
                            item_pool.append(self.create_other_game_item("Hylian Shield"))
                for SonicMulti in SonicNames:
                    if SonicMulti == game_name:
                        if sonic < 1:
                            sonic += 1
                            item_pool.append(self.create_other_game_item("Chaos Emerald"))
                for JunkoMulti in JunkoNames:
                    if JunkoMulti == game_name:
                        if junko < 1:
                            junko += 1
                            item_pool.append(self.create_other_game_item("Dreamer's Crown"))
                if game_name == "Cave Story":
                    if cavestory < 1:
                        cavestory += 1
                        item_pool.append(self.create_other_game_item("Blade"))
                if game_name == "Clique":
                    if clique < 1:
                        clique += 1
                        item_pool.append(self.create_other_game_item("The Big Red Button"))
                for MetroidMulti in MetroidNames:
                    if MetroidMulti == game_name:
                        if metroid < 1:
                            metroid += 1
                            item_pool.append(self.create_other_game_item("Varia Suit"))
                for KirbyMulti in KirbyNames:
                    if KirbyMulti == game_name:
                        if kirby < 1:
                            kirby += 1
                            item_pool.append(self.create_other_game_item("Warp Star"))
                if game_name == "Hollow Knight":
                    if hollow < 1:
                        hollow += 1
                        item_pool.append(self.create_other_game_item("Dream Nail"))
                for LttPMulti in LttPNames:
                    if LttPMulti == game_name:
                        if lttp < 1:
                            lttp += 1
                            item_pool.append(self.create_other_game_item("Moon Pearl"))
                for MegaManMulti in MegaManNames:
                    if MegaManMulti == game_name:
                        if megaman < 1:
                            megaman += 1
                            item_pool.append(self.create_other_game_item("Mega Buster"))
                for LADXMulti in LADXNames:
                    if LADXMulti == game_name:
                        if ladx < 1:
                            ladx += 1
                            item_pool.append(self.create_other_game_item("Roc's Feather"))
                if game_name == "Toontown":
                    if toontown < 1:
                        toontown += 1
                        item_pool.append(self.create_other_game_item("Lawbot Disguise"))
                if game_name == "A Hat in Time":
                    if hatintime < 1:
                        hatintime += 1
                        item_pool.append(self.create_other_game_item("Hookshot Badge"))
                for KingdomHeartsMulti in KingdomHeartsNames:
                    if KingdomHeartsMulti == game_name:
                        if kingdom < 1:
                            kingdom += 1
                            item_pool.append(self.create_other_game_item("Reflect Element"))
                for PokemonMulti in PokemonNames:
                    if PokemonMulti == game_name:
                        if pokemon < 1:
                            pokemon += 1
                            item_pool.append(self.create_other_game_item("HM04 Strength"))
                if game_name == "Five Nights at Fuckboy's 2":
                    if fuckboys < 1:
                        fuckboys += 1
                        item_pool.append(self.create_other_game_item("Toy Freddy"))
                if game_name == "Jigsaw":
                    if jigsaw < 1:
                        jigsaw += 1
                        item_pool.append(self.create_other_game_item("1 Puzzle Piece"))
                if game_name == "Lies of P":
                    if p < 1:
                        p += 1
                        item_pool.append(self.create_other_game_item("P"))
                if game_name == "SMZ3":
                    if smz < 1:
                        smz += 1
                        item_pool.append(self.create_other_game_item("Star Fox Credits Theme"))
                if game_name == "Scooby-Doo! Night of 100 Frights":
                    if scoob < 1:
                        scoob += 1
                        item_pool.append(self.create_other_game_item("Scooby Snack"))
                if game_name == "Undertale 2":
                    if undertaletwo < 1:
                        undertaletwo += 1
                        item_pool.append(self.create_other_game_item("Anime catboy transformation potion"))
                if game_name == "SM64 Romhack":
                    if sm64romhack < 1:
                        sm64romhack += 1
                        item_pool.append(self.create_other_game_item("Lava Badge"))
                if game_name == "Plants Vs Zombies Fusion":
                    if pvzfusion < 1:
                        pvzfusion += 1
                        item_pool.append(self.create_other_game_item("The Fog is Coming"))


        while len(item_pool) < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        fillers = get_items_by_category("Filler")
        weights = [data.weight for data in fillers.values()]
        return self.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

    def create_item(self, name: str, classification: ItemClassification = ItemClassification.filler) -> FNaFB1Item:
        data = item_table[name]
        return FNaFB1Item(name, classification, data.code, self.player)
    
    def create_other_game_item(self, name: str) -> FNaFB1Item:
        data = other_game_item_table[name]
        return FNaFB1Item(name, data.classification, data.code, self.player)

    def create_regions(self):
        create_regions(self)

    def set_rules(self):
        set_rules(self, self.player)