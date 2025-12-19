from typing import Dict, List, NamedTuple, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .__init__ import FNaFB1World
from BaseClasses import MultiWorld, Region
from .Locations import FNaFB1Location, location_table, get_locations_by_category
from Options import Toggle


class FNaFB1RegionData(NamedTuple):
    locations: Optional[List[str]]


def create_regions(world: "FNaFB1World"):
    regions: Dict[str, FNaFB1RegionData] = {
        "Menu":                 FNaFB1RegionData(None),

        "Show Stage":           FNaFB1RegionData(["Show Stage - Left Chest",
                                                 "Show Stage - Right Chest",
                                                 "Dining Area - Punch the fuck out of the kitchen door",
                                                 "Show Stage - Camera",
                                                 "Dining Area - Camera",
                                                 "Kitchen - Chica",
                                                 "Show Stage - Toy Freddy",
                                                 "Dining Area - Chest",
                                                 "Dining Area - Dragon Dildo Ritual"]),
        
        "Levelsanity":          FNaFB1RegionData([]),
        
        "Trade Machine":        FNaFB1RegionData([]),

        "Trade Machine IW":     FNaFB1RegionData([]),

        "Pirate Cove":          FNaFB1RegionData(["Pirate Cove - Burn the place to the ground",
                                                 "Pirate Cove - Mangle",
                                                 "Pirate Cove - Camera",
                                                 "Pirate Cove - Chest"]),

        "Supply Closet":        FNaFB1RegionData(["Supply Closet - Chest",
                                                 "Supply Closet - Gamma Party Hat",
                                                 "Supply Closet - Camera"]),

        "Supply Closet BB":     FNaFB1RegionData([]),

        "West Hall":            FNaFB1RegionData(["West Hall - Camera",
                                                  "West Hall - Chest"]),

        "West Hall Corner":     FNaFB1RegionData(["West Hall Corner - Chest",
                                                 "West Hall Corner - Camera"]),

        "East Hall":            FNaFB1RegionData(["East Hall - Camera"]),

        "East Hall Corner":     FNaFB1RegionData(["East Hall Corner - Camera",
                                                 "East Hall Corner - Omega Party Hat",
                                                 "East Hall Corner - Chest"]),
        "East Hall Corner BB":  FNaFB1RegionData([]),

        "Restrooms":            FNaFB1RegionData(["Restrooms - Chest",
                                                 "Restrooms - Camera",
                                                 "Restrooms - Turn in Bonnie's Head Voucher",
                                                 "Restrooms - Toy Chica",
                                                 "Restrooms - The Puppet",
                                                 "Restrooms - Beta Party Hat"]),

        "Restrooms BB":         FNaFB1RegionData([]),

        "Backroom":             FNaFB1RegionData(["Backroom - Camera",
                                                 "Backroom - Alpha Party Hat",
                                                 "Backroom - Return Bonnie's Head",
                                                 "Backroom - Toy Bonnie",
                                                 "Backroom - Alpha Party Hat",
                                                 "Backroom - Chest"]),

        "Backroom BB":          FNaFB1RegionData([]),

        "Interior Walls":       FNaFB1RegionData(["Interior Walls - ???"]),

        "Office":               FNaFB1RegionData(["Office - Golden Freddy"]),

        "Scrungip DLC":         FNaFB1RegionData([]),

        "Scrungip DLC Levels":  FNaFB1RegionData([]),

        "Puppetmaster BB":      FNaFB1RegionData(["Show Stage - Puppetmaster BB"])
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
    for scrungip in get_locations_by_category("Scrungip").keys():
        regions["Scrungip DLC"].locations.append(scrungip)
    for scrungiplevels in get_locations_by_category("ScrungipLevelsanity").keys():
        regions["Scrungip DLC Levels"].locations.append(scrungiplevels)

    for name, data in regions.items():
        if name == "Interior Walls" and not world.options.interior_walls:
            continue
        if name == "Trade Machine IW" and (not world.options.interior_walls or not world.options.trade_quest):
            continue
        if name == "Trade Machine" and not world.options.trade_quest:
            continue
        if name == "Levelsanity" and not world.options.levelsanity:
            continue
        if name == "Scrungip DLC" and not world.options.developer_intrusion:
            continue
        if name == "Scrungip DLC Levels" and not world.options.developer_intrusion:
            continue
        if name == "Puppetmaster BB" and world.options.goal == "golden_freddy":
            continue
        world.multiworld.regions.append(create_region(world.multiworld, world.player, name, data))


def create_region(multiworld: MultiWorld, player: int, name: str, data: FNaFB1RegionData):
    region = Region(name, player, multiworld)
    if data.locations:
        for loc_name in data.locations:
            loc_data = location_table.get(loc_name)
            location = FNaFB1Location(player, loc_name, loc_data.code if loc_data else None, region)
            region.locations.append(location)

    return region
    
def connect_regions(multiworld: MultiWorld, source: str, target: List[str], rule=None):
    sourceRegion = multiworld.get_region(source)
    targetRegion = multiworld.get_region(target)
    sourceRegion.connect(targetRegion, rule=rule)