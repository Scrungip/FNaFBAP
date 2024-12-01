from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, LocationProgressType
from .Locations import FNaFB2Location, location_table, get_locations_by_category
from Options import Toggle


class FNaFB2RegionData(NamedTuple):
    locations: Optional[List[str]]


def create_regions(multiworld: MultiWorld, player: int):
    regions: Dict[str, FNaFB2RegionData] = {
        "Menu":                         FNaFB2RegionData(None),

        "Show Stage":                   FNaFB2RegionData(["Show Stage - Left Chest",
                                                 "Show Stage - Right Chest",
                                                 "Vending Machine - Turn in Sex Toy",
                                                 "Game Room - Punch the fuck out of the carousel",
                                                 "Show Stage - Camera",
                                                 "Game Room - Camera",
                                                 "Prize Corner - Camera",
                                                 "The Puppet",
                                                 "The Second Puppet"]),
        
        "Show Stage Proud":             FNaFB2RegionData(["Show Stage - Lucky Soda Chest",
                                                 "Show Stage - Double Pizza Chest"]),
        
        "Levelsanity":                  FNaFB2RegionData([]),

        "Trade Machine":                FNaFB2RegionData([]),

        "Kid's Cove":                   FNaFB2RegionData(["Kid's Cove - Return Sex Toy",
                                                  "Kid's Cove - Chest",
                                                  "Kid's Cove - Camera",
                                                  "Kid's Cove - Protection Hat"]),

        "Kid's Cove B.B.":              FNaFB2RegionData(["Turn in Sex Toy Voucher to B.B."]),
        
        "Kid's Cove Proud":             FNaFB2RegionData([]),
        
        "Kid's Cove Critical":          FNaFB2RegionData(["Kid's Cove - Chest 1",
                                                          "Kid's Cove - Chest 2"]),

        "Main Hall":                    FNaFB2RegionData(["Main Hall - Camera",
                                                  "Main Hall - Protection Hat"]),

        "Main Hall B.B.":               FNaFB2RegionData([]),

        "Women's Bathroom":             FNaFB2RegionData(["Women's Bathroom - Toy Chica",
                                                  "Women's Bathroom - Chest",
                                                  "Women's Bathroom - Splash Woman",
                                                  "The Puppet - Rod of Femininity A",
                                                  "The Second Puppet - Rod of Femininity B",
                                                  "B.B. - Foam Cupcakes A"]),
        
        "Women's Bathroom Proud":       FNaFB2RegionData([]),
        
        "Women's Bathroom Critical":    FNaFB2RegionData(["Women's Bathroom - Shadow Bonnie"]),

        "Men's Bathroom":               FNaFB2RegionData(["Men's Bathroom - Chest"]),

        "Men's Bathroom Proud":         FNaFB2RegionData([]),

        "Men's Bathroom Critical":      FNaFB2RegionData([]),

        "Parts/Service":                FNaFB2RegionData(["Parts/Service - Camera",
                                                  "Foxy's Steppin' Cove",
                                                  "Puppet Man Dating Sim",
                                                  "SEND CAKE TO CHILD",
                                                  "Boss Rush"]),

        "Parts/Service Proud":          FNaFB2RegionData([]),

        "Office Hall":                  FNaFB2RegionData([]),

        "Office Hall Proud":            FNaFB2RegionData([]),

        "Party Room 3":                 FNaFB2RegionData(["Party Room 3 - Withered Freddy",
                                                  "Party Room 3 - Camera",
                                                  "Party Room 3 - Protection Hat"]),

        "Party Room 3 B.B.":            FNaFB2RegionData([]),
        
        "Party Room 3 Proud":           FNaFB2RegionData([]),
        
        "Party Room 3 Critical":        FNaFB2RegionData([]),

        "Party Room 4":                 FNaFB2RegionData(["Party Room 4 - Withered Foxy",
                                                 "Party Room 4 - Withered Foxy Rematch",
                                                 "Party Room 4 - Camera"]),
        
        "Party Room 4 Proud":           FNaFB2RegionData([]),
        
        "Party Room 4 Critical":        FNaFB2RegionData([]),
        
        "Party Room 1":                 FNaFB2RegionData(["Party Room 1 - Withered Bonnie",
                                                  "Party Room 1 - Camera"]),
        
        "Party Room 1 Proud":           FNaFB2RegionData([]),
        
        "Party Room 1 Critical":        FNaFB2RegionData([]),
        
        "Left Vent":                    FNaFB2RegionData(["Left Vent - Camera"]),

        "Party Room 2":                 FNaFB2RegionData(["Party Room 2 - Withered Chica",
                                                  "Party Room 2 - Camera"]),

        "Party Room 2 Proud":           FNaFB2RegionData([]),

        "Party Room 2 Critical":        FNaFB2RegionData([]),

        "Right Vent":                   FNaFB2RegionData(["Right Vent - Toy Bonnie",
                                                  "Right Vent - Camera"]),

        "Office":                       FNaFB2RegionData(["Office - Left Chest",
                                                  "Office - Right Chest",
                                                  "Office - Camera",
                                                  "Office - Protection Hat"]),
        
        "Office B.B.":                  FNaFB2RegionData([]),

        "Office Proud":                 FNaFB2RegionData([]),

        "Office Critical":              FNaFB2RegionData([]),

        "Cave of the Past":             FNaFB2RegionData(["Cave of the Past - Dragon Dildo A",
                                                  "Cave of the Past - Dragon Dildo B",
                                                  "Cave of the Past - Dragon Dildo C",
                                                  "Cave of the Past - Dragon Dildo D",
                                                  "Cave of the Past - Dragon Dildo E",
                                                  "Cave of the Past - Dragon Dildo F"]),
        
        "B.B.'s Lair":                  FNaFB2RegionData(["B.B.'s Lair - B.B."]),
        
        "B.B. Giygas":                  FNaFB2RegionData(["B.B. Giygas - Left Chest 1",
                                                  "B.B. Giygas - Left Chest 2",
                                                  "B.B. Giygas - Left Chest 3",
                                                  "B.B. Giygas - Left Chest 4",
                                                  "B.B. Giygas - Left Chest 5",
                                                  "B.B. Giygas - Right Chest 1",
                                                  "B.B. Giygas - Right Chest 2",
                                                  "B.B. Giygas - Right Chest 3",
                                                  "B.B. Giygas"]),
        
        "Refurbs":                      FNaFB2RegionData(["Refurbs"])
    }

    # Category hell
    for mainhallbb in get_locations_by_category("MainHallBB").keys():
        regions["Main Hall B.B."].locations.append(mainhallbb)
    for partyroombb in get_locations_by_category("PartyRoomBB").keys():
        regions["Party Room 3 B.B."].locations.append(partyroombb)
    for kidscovebb in get_locations_by_category("KidsCoveBB").keys():
        regions["Kid's Cove B.B."].locations.append(kidscovebb)
    for officebb in get_locations_by_category("OfficeBB").keys():
        regions["Office B.B."].locations.append(officebb)
    for voucher in get_locations_by_category("Trade").keys():
        regions["Trade Machine"].locations.append(voucher)
    for levels in get_locations_by_category("Levelsanity").keys():
        regions["Levelsanity"].locations.append(levels)
    for cassette in get_locations_by_category("Cassette").keys():
        regions[cassette.split(" - ")[0] + " Proud"].locations.append(cassette)
    for gem in get_locations_by_category("Gem").keys():
        regions[gem.split(" - ")[0] + " Critical"].locations.append(gem)

    for name, data in regions.items():
        if name == "Trade Machine" and multiworld.trade_quest[player] == Toggle.option_false:
            continue
        if name == "Levelsanity" and (multiworld.levelsanity[player] == Toggle.option_false or multiworld.difficulty[player].value == 2):
            continue
        if "Critical" in name and multiworld.difficulty[player].value < 2:
            continue
        if "Proud" in name and multiworld.difficulty[player].value < 1:
            continue
        if name == "Refurbs" and multiworld.Goal[player].value == 0:
            continue
        multiworld.regions.append(create_region(multiworld, player, name, data))


def create_region(multiworld: MultiWorld, player: int, name: str, data: FNaFB2RegionData):
    region = Region(name, player, multiworld)
    if data.locations:
        for loc_name in data.locations:
            loc_data = location_table.get(loc_name)
            location = FNaFB2Location(player, loc_name, loc_data.code if loc_data else None, region)
            if (
                ("Rod of Femininity" in loc_name and multiworld.fem_rods[player] == Toggle.option_true)
                or (loc_name == "Boss Rush" and multiworld.extra_checks[player] == Toggle.option_true and multiworld.Goal[player] == 0)
                or (loc_name == "Cave of the Past - Dragon Dildo F" and multiworld.extra_checks[player] == Toggle.option_true and multiworld.Goal[player] == 0)
                or ("Shadow Bonnie" in loc_name and multiworld.shadow_bonnie[player] == Toggle.option_true and multiworld.difficulty[player].value == 2)
                ):
                location.progress_type = LocationProgressType.EXCLUDED
            region.locations.append(location)

    return region
    
def connect_regions(multiworld: MultiWorld, player: int, source: str, target: List[str], rule=None):
    sourceRegion = multiworld.get_region(source, player)
    targetRegion = multiworld.get_region(target, player)
    sourceRegion.connect(targetRegion, rule=rule)