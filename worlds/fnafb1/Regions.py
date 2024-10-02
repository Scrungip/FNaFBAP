from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region
from .Locations import FNaFBLocation, location_table, get_locations_by_category
from Options import Toggle


class FNaFBRegionData(NamedTuple):
    locations: Optional[List[str]]


def create_regions(multiworld: MultiWorld, player: int):
    regions: Dict[str, FNaFBRegionData] = {
        "Menu":                 FNaFBRegionData(None),

        "Show Stage":           FNaFBRegionData(["Show Stage - Left Chest",
                                                 "Show Stage - Right Chest",
                                                 "Dining Area - Punch the fuck out of the kitchen door",
                                                 "Show Stage - Camera",
                                                 "Dining Area - Camera",
                                                 "Kitchen - Chica",
                                                 "Show Stage - Toy Freddy"]),
        
        "Levelsanity":          FNaFBRegionData([]),
        
        "Trade Machine":        FNaFBRegionData([]),

        "Trade Machine IW":     FNaFBRegionData([]),

        "Pirate Cove":          FNaFBRegionData(["Pirate Cove - Burn the place to the ground",
                                                 "Pirate Cove - Mangle",
                                                 "Pirate Cove - Camera"]),

        "Supply Closet":        FNaFBRegionData(["Supply Closet - Chest",
                                                 "Supply Closet - Gamma Party Hat",
                                                 "Supply Closet - Camera"]),

        "Supply Closet BB":     FNaFBRegionData([]),

        "West Hall":            FNaFBRegionData(["West Hall - Camera"]),

        "West Hall Corner":     FNaFBRegionData(["West Hall Corner - Chest",
                                                 "West Hall Corner - Camera"]),

        "East Hall":            FNaFBRegionData(["East Hall - Camera"]),

        "East Hall Corner":     FNaFBRegionData(["East Hall Corner - Camera",
                                                 "East Hall Corner - Omega Party Hat"]),
        "East Hall Corner BB":  FNaFBRegionData([]),

        "Restrooms":            FNaFBRegionData(["Restrooms - Chest",
                                                 "Restrooms - Camera",
                                                 "Restrooms - Turn in Bonnie's Head Voucher",
                                                 "Restrooms - Toy Chica",
                                                 "The Puppet",
                                                 "Restrooms - Beta Party Hat"]),

        "Restrooms BB":         FNaFBRegionData([]),

        "Backroom":             FNaFBRegionData(["Backroom - Camera",
                                                 "Backroom - Alpha Party Hat",
                                                 "Backroom - Return Bonnie's Head",
                                                 "Backroom - Toy Bonnie",
                                                 "Backroom - Alpha Party Hat"]),

        "Backroom BB":          FNaFBRegionData([]),

        "Interior Walls":       FNaFBRegionData(["Interior Walls - ???"]),

        "Office":               FNaFBRegionData(["Office - Golden Freddy"])
    }

    # Category hell
    for supplybb in get_locations_by_category("SupplyClosetBB").keys():
        regions["Supply Closet BB"].locations.append(supplybb)
    for cornerbb in get_locations_by_category("EastHallBB").keys():
        regions["East Hall Corner BB"].locations.append(cornerbb)
    for restroomsbb in get_locations_by_category("RestroomsBB").keys():
        regions["Restrooms BB"].locations.append(restroomsbb)
    for backroombb in get_locations_by_category("BackroomBB").keys():
        regions["Backroom BB"].locations.append(backroombb)
    for walls in get_locations_by_category("Walls").keys():
        regions["Interior Walls"].locations.append(walls)
    for voucher in get_locations_by_category("Trade").keys():
        regions["Trade Machine"].locations.append(voucher)
    for voucheriw in get_locations_by_category("TradeIW").keys():
        regions["Trade Machine IW"].locations.append(voucheriw)   
    for levels in get_locations_by_category("Levelsanity").keys():
        regions["Levelsanity"].locations.append(levels)

    for name, data in regions.items():
        if name == "Interior Walls" and multiworld.interior_walls[player] == Toggle.option_false:
            continue
        if name == "Trade Machine IW" and (multiworld.interior_walls[player] == Toggle.option_false or multiworld.trade_quest[player] == Toggle.option_false):
            continue
        if name == "Trade Machine" and multiworld.trade_quest[player] == Toggle.option_false:
            continue
        if name == "Levelsanity" and multiworld.levelsanity[player] == Toggle.option_false:
            continue
        multiworld.regions.append(create_region(multiworld, player, name, data))


def create_region(multiworld: MultiWorld, player: int, name: str, data: FNaFBRegionData):
    region = Region(name, player, multiworld)
    if data.locations:
        for loc_name in data.locations:
            loc_data = location_table.get(loc_name)
            location = FNaFBLocation(player, loc_name, loc_data.code if loc_data else None, region)
            region.locations.append(location)

    return region
    
def connect_regions(multiworld: MultiWorld, player: int, source: str, target: List[str], rule=None):
    sourceRegion = multiworld.get_region(source, player)
    targetRegion = multiworld.get_region(target, player)
    sourceRegion.connect(targetRegion, rule=rule)