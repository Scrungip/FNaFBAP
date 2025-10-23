from typing import List

from BaseClasses import Tutorial, Location, LocationProgressType, CollectionState, MultiWorld, ItemClassification
from worlds.AutoWorld import WebWorld, World
from .Items import FNaFB1Item, FNaFB1ItemData, get_items_by_category, item_table
from .Locations import FNaFB1Location, location_table
from .Options import FNaFB1Options
from .Regions import create_regions
from .Rules import set_rules


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

    item_name_to_id = {name: data.code for name, data in item_table.items()}
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

    def fill_slot_data(self) -> dict:
        return self.options.as_dict(*[name for name in self.options_dataclass.type_hints.keys()])

    def create_items(self):
        item_pool: List[FNaFB1Item] = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        chars = ["Freddy", "Bonnie", "Chica", "Foxy"]
        randomstarter = self.multiworld.random.choice(chars)
        if self.options.random_starter:
            self.multiworld.push_precollected(self.create_item(randomstarter))
        else:
            self.multiworld.push_precollected(self.create_item("Freddy"))
        if self.options.goal == "puppetmaster_bb":
            self.multiworld.push_precollected(self.create_item("Puppet's Strings"))
        for name, data in item_table.items():
            quantity = data.max_quantity
            category = data.category
            classification = data.classification

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
            if name == randomstarter and self.options.random_starter:
                continue
            if name == "Freddy" and not self.options.random_starter:
                continue

            # Remove more unneccessary items to make room for filler when extra settings aren't enabled
            if name == "Dragon Dildo" and self.get_extra_locations() <= 1:
                continue
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

            item_pool += [self.create_item(name) for _ in range(0, quantity)]
        while len(item_pool) < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        fillers = get_items_by_category("Filler")
        weights = [data.weight for data in fillers.values()]
        return self.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

    def create_item(self, name: str) -> FNaFB1Item:
        data = item_table[name]
        return FNaFB1Item(name, data.classification, data.code, self.player)

    def create_regions(self):
        create_regions(self)

    def set_rules(self):
        set_rules(self, self.player)