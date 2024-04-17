from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, Entrance
from .Locations import FNaFBLocation, location_table, get_locations_by_category


class FNaFBRegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]


def create_regions(multiworld: MultiWorld, player: int):
    regions: Dict[str, FNaFBRegionData] = {
        "Menu":                 FNaFBRegionData(None, 
                                                ["Show Stage"]),
        "Show Stage":           FNaFBRegionData(["Show Stage - Left Chest",
                                                 "Show Stage - Right Chest",
                                                 "Dining Area - Punch the fuck out of the kitchen door",
                                                 "Show Stage - Camera",
                                                 "Dining Room - Camera",
                                                 "Kitchen - Chica",
                                                 "Show Stage - Toy Freddy"],  
                                                ["Backroom",
                                                "Pirate Cove",
                                                "Restrooms",
                                                "Interior Walls",
                                                "West Hall",
                                                "East Hall"]),
        "Pirate Cove":          FNaFBRegionData(["Pirate Cove - Burn the place to the ground",
                                                 "Pirate Cove - Mangle",
                                                 "Pirate Cove - Camera"],   
                                                ["Show Stage"]),
        "Supply Closet":        FNaFBRegionData(["Supply Closet - Chest",
                                                 "Supply Closet - Gamma Party Hat",
                                                 "Supply Closet - Camera"],   
                                                ["West Hall", "Supply Closet BB"]),
        "Supply Closet BB":     FNaFBRegionData([],   
                                                ["Supply Closet"]),
        "West Hall":            FNaFBRegionData(["West Hall - Camera"],   
                                                ["Show Stage", "Supply Closet", "West Hall Corner"]),
        "West Hall Corner":     FNaFBRegionData(["West Hall Corner - Chest",
                                                 "West Hall Corner - Camera"],   
                                                ["West Hall", "Office"]),
        "East Hall":            FNaFBRegionData(["East Hall - Camera"],   
                                                ["Show Stage", "East Hall Corner"]),
        "East Hall Corner":     FNaFBRegionData(["East Hall Corner - Camera",
                                                 "East Hall Corner - Omega Party Hat"],   
                                                ["East Hall", "Office", "East Hall Corner BB"]),
        "East Hall Corner BB":  FNaFBRegionData([],   
                                                ["East Hall Corner"]),
        "Restrooms":            FNaFBRegionData(["Restrooms - Chest",
                                                 "Restrooms - Camera",
                                                 "Restrooms - Turn in Bonnie's Head Voucher"],   
                                                ["Show Stage", "Restrooms BB"]),
        "Restrooms BB":         FNaFBRegionData([],   
                                                ["Restrooms"]),
        "Backroom":             FNaFBRegionData(["Backroom - Camera",
                                                 "Backroom - Alpha Party Hat",
                                                 "Backroom - Return Bonnie's Head"],   
                                                ["Show Stage" "Backroom BB"]),
        "Backroom BB":          FNaFBRegionData([],   
                                                ["Backroom"]),
        "Interior Walls":       FNaFBRegionData(["Interior Walls - ???"],   
                                                ["Show Stage"]),
        "Office":               FNaFBRegionData(["Office - Golden Freddy"],   
                                                None),
    }

    # Manor & Special
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
    for weapontrade in get_locations_by_category("Trade").keys():
        regions["Show Stage"].locations.append(weapontrade)


def create_region(multiworld: MultiWorld, player: int, name: str, data: FNaFBRegionData):
    region = Region(name, player, multiworld)
    if data.locations:
        for loc_name in data.locations:
            loc_data = location_table.get(loc_name)
            location = FNaFBLocation(player, loc_name, loc_data.code if loc_data else None, region)
            region.locations.append(location)

    if data.region_exits:
        for exit in data.region_exits:
            entrance = Entrance(player, exit, region)
            region.exits.append(entrance)

    return region
