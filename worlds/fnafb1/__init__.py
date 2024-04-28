from typing import List

from BaseClasses import Tutorial, Location, LocationProgressType, CollectionState, MultiWorld
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
        "A guide to setting up the Five Nights at F***boy's client for use with Archipelago.",
        "English",
        "fnafb_en.md",
        "fnafb/en",
        ["Scrungip"]
    )]


class FNaFBWorld(World):
    """
    Five Nights at F***boy's is an RPG game that contains a lot of crude humor from the mid 2010's, join Freddy F***boy as he begins his night of debauchery.
    """
    game = "Five Nights at Fuckboy's"
    option_definitions = fnafb_options
    topology_present = True
    data_version = 4
    required_client_version = (0, 4, 5)
    web = FNaFBWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    def get_setting(self, name: str):
        return getattr(self.multiworld, name)[self.player]

    def fill_slot_data(self) -> dict:
        return {option_name: self.get_setting(option_name).value for option_name in fnafb_options}

    def create_items(self):
        item_pool: List[FNaFBItem] = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        for name, data in item_table.items():
            quantity = data.max_quantity

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
        if (name == "Reveal Interior Walls") and not self.get_setting("trade_quest"):
            item.classification = ItemClassification.filler
        return FNaFBItem(name, data.classification, data.code, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.player)

    def generate_early(self):
        if not self.get_setting("trade_quest"):
            self.multiworld.get_location("Dining Area - Trade Alpha Voucher", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Dining Area - Trade Beta Voucher", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Dining Area - Trade Gamma Voucher", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Dining Area - Trade Omega Voucher", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Dining Area - Trade Spades Voucher", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Dining Area - Trade Hearts Voucher", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Dining Area - Trade Diamonds Voucher", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Dining Area - Trade Clubs Voucher", self.player).progress_type = LocationProgressType.EXCLUDED
        if not self.get_setting("interior_walls"):
            self.multiworld.get_location("Interior Walls - Chest 1", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 2", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 3", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 4", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 5", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 6", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 7", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 8", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 9", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 10", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 11", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 12", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 13", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 14", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 15", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 16", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 17", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 18", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 19", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 20", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 21", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 22", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 23", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 24", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 25", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 26", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 27", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 28", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - Chest 29", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Interior Walls - ???", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Dining Area - Trade Spades Voucher", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Dining Area - Trade Hearts Voucher", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Dining Area - Trade Diamonds Voucher", self.player).progress_type = LocationProgressType.EXCLUDED
            self.multiworld.get_location("Dining Area - Trade Clubs Voucher", self.player).progress_type = LocationProgressType.EXCLUDED


