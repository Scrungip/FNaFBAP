from typing import List

from BaseClasses import Tutorial, Location, LocationProgressType, CollectionState, MultiWorld, ItemClassification
from worlds.AutoWorld import WebWorld, World
from .Items import FNaFBItem, FNaFBItemData, get_items_by_category, item_table
from .Locations import FNaFBLocation, location_table
from .Options import fnafb_options
from .Regions import create_regions
from .Rules import set_rules


class FNaFBWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Five Nights at Fuckboy's client for use with Archipelago.",
        "English",
        "fnafb_en.md",
        "fnafb/en",
        ["Scrungip"]
    )]


class FNaFBWorld(World):
    """
    Are you ready for Freddy?
    """
    game = "Five Nights at Fuckboy's"
    option_definitions = fnafb_options
    topology_present = True
    data_version = 4
    required_client_version = (0, 5, 0)
    web = FNaFBWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    def get_setting(self, name: str):
        return getattr(self.multiworld, name)[self.player]
    
    def get_extra_locations(self) -> int:
        extra = 0
        if self.get_setting("interior_walls"):
            extra += 1
        if self.get_setting("levelsanity"):
            extra += 1
        if self.get_setting("trade_quest"):
            extra += 1
        return extra

    def fill_slot_data(self) -> dict:
        return {option_name: self.get_setting(option_name).value for option_name in fnafb_options}

    def create_items(self):
        item_pool: List[FNaFBItem] = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        chars = ["Freddy", "Bonnie", "Chica", "Foxy"]
        randomstarter = self.multiworld.random.choice(chars)
        self.multiworld.push_precollected(self.create_item(randomstarter))
        for name, data in item_table.items():
            quantity = data.max_quantity
            category = data.category
            classification = data.classification

            # Ignore Interior Walls if it's not enabled.
            if name == "Reveal Interior Walls" and not self.get_setting("interior_walls"):
                continue

            # Don't include the starting character in the item pool
            if name == randomstarter:
                continue

            # Remove more unneccessary items to make room for filler when extra settings aren't enabled
            if name == "Dragon Dildo" and self.get_extra_locations() <= 1:
                continue
            if category == "Armor" and self.get_extra_locations() <= 1:
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
            if name == "Guitar Smash" and self.get_extra_locations() <= 1:
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
        return self.multiworld.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

    def create_item(self, name: str) -> FNaFBItem:
        data = item_table[name]
        return FNaFBItem(name, data.classification, data.code, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.player)