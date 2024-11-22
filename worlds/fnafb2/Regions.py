from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, LocationProgressType
from .Locations import FNaFB2Location, location_table, get_locations_by_category
from Options import Toggle


class FNaFB2RegionData(NamedTuple):
    locations: Optional[List[str]]


def create_regions(multiworld: MultiWorld, player: int):
    regions: Dict[str, FNaFB2RegionData] = {
        "Menu":                 FNaFB2RegionData(None),

        "Show Stage":           FNaFB2RegionData(["Show Stage - Left Chest",
                                                 "Show Stage - Right Chest",
                                                 "Show Stage - Lucky Soda Chest",
                                                 "Show Stage - Double Pizza Chest",
                                                 "Vending Machine - Turn in Sex Toy",
                                                 "Game Room - Punch the fuck out of the carousel",
                                                 "Show Stage - Camera",
                                                 "Game Room - Camera",
                                                 "Prize Corner - Camera",
                                                 "The Puppet",
                                                 "The Second Puppet"]),
        
        "Levelsanity":          FNaFB2RegionData([]),
        
        "Trade Machine":        FNaFB2RegionData([]),
        
        "Kid's Cove":           FNaFB2RegionData(["Kid's Cove - Return Sex Toy",
                                                  "Kid's Cove - Chest",
                                                  "Kid's Cove - Camera",
                                                  "Kid's Cove - Protection Hat"]),

        "Kid's Cove BB":        FNaFB2RegionData(["Turn in Sex Toy Voucher to BB"]),

        "Main Hall":            FNaFB2RegionData(["Main Hall - Camera",
                                                  "Main Hall - Protection Hat"]),

        "Main Hall BB":         FNaFB2RegionData([]),

        "Women's Bathroom":     FNaFB2RegionData(["Women's Bathroom - Toy Chica",
                                                  "Women's Bathroom - Chest",
                                                  "Women's Bathroom - Splash Woman",
                                                  "The Puppet - Rod of Femininity A",
                                                  "The Second Puppet - Rod of Femininity B",
                                                  "BB - Foam Cupcakes A"]),

        "Men's Bathroom":       FNaFB2RegionData(["Men's Bathroom - Chest"]),

        "Parts/Service":        FNaFB2RegionData(["Parts/Service - Camera",
                                                  "Foxy's Steppin' Cove",
                                                  "Puppet Man Dating Sim",
                                                  "SEND CAKE TO CHILD",
                                                  "Boss Rush"]),

        "Office Hall":          FNaFB2RegionData([]),

        "Party Room 3":         FNaFB2RegionData(["Party Room 3 - Withered Freddy",
                                                  "Party Room 3 - Camera",
                                                  "Party Room 3 - Protection Hat"]),

        "Party Room 3 BB":      FNaFB2RegionData([]),

        "Party Room 4":         FNaFB2RegionData(["Party Room 4 - Withered Foxy",
                                                 "Party Room 4 - Withered Foxy Rematch",
                                                 "Party Room 4 - Camera"]),
        
        "Party Room 1":         FNaFB2RegionData(["Party Room 1 - Withered Bonnie",
                                                  "Party Room 1 - Camera"]),
        
        "Left Vent":            FNaFB2RegionData(["Left Vent - Camera"]),

        "Party Room 2":         FNaFB2RegionData(["Party Room 2 - Withered Chica",
                                                  "Party Room 2 - Camera"]),

        "Right Vent":           FNaFB2RegionData(["Right Vent - Toy Bonnie",
                                                  "Right Vent - Camera"]),

        "Office":               FNaFB2RegionData(["Office - Left Chest",
                                                  "Office - Right Chest",
                                                  "Office - Camera",
                                                  "Office - Protection Hat"]),
        
        "Office BB":            FNaFB2RegionData([]),

        "Cave of the Past":     FNaFB2RegionData(["Cave of the Past - Dragon Dildo A",
                                                  "Cave of the Past - Dragon Dildo B",
                                                  "Cave of the Past - Dragon Dildo C",
                                                  "Cave of the Past - Dragon Dildo D",
                                                  "Cave of the Past - Dragon Dildo E",
                                                  "Cave of the Past - Dragon Dildo F",
                                                  "BB's Lair - BB"]),
        
        "BB Giygas":           FNaFB2RegionData(["BB Giygas - Left Chest 1",
                                                  "BB Giygas - Left Chest 2",
                                                  "BB Giygas - Left Chest 3",
                                                  "BB Giygas - Left Chest 4",
                                                  "BB Giygas - Left Chest 5",
                                                  "BB Giygas - Right Chest 1",
                                                  "BB Giygas - Right Chest 2",
                                                  "BB Giygas - Right Chest 3",
                                                  "BB Giygas"]),
        
        "Refurbs":             FNaFB2RegionData(["Refurbs"])
    }

    # Category hell
    for mainhallbb in get_locations_by_category("MainHallBB").keys():
        regions["Main Hall BB"].locations.append(mainhallbb)
    for partyroombb in get_locations_by_category("PartyRoomBB").keys():
        regions["Party Room 3 BB"].locations.append(partyroombb)
    for kidscovebb in get_locations_by_category("KidsCoveBB").keys():
        regions["Kid's Cove BB"].locations.append(kidscovebb)
    for officebb in get_locations_by_category("OfficeBB").keys():
        regions["Office BB"].locations.append(officebb)
    for voucher in get_locations_by_category("Trade").keys():
        regions["Trade Machine"].locations.append(voucher)
    for levels in get_locations_by_category("Levelsanity").keys():
        regions["Levelsanity"].locations.append(levels)
    if multiworld.difficulty[player].value == 1:
        regions["Show Stage"].locations.append("Show Stage - Cassette Radar Chest")
        regions["Kid's Cove"].locations.append("Kid's Cove - Cassette")
        regions["Parts/Service"].locations.append("Parts/Service - Cassette")
        regions["Men's Bathroom"].locations.append("Men's Bathroom - Cassette")
        regions["Women's Bathroom"].locations.append("Women's Bathroom - Cassette")
        regions["Office"].locations.extend(["Office - Cassette", "Office - Rap God"])
        regions["Office Hall"].locations.append("Office Hall - Cassette")
        regions["Party Room 1"].locations.append("Party Room 1 - Cassette")
        regions["Party Room 2"].locations.append("Party Room 2 - Cassette")
        regions["Party Room 3"].locations.append("Party Room 3 - Cassette")
        regions["Party Room 4"].locations.append("Party Room 4 - Cassette")

    for name, data in regions.items():
        if name == "Trade Machine" and multiworld.trade_quest[player] == Toggle.option_false:
            continue
        if name == "Levelsanity" and multiworld.levelsanity[player] == Toggle.option_false:
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
            if ("Rod of Femininity" in loc_name and multiworld.fem_rods[player] == Toggle.option_true) \
                or (loc_name == "Boss Rush" and multiworld.boss_rush[player] == Toggle.option_true and multiworld.Goal[player] == 0) \
                    or (loc_name == "Cave of the Past - Dragon Dildo F" and multiworld.boss_rush[player] == Toggle.option_true):
                location.progress_type = LocationProgressType.EXCLUDED
            region.locations.append(location)

    return region
    
def connect_regions(multiworld: MultiWorld, player: int, source: str, target: List[str], rule=None):
    sourceRegion = multiworld.get_region(source, player)
    targetRegion = multiworld.get_region(target, player)
    sourceRegion.connect(targetRegion, rule=rule)