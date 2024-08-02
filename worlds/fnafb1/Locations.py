from typing import Dict, NamedTuple, Optional

from BaseClasses import Location


class FNaFBLocation(Location):
    game: str = "Five Nights at Fuckboy's"


class FNaFBLocationData(NamedTuple):
    category: str
    code: Optional[int] = None


def get_locations_by_category(category: str) -> Dict[str, FNaFBLocationData]:
    location_dict: Dict[str, FNaFBLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict


location_table: Dict[str, FNaFBLocationData] = {
    # General Checks
    "Show Stage - Left Chest":                                            FNaFBLocationData("General",   756783_000),
    "Show Stage - Right Chest":                                           FNaFBLocationData("General",   756783_001),
    "Dining Area - Punch the fuck out of the kitchen door":               FNaFBLocationData("General",   756783_002),
    "West Hall Corner - Chest":                                           FNaFBLocationData("General",   756783_003),
    "Supply Closet - Chest":                                              FNaFBLocationData("General",   756783_004),
    "Restrooms - Chest":                                                  FNaFBLocationData("General",   756783_005),
    # Quests
    "Restrooms - Turn in Bonnie's Head Voucher":                          FNaFBLocationData("Quests",   756783_006),
    "Backroom - Return Bonnie's Head":                                    FNaFBLocationData("Quests",   756783_007),
    "Pirate Cove - Burn the place to the ground":                         FNaFBLocationData("Quests",   756783_008),
    # Trade-Ins
    "Dining Area - Trade Alpha Voucher":                                  FNaFBLocationData("Trade",   756783_009),
    "Dining Area - Trade Beta Voucher":                                   FNaFBLocationData("Trade",   756783_010),
    "Dining Area - Trade Gamma Voucher":                                  FNaFBLocationData("Trade",   756783_011),
    "Dining Area - Trade Omega Voucher":                                  FNaFBLocationData("Trade",   756783_012),
    "Dining Area - Trade Spades Voucher":                                 FNaFBLocationData("TradeIW",   756783_013),
    "Dining Area - Trade Hearts Voucher":                                 FNaFBLocationData("TradeIW",   756783_014),
    "Dining Area - Trade Diamonds Voucher":                               FNaFBLocationData("TradeIW",   756783_015),
    "Dining Area - Trade Clubs Voucher":                                  FNaFBLocationData("TradeIW",   756783_016),
    #Interior Walls
    "Interior Walls - Chest 1":                                           FNaFBLocationData("Walls",   756783_017),
    "Interior Walls - Chest 2":                                           FNaFBLocationData("Walls",   756783_018),
    "Interior Walls - Chest 3":                                           FNaFBLocationData("Walls",   756783_019),
    "Interior Walls - Chest 4":                                           FNaFBLocationData("Walls",   756783_020),
    "Interior Walls - Chest 5":                                           FNaFBLocationData("Walls",   756783_021),
    "Interior Walls - Chest 6":                                           FNaFBLocationData("Walls",   756783_022),
    "Interior Walls - Chest 7":                                           FNaFBLocationData("Walls",   756783_023),
    "Interior Walls - Chest 8":                                           FNaFBLocationData("Walls",   756783_024),
    "Interior Walls - Chest 9":                                           FNaFBLocationData("Walls",   756783_025),
    "Interior Walls - Chest 10":                                          FNaFBLocationData("Walls",   756783_026),
    "Interior Walls - Chest 11":                                          FNaFBLocationData("Walls",   756783_027),
    "Interior Walls - Chest 12":                                          FNaFBLocationData("Walls",   756783_028),
    "Interior Walls - Chest 13":                                          FNaFBLocationData("Walls",   756783_029),
    "Interior Walls - Chest 14":                                          FNaFBLocationData("Walls",   756783_030),
    "Interior Walls - Chest 15":                                          FNaFBLocationData("Walls",   756783_031),
    "Interior Walls - Chest 16":                                          FNaFBLocationData("Walls",   756783_032),
    "Interior Walls - Chest 17":                                          FNaFBLocationData("Walls",   756783_033),
    "Interior Walls - Chest 18":                                          FNaFBLocationData("Walls",   756783_034),
    "Interior Walls - Chest 19":                                          FNaFBLocationData("Walls",   756783_035),
    "Interior Walls - Chest 20":                                          FNaFBLocationData("Walls",   756783_036),
    "Interior Walls - Chest 21":                                          FNaFBLocationData("Walls",   756783_037),
    "Interior Walls - Chest 22":                                          FNaFBLocationData("Walls",   756783_038),
    "Interior Walls - Chest 23":                                          FNaFBLocationData("Walls",   756783_039),
    "Interior Walls - Chest 24":                                          FNaFBLocationData("Walls",   756783_040),
    "Interior Walls - Chest 25":                                          FNaFBLocationData("Walls",   756783_041),
    "Interior Walls - Chest 26":                                          FNaFBLocationData("Walls",   756783_042),
    "Interior Walls - Chest 27":                                          FNaFBLocationData("Walls",   756783_043),
    "Interior Walls - Chest 28":                                          FNaFBLocationData("Walls",   756783_044),
    "Interior Walls - Chest 29":                                          FNaFBLocationData("Walls",   756783_045),
    # Bosses
    "Show Stage - Toy Freddy":                                            FNaFBLocationData("Boss",   756783_046),
    "Backroom - Toy Bonnie":                                              FNaFBLocationData("Boss",   756783_047),
    "Restrooms - Toy Chica":                                              FNaFBLocationData("Boss",   756783_048),
    "Pirate Cove - Mangle":                                               FNaFBLocationData("Boss",   756783_049),
    "The Puppet":                                                         FNaFBLocationData("Boss",   756783_050),
    "Interior Walls - ???":                                               FNaFBLocationData("Walls",   756783_051),
    "Office - Golden Freddy":                                             FNaFBLocationData("Boss",   756783_052),
    # Shops
    "Backroom BB - Item 1":                                               FNaFBLocationData("BackroomBB",   756783_053),
    "Backroom BB - Item 2":                                               FNaFBLocationData("BackroomBB",   756783_054),
    "Backroom BB - Item 3":                                               FNaFBLocationData("BackroomBB",   756783_055),
    "Backroom BB - Item 4":                                               FNaFBLocationData("BackroomBB",   756783_056),
    "Backroom BB - Item 5":                                               FNaFBLocationData("BackroomBB",   756783_057),
    "Backroom BB - Item 6":                                               FNaFBLocationData("BackroomBB",   756783_058),
    "Restrooms BB - Item 1":                                              FNaFBLocationData("RestroomsBB",   756783_059),
    "Restrooms BB - Item 2":                                              FNaFBLocationData("RestroomsBB",   756783_060),
    "Restrooms BB - Item 3":                                              FNaFBLocationData("RestroomsBB",   756783_061),
    "Restrooms BB - Item 4":                                              FNaFBLocationData("RestroomsBB",   756783_062),
    "Restrooms BB - Item 5":                                              FNaFBLocationData("RestroomsBB",   756783_063),
    "Restrooms BB - Item 6":                                              FNaFBLocationData("RestroomsBB",   756783_064),
    "Restrooms BB - Item 7":                                              FNaFBLocationData("RestroomsBB",   756783_065),
    "Restrooms BB - Item 8":                                              FNaFBLocationData("RestroomsBB",   756783_066),
    "Supply Closet BB - Item 1":                                          FNaFBLocationData("SupplyClosetBB",   756783_067),
    "Supply Closet BB - Item 2":                                          FNaFBLocationData("SupplyClosetBB",   756783_068),
    "Supply Closet BB - Item 3":                                          FNaFBLocationData("SupplyClosetBB",   756783_069),
    "Supply Closet BB - Item 4":                                          FNaFBLocationData("SupplyClosetBB",   756783_070),
    "Supply Closet BB - Item 5":                                          FNaFBLocationData("SupplyClosetBB",   756783_071),
    "Supply Closet BB - Item 6":                                          FNaFBLocationData("SupplyClosetBB",   756783_072),
    "Supply Closet BB - Item 7":                                          FNaFBLocationData("SupplyClosetBB",   756783_073),
    "Supply Closet BB - Item 8":                                          FNaFBLocationData("SupplyClosetBB",   756783_074),
    "Supply Closet BB - Item 9":                                          FNaFBLocationData("SupplyClosetBB",   756783_075),
    "Supply Closet BB - Item 10":                                         FNaFBLocationData("SupplyClosetBB",   756783_076),
    "East Hall Corner BB - Item 1":                                       FNaFBLocationData("EastHallBB",   756783_077),
    "East Hall Corner BB - Item 2":                                       FNaFBLocationData("EastHallBB",   756783_078),
    "East Hall Corner BB - Item 3":                                       FNaFBLocationData("EastHallBB",   756783_079),
    "East Hall Corner BB - Item 4":                                       FNaFBLocationData("EastHallBB",   756783_080),
    "East Hall Corner BB - Item 5":                                       FNaFBLocationData("EastHallBB",   756783_081),
    "East Hall Corner BB - Item 6":                                       FNaFBLocationData("EastHallBB",   756783_082),
    "East Hall Corner BB - Item 7":                                       FNaFBLocationData("EastHallBB",   756783_083),
    "East Hall Corner BB - Item 8":                                       FNaFBLocationData("EastHallBB",   756783_084),
    "East Hall Corner BB - Item 9":                                       FNaFBLocationData("EastHallBB",   756783_085),
    "East Hall Corner BB - Item 10":                                      FNaFBLocationData("EastHallBB",   756783_086),
    "East Hall Corner BB - Item 11":                                      FNaFBLocationData("EastHallBB",   756783_087),
    "East Hall Corner BB - Item 12":                                      FNaFBLocationData("EastHallBB",   756783_088),
    # Cameras
    "Show Stage - Camera":                                                  FNaFBLocationData("Cameras",   756783_089),
    "Dining Area - Camera":                                                 FNaFBLocationData("Cameras",   756783_090),
    "Backroom - Camera":                                                    FNaFBLocationData("Cameras",   756783_091),
    "West Hall - Camera":                                                   FNaFBLocationData("Cameras",   756783_092),
    "East Hall - Camera":                                                   FNaFBLocationData("Cameras",   756783_093),
    "Restrooms - Camera":                                                   FNaFBLocationData("Cameras",   756783_094),
    "Pirate Cove - Camera":                                                 FNaFBLocationData("Cameras",   756783_095),
    "Supply Closet - Camera":                                               FNaFBLocationData("Cameras",   756783_096),
    "East Hall Corner - Camera":                                            FNaFBLocationData("Cameras",   756783_097),
    "West Hall Corner - Camera":                                            FNaFBLocationData("Cameras",   756783_098),
    # Party Hats
    "Backroom - Alpha Party Hat":                                           FNaFBLocationData("PartyHats",    756783_099),
    "Restrooms - Beta Party Hat":                                           FNaFBLocationData("PartyHats",    756783_100),
    "Supply Closet - Gamma Party Hat":                                      FNaFBLocationData("PartyHats",    756783_101),
    "East Hall Corner - Omega Party Hat":                                   FNaFBLocationData("PartyHats",    756783_102),
    # Whoops I forgot this one
    "Kitchen - Chica":                                                      FNaFBLocationData("General",      756783_103),
    # Levels
    **{f"Freddy - Level {i+1}":                                             FNaFBLocationData("Levelsanity",  756783_110 + i) for i in range(0, 20)},
    **{f"Bonnie - Level {i+1}":                                             FNaFBLocationData("Levelsanity",  756783_140 + i) for i in range(0, 20)},
    **{f"Chica - Level {i+1}":                                              FNaFBLocationData("Levelsanity",  756783_170 + i) for i in range(0, 20)},
    **{f"Foxy - Level {i+1}":                                               FNaFBLocationData("Levelsanity",  756783_200 + i) for i in range(0, 20)}
}
