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
    game = "Five Nights at Fuckboys"
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

    def generate_early(self):
        if not self.get_setting("trade_quest"):
            multiworld.get_location("Dining Area - Trade Alpha Voucher", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Dining Area - Trade Beta Voucher", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Dining Area - Trade Gamma Voucher", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Dining Area - Trade Omega Voucher", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Dining Area - Trade Spades Voucher", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Dining Area - Trade Hearts Voucher", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Dining Area - Trade Diamonds Voucher", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Dining Area - Trade Clubs Voucher", player).progress_type = LocationProgressType.EXCLUDED
        if not self.get_setting("interior_walls"):
            multiworld.get_location("Interior Walls - Chest 1", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 2", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 3", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 4", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 5", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 6", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 7", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 8", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 9", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 10", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 11", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 12", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 13", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 14", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 15", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 16", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 17", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 18", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 19", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 20", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 21", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 22", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 23", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 24", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 25", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 26", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 27", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 28", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - Chest 29", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Interior Walls - ???", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Dining Area - Trade Spades Voucher", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Dining Area - Trade Hearts Voucher", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Dining Area - Trade Diamonds Voucher", player).progress_type = LocationProgressType.EXCLUDED
            multiworld.get_location("Dining Area - Trade Clubs Voucher", player).progress_type = LocationProgressType.EXCLUDED


    def create_items(self):
        item_pool: List[FNaFBItem] = []

    def get_filler_item_name(self) -> str:
        fillers = get_items_by_category("Filler")
        weights = [data.weight for data in fillers.values()]
        return self.multiworld.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

    def create_item(self, name: str) -> FNaFBItem:
        data = item_table[name]
        return FNaFBItem(name, data.classification, data.code, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)

