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
                                                 "Dining Area - Camera",
                                                 "Kitchen - Chica",
                                                 "Show Stage - Toy Freddy"],

                                                ["Backroom",
                                                "Pirate Cove",
                                                "Restrooms",
                                                "Interior Walls",
                                                "West Hall",
                                                "East Hall",
                                                "Trade Machine"]),
        
        "Trade Machine":        FNaFBRegionData([],
                                                None),

        "Pirate Cove":          FNaFBRegionData(["Pirate Cove - Burn the place to the ground",
                                                 "Pirate Cove - Mangle",
                                                 "Pirate Cove - Camera"],

                                                None),

        "Supply Closet":        FNaFBRegionData(["Supply Closet - Chest",
                                                 "Supply Closet - Gamma Party Hat",
                                                 "Supply Closet - Camera"],

                                                ["Supply Closet BB"]),

        "Supply Closet BB":     FNaFBRegionData([],
                                                   
                                                None),

        "West Hall":            FNaFBRegionData(["West Hall - Camera"],  
                                                 
                                                ["Supply Closet",
                                                 "West Hall Corner"]),

        "West Hall Corner":     FNaFBRegionData(["West Hall Corner - Chest",
                                                 "West Hall Corner - Camera"],  

                                                ["Office"]),

        "East Hall":            FNaFBRegionData(["East Hall - Camera"],   
                                                ["East Hall Corner"]),

        "East Hall Corner":     FNaFBRegionData(["East Hall Corner - Camera",
                                                 "East Hall Corner - Omega Party Hat"],

                                                ["Office",
                                                 "East Hall Corner BB"]),
        "East Hall Corner BB":  FNaFBRegionData([],
                                                   
                                                None),

        "Restrooms":            FNaFBRegionData(["Restrooms - Chest",
                                                 "Restrooms - Camera",
                                                 "Restrooms - Turn in Bonnie's Head Voucher",
                                                 "Restrooms - Toy Chica",
                                                 "The Puppet",
                                                 "Restrooms - Beta Party Hat"],

                                                ["Show Stage", "Restrooms BB"]),

        "Restrooms BB":         FNaFBRegionData([],
                                                   
                                                None),

        "Backroom":             FNaFBRegionData(["Backroom - Camera",
                                                 "Backroom - Alpha Party Hat",
                                                 "Backroom - Return Bonnie's Head",
                                                 "Backroom - Toy Bonnie",
                                                 "Backroom - Alpha Party Hat"],

                                                ["Backroom BB"]),

        "Backroom BB":          FNaFBRegionData([],
                                                   
                                                None),

        "Interior Walls":       FNaFBRegionData(["Interior Walls - ???"],
                                                   
                                                None),

        "Office":               FNaFBRegionData(["Office - Golden Freddy"],
                                                   
                                                None),
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

    for name, data in regions.items():
        multiworld.regions.append(create_region(multiworld, player, name, data))


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
    
