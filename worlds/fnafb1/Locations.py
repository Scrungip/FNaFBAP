from typing import Dict, NamedTuple, Optional

from BaseClasses import Location


class FNaFB1Location(Location):
    game: str = "Five Nights at Fuckboy's"


class FNaFB1LocationData(NamedTuple):
    category: str
    code: Optional[int] = None


def get_locations_by_category(category: str) -> Dict[str, FNaFB1LocationData]:
    location_dict: Dict[str, FNaFB1LocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict


location_table: Dict[str, FNaFB1LocationData] = {
    # General Checks
    "Show Stage - Left Chest":                                            FNaFB1LocationData("General",   756783_000),
    "Show Stage - Right Chest":                                           FNaFB1LocationData("General",   756783_001),
    "Dining Area - Punch the fuck out of the kitchen door":               FNaFB1LocationData("General",   756783_002),
    "West Hall Corner - Chest":                                           FNaFB1LocationData("General",   756783_003),
    "Supply Closet - Chest":                                              FNaFB1LocationData("General",   756783_004),
    "Restrooms - Chest":                                                  FNaFB1LocationData("General",   756783_005),
    # Quests
    "Restrooms - Turn in Bonnie's Head Voucher":                          FNaFB1LocationData("Quests",   756783_006),
    "Backroom - Return Bonnie's Head":                                    FNaFB1LocationData("Quests",   756783_007),
    "Pirate Cove - Burn the place to the ground":                         FNaFB1LocationData("Quests",   756783_008),
    # Trade-Ins
    "Show Stage - Trade Alpha Voucher":                                   FNaFB1LocationData("Trade",   756783_009),
    "Show Stage - Trade Beta Voucher":                                    FNaFB1LocationData("Trade",   756783_010),
    "Show Stage - Trade Gamma Voucher":                                   FNaFB1LocationData("Trade",   756783_011),
    "Show Stage - Trade Omega Voucher":                                   FNaFB1LocationData("Trade",   756783_012),
    "Show Stage - Trade Spades Voucher":                                  FNaFB1LocationData("TradeIW",   756783_013),
    "Show Stage - Trade Hearts Voucher":                                  FNaFB1LocationData("TradeIW",   756783_014),
    "Show Stage - Trade Diamonds Voucher":                                FNaFB1LocationData("TradeIW",   756783_015),
    "Show Stage - Trade Clubs Voucher":                                   FNaFB1LocationData("TradeIW",   756783_016),
    #Interior Walls
    "Interior Walls - Chest 1":                                           FNaFB1LocationData("Walls",   756783_017),
    "Interior Walls - Chest 2":                                           FNaFB1LocationData("Walls",   756783_018),
    "Interior Walls - Chest 3":                                           FNaFB1LocationData("Walls",   756783_019),
    "Interior Walls - Chest 4":                                           FNaFB1LocationData("Walls",   756783_020),
    "Interior Walls - Chest 5":                                           FNaFB1LocationData("Walls",   756783_021),
    "Interior Walls - Chest 6":                                           FNaFB1LocationData("Walls",   756783_022),
    "Interior Walls - Chest 7":                                           FNaFB1LocationData("Walls",   756783_023),
    "Interior Walls - Chest 8":                                           FNaFB1LocationData("Walls",   756783_024),
    "Interior Walls - Chest 9":                                           FNaFB1LocationData("Walls",   756783_025),
    "Interior Walls - Chest 10":                                          FNaFB1LocationData("Walls",   756783_026),
    "Interior Walls - Chest 11":                                          FNaFB1LocationData("Walls",   756783_027),
    "Interior Walls - Chest 12":                                          FNaFB1LocationData("Walls",   756783_028),
    "Interior Walls - Chest 13":                                          FNaFB1LocationData("Walls",   756783_029),
    "Interior Walls - Chest 14":                                          FNaFB1LocationData("Walls",   756783_030),
    "Interior Walls - Chest 15":                                          FNaFB1LocationData("Walls",   756783_031),
    "Interior Walls - Chest 16":                                          FNaFB1LocationData("Walls",   756783_032),
    "Interior Walls - Chest 17":                                          FNaFB1LocationData("Walls",   756783_033),
    "Interior Walls - Chest 18":                                          FNaFB1LocationData("Walls",   756783_034),
    "Interior Walls - Chest 19":                                          FNaFB1LocationData("Walls",   756783_035),
    "Interior Walls - Chest 20":                                          FNaFB1LocationData("Walls",   756783_036),
    "Interior Walls - Chest 21":                                          FNaFB1LocationData("Walls",   756783_037),
    "Interior Walls - Chest 22":                                          FNaFB1LocationData("Walls",   756783_038),
    "Interior Walls - Chest 23":                                          FNaFB1LocationData("Walls",   756783_039),
    "Interior Walls - Chest 24":                                          FNaFB1LocationData("Walls",   756783_040),
    "Interior Walls - Chest 25":                                          FNaFB1LocationData("Walls",   756783_041),
    "Interior Walls - Chest 26":                                          FNaFB1LocationData("Walls",   756783_042),
    "Interior Walls - Chest 27":                                          FNaFB1LocationData("Walls",   756783_043),
    "Interior Walls - Chest 28":                                          FNaFB1LocationData("Walls",   756783_044),
    "Interior Walls - Chest 29":                                          FNaFB1LocationData("Walls",   756783_045),
    # Bosses
    "Show Stage - Toy Freddy":                                            FNaFB1LocationData("Boss",   756783_046),
    "Backroom - Toy Bonnie":                                              FNaFB1LocationData("Boss",   756783_047),
    "Restrooms - Toy Chica":                                              FNaFB1LocationData("Boss",   756783_048),
    "Pirate Cove - Mangle":                                               FNaFB1LocationData("Boss",   756783_049),
    "Restrooms - The Puppet":                                             FNaFB1LocationData("Boss",   756783_050),
    "Interior Walls - ???":                                               FNaFB1LocationData("Walls",   756783_051),
    "Office - Golden Freddy":                                             FNaFB1LocationData("Boss",   756783_052),
    # Shops
    "Backroom BB - Item 1":                                               FNaFB1LocationData("BackroomBB",   756783_053),
    "Backroom BB - Item 2":                                               FNaFB1LocationData("BackroomBB",   756783_054),
    "Backroom BB - Item 3":                                               FNaFB1LocationData("BackroomBB",   756783_055),
    "Backroom BB - Item 4":                                               FNaFB1LocationData("BackroomBB",   756783_056),
    "Backroom BB - Item 5":                                               FNaFB1LocationData("BackroomBB",   756783_057),
    "Backroom BB - Item 6":                                               FNaFB1LocationData("BackroomBB",   756783_058),
    "Restrooms BB - Item 1":                                              FNaFB1LocationData("RestroomsBB",   756783_059),
    "Restrooms BB - Item 2":                                              FNaFB1LocationData("RestroomsBB",   756783_060),
    "Restrooms BB - Item 3":                                              FNaFB1LocationData("RestroomsBB",   756783_061),
    "Restrooms BB - Item 4":                                              FNaFB1LocationData("RestroomsBB",   756783_062),
    "Restrooms BB - Item 5":                                              FNaFB1LocationData("RestroomsBB",   756783_063),
    "Restrooms BB - Item 6":                                              FNaFB1LocationData("RestroomsBB",   756783_064),
    "Restrooms BB - Item 7":                                              FNaFB1LocationData("RestroomsBB",   756783_065),
    "Restrooms BB - Item 8":                                              FNaFB1LocationData("RestroomsBB",   756783_066),
    "Supply Closet BB - Item 1":                                          FNaFB1LocationData("SupplyClosetBB",   756783_067),
    "Supply Closet BB - Item 2":                                          FNaFB1LocationData("SupplyClosetBB",   756783_068),
    "Supply Closet BB - Item 3":                                          FNaFB1LocationData("SupplyClosetBB",   756783_069),
    "Supply Closet BB - Item 4":                                          FNaFB1LocationData("SupplyClosetBB",   756783_070),
    "Supply Closet BB - Item 5":                                          FNaFB1LocationData("SupplyClosetBB",   756783_071),
    "Supply Closet BB - Item 6":                                          FNaFB1LocationData("SupplyClosetBB",   756783_072),
    "Supply Closet BB - Item 7":                                          FNaFB1LocationData("SupplyClosetBB",   756783_073),
    "Supply Closet BB - Item 8":                                          FNaFB1LocationData("SupplyClosetBB",   756783_074),
    "Supply Closet BB - Item 9":                                          FNaFB1LocationData("SupplyClosetBB",   756783_075),
    "Supply Closet BB - Item 10":                                         FNaFB1LocationData("SupplyClosetBB",   756783_076),
    "East Hall Corner BB - Item 1":                                       FNaFB1LocationData("EastHallBB",   756783_077),
    "East Hall Corner BB - Item 2":                                       FNaFB1LocationData("EastHallBB",   756783_078),
    "East Hall Corner BB - Item 3":                                       FNaFB1LocationData("EastHallBB",   756783_079),
    "East Hall Corner BB - Item 4":                                       FNaFB1LocationData("EastHallBB",   756783_080),
    "East Hall Corner BB - Item 5":                                       FNaFB1LocationData("EastHallBB",   756783_081),
    "East Hall Corner BB - Item 6":                                       FNaFB1LocationData("EastHallBB",   756783_082),
    "East Hall Corner BB - Item 7":                                       FNaFB1LocationData("EastHallBB",   756783_083),
    "East Hall Corner BB - Item 8":                                       FNaFB1LocationData("EastHallBB",   756783_084),
    "East Hall Corner BB - Item 9":                                       FNaFB1LocationData("EastHallBB",   756783_085),
    "East Hall Corner BB - Item 10":                                      FNaFB1LocationData("EastHallBB",   756783_086),
    "East Hall Corner BB - Item 11":                                      FNaFB1LocationData("EastHallBB",   756783_087),
    "East Hall Corner BB - Item 12":                                      FNaFB1LocationData("EastHallBB",   756783_088),
    # Cameras
    "Show Stage - Camera":                                                FNaFB1LocationData("Cameras",   756783_089),
    "Dining Area - Camera":                                               FNaFB1LocationData("Cameras",   756783_090),
    "Backroom - Camera":                                                  FNaFB1LocationData("Cameras",   756783_091),
    "West Hall - Camera":                                                 FNaFB1LocationData("Cameras",   756783_092),
    "East Hall - Camera":                                                 FNaFB1LocationData("Cameras",   756783_093),
    "Restrooms - Camera":                                                 FNaFB1LocationData("Cameras",   756783_094),
    "Pirate Cove - Camera":                                               FNaFB1LocationData("Cameras",   756783_095),
    "Supply Closet - Camera":                                             FNaFB1LocationData("Cameras",   756783_096),
    "East Hall Corner - Camera":                                          FNaFB1LocationData("Cameras",   756783_097),
    "West Hall Corner - Camera":                                          FNaFB1LocationData("Cameras",   756783_098),
    # Party Hats
    "Backroom - Alpha Party Hat":                                         FNaFB1LocationData("PartyHats",    756783_099),
    "Restrooms - Beta Party Hat":                                         FNaFB1LocationData("PartyHats",    756783_100),
    "Supply Closet - Gamma Party Hat":                                    FNaFB1LocationData("PartyHats",    756783_101),
    "East Hall Corner - Omega Party Hat":                                 FNaFB1LocationData("PartyHats",    756783_102),
    # Whoops I forgot this one
    "Kitchen - Chica":                                                    FNaFB1LocationData("General",      756783_103),
    # Levels
    **{f"Freddy - Level {i+1}":                                           FNaFB1LocationData("Levelsanity",  756783_110 + i) for i in range(0, 20)},
    **{f"Bonnie - Level {i+1}":                                           FNaFB1LocationData("Levelsanity",  756783_140 + i) for i in range(0, 20)},
    **{f"Chica - Level {i+1}":                                            FNaFB1LocationData("Levelsanity",  756783_170 + i) for i in range(0, 20)},
    **{f"Foxy - Level {i+1}":                                             FNaFB1LocationData("Levelsanity",  756783_200 + i) for i in range(0, 20)},
    # Randomizer DLC
    "Backroom - Scrungip":                                                FNaFB1LocationData("Scrungip",     756783_250),
    "Dining Area - Scrungip":                                             FNaFB1LocationData("Scrungip",     756783_251),
    "Hidden Room - Scrungip":                                             FNaFB1LocationData("Scrungip",     756783_252),
    "Pirate Cove - Scrungip":                                             FNaFB1LocationData("Scrungip",     756783_253),
    "West Hall Corner - Scrungip":                                        FNaFB1LocationData("Scrungip",     756783_254),
    "Backroom - The Mirror":                                              FNaFB1LocationData("Scrungip",     756783_255),
    "Show Stage - Puppetmaster BB":                                       FNaFB1LocationData("Puppetmaster", 756783_256),
    **{f"Scrungip - Level {i+1}":                                         FNaFB1LocationData("ScrungipLevelsanity",  756783_300 + i) for i in range(0, 20)},

    # For parity with the final builds of the original game
    "Dining Area - Chest":                                                FNaFB1LocationData("General",      780000_001),
    "Pirate Cove - Chest":                                                FNaFB1LocationData("General",      780000_002),
    "West Hall - Chest":                                                  FNaFB1LocationData("General",      780000_003),
    "East Hall Corner - Chest":                                           FNaFB1LocationData("General",      780000_004),
    "Backroom - Chest":                                                   FNaFB1LocationData("General",      780000_005),
    "Dining Area - Dragon Dildo Ritual":                                  FNaFB1LocationData("General",      780000_006)
}
