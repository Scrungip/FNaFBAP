from typing import List

from BaseClasses import Tutorial, Location, LocationProgressType, CollectionState, MultiWorld, ItemClassification
from worlds.AutoWorld import WebWorld, World
from .Items import FNaFB2Item, FNaFB2ItemData, get_items_by_category, item_table
from .Locations import FNaFB2Location, location_table
from .Options import fnafb2_options
from .Regions import create_regions
from .Rules import set_rules


class FNaFB2Web(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Five Nights at Fuckboy's 2 client for use with Archipelago.",
        "English",
        "fnafb2_en.md",
        "fnafb2/en",
        ["Zuils and Scrungip"]
    )]


class FNaFB2World(World):
    """
    Are you Freddy for ready?
    """
    game = "Five Nights at Fuckboy's 2"
    option_definitions = fnafb2_options
    topology_present = True
    data_version = 4
    required_client_version = (0, 5, 0)
    web = FNaFB2Web()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    def get_setting(self, name: str):
        return getattr(self.multiworld, name)[self.player]

    def fill_slot_data(self) -> dict:
        return {option_name: self.get_setting(option_name).value for option_name in fnafb2_options}

    def create_items(self):
        item_pool: List[FNaFB2Item] = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        for name, data in item_table.items():
            quantity = data.max_quantity
            category = data.category
            classification = data.classification
            
            # If difficulty is standard, remove the cassettes, lucky soda, and double pizza
            if self.get_setting("difficulty") == 0 and (category == "Cassette" \
                or "Lucky Soda" in name or "Double Pizza" in name):
                continue
            
            # Ignore filler, it will be added in a later stage.
            if category == "Filler":
                continue

            item_pool += [self.create_item(name) for _ in range(quantity)]
        while len(item_pool) < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        fillers = get_items_by_category("Filler")
        weights = [data.weight for data in fillers.values()]
        return self.multiworld.random.choices(list(fillers.keys()), weights, k=1)[0]

    def create_item(self, name: str) -> FNaFB2Item:
        data = item_table[name]
        return FNaFB2Item(name, data.classification, data.code, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.player)