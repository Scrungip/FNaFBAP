from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, Entrance
from .Locations import FNaFBLocation, location_table, get_locations_by_category


class FNaFBRegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]


def create_regions(multiworld: MultiWorld, player: int):
    regions: Dict[str, FNaFBRegionData] = {
        "Menu":                 FNaFBRegionData(None, ["Show Stage"]),
        "Show Stage":           FNaFBRegionData([],   ["Backroom", "Pirate Cove", "Restrooms", "Interior Walls", "West Hall", "East Hall"]),
        "Pirate Cove":          FNaFBRegionData([],   ["Show Stage"]),
        "Supply Closet":        FNaFBRegionData([],   ["West Hall", "Supply Closet BB"]),
        "Supply Closet BB":     FNaFBRegionData([],   ["Supply Closet"]),
        "West Hall":            FNaFBRegionData([],   ["Show Stage", "Supply Closet", "West Hall Corner"]),
        "West Hall Corner":     FNaFBRegionData([],   ["West Hall", "Office"]),
        "East Hall":            FNaFBRegionData([],   ["Show Stage", "East Hall Corner"]),
        "East Hall Corner":     FNaFBRegionData([],   ["East Hall", "Office", "East Hall Corner BB"]),
        "East Hall Corner BB":  FNaFBRegionData([],   ["East Hall Corner"]),
        "Restrooms":            FNaFBRegionData([],   ["Show Stage", "Restrooms BB"]),
        "Restrooms BB":         FNaFBRegionData([],   ["Restrooms"]),
        "Backroom":             FNaFBRegionData([],   ["Show Stage" "Backroom BB"]),
        "Backroom BB":          FNaFBRegionData([],   ["Backroom"]),
        "Interior Walls":       FNaFBRegionData([],   ["Show Stage"]),
        "Office":               FNaFBRegionData([],   None),
    }

    # Manor & Special
    for manor in get_locations_by_category("Manor").keys():
        regions["The Manor"].locations.append(manor)
    for special in get_locations_by_category("Special").keys():
        regions["Castle Hamson"].locations.append(special)

    # Chests
    chests = int(multiworld.chests_per_zone[player])
    for i in range(0, chests):
        if multiworld.universal_chests[player]:
            regions["Castle Hamson"].locations.append(f"Chest {i + 1}")
            regions["Forest Abkhazia"].locations.append(f"Chest {i + 1 + chests}")
            regions["The Maya"].locations.append(f"Chest {i + 1 + (chests * 2)}")
            regions["Land of Darkness"].locations.append(f"Chest {i + 1 + (chests * 3)}")
        else:
            regions["Castle Hamson"].locations.append(f"Castle Hamson - Chest {i + 1}")
            regions["Forest Abkhazia"].locations.append(f"Forest Abkhazia - Chest {i + 1}")
            regions["The Maya"].locations.append(f"The Maya - Chest {i + 1}")
            regions["Land of Darkness"].locations.append(f"Land of Darkness - Chest {i + 1}")

    # Fairy Chests
    chests = int(multiworld.fairy_chests_per_zone[player])
    for i in range(0, chests):
        if multiworld.universal_fairy_chests[player]:
            regions["Castle Hamson"].locations.append(f"Fairy Chest {i + 1}")
            regions["Forest Abkhazia"].locations.append(f"Fairy Chest {i + 1 + chests}")
            regions["The Maya"].locations.append(f"Fairy Chest {i + 1 + (chests * 2)}")
            regions["Land of Darkness"].locations.append(f"Fairy Chest {i + 1 + (chests * 3)}")
        else:
            regions["Castle Hamson"].locations.append(f"Castle Hamson - Fairy Chest {i + 1}")
            regions["Forest Abkhazia"].locations.append(f"Forest Abkhazia - Fairy Chest {i + 1}")
            regions["The Maya"].locations.append(f"The Maya - Fairy Chest {i + 1}")
            regions["Land of Darkness"].locations.append(f"Land of Darkness - Fairy Chest {i + 1}")

    # Set up the regions correctly.
    for name, data in regions.items():
        multiworld.regions.append(create_region(multiworld, player, name, data))

    multiworld.get_entrance("Castle Hamson", player).connect(multiworld.get_region("Castle Hamson", player))
    multiworld.get_entrance("The Manor", player).connect(multiworld.get_region("The Manor", player))
    multiworld.get_entrance("Forest Abkhazia", player).connect(multiworld.get_region("Forest Abkhazia", player))
    multiworld.get_entrance("The Maya", player).connect(multiworld.get_region("The Maya", player))
    multiworld.get_entrance("Land of Darkness", player).connect(multiworld.get_region("Land of Darkness", player))
    multiworld.get_entrance("The Fountain Room", player).connect(multiworld.get_region("The Fountain Room", player))


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
