from typing import Dict, NamedTuple, Optional

from BaseClasses import Location


class FNaFB2Location(Location):
    game: str = "Five Nights at Fuckboy's 2"


class FNaFB2LocationData(NamedTuple):
    category: str
    code: Optional[int] = None


def get_locations_by_category(category: str) -> Dict[str, FNaFB2LocationData]:
    location_dict: Dict[str, FNaFB2LocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict


location_table: Dict[str, FNaFB2LocationData] = {
    # General Checks
    "Show Stage - Left Chest":                                            FNaFB2LocationData("General",     766783_000),
    "Show Stage - Right Chest":                                           FNaFB2LocationData("General",     766783_001),
    "Show Stage - Lucky Soda Chest":                                      FNaFB2LocationData("General",     766783_002),
    "Show Stage - Double Pizza Chest":                                    FNaFB2LocationData("General",     766783_003),
    "Game Room - Punch the fuck out of the carousel":                     FNaFB2LocationData("General",     766783_004),
    "Kid's Cove - Chest 1":                                               FNaFB2LocationData("General",     766783_005),
    "Kid's Cove - Chest 2":                                               FNaFB2LocationData("General",     766783_006),
    "Men's Bathroom - Chest":                                             FNaFB2LocationData("General",     766783_007),
    "B.B. - Foam Cupcakes A":                                             FNaFB2LocationData("General",     766783_008),
    "Women's Bathroom - Toy Chica":                                       FNaFB2LocationData("General",     766783_009),
    "Right Vent - Toy Bonnie":                                            FNaFB2LocationData("General",     766783_010),
    **{f"Cave of the Past - Dragon Dildo {chr(i + 65)}":                  FNaFB2LocationData("General",     766783_011 + i) for i in range(6)},
    "B.B. Giygas - Left Chest 1":                                         FNaFB2LocationData("General",     766783_017),
    "B.B. Giygas - Left Chest 2":                                         FNaFB2LocationData("General",     766783_018),
    "B.B. Giygas - Left Chest 3":                                         FNaFB2LocationData("General",     766783_019),
    "B.B. Giygas - Left Chest 4":                                         FNaFB2LocationData("General",     766783_020),
    "B.B. Giygas - Left Chest 5":                                         FNaFB2LocationData("General",     766783_021),
    "B.B. Giygas - Right Chest 1":                                        FNaFB2LocationData("General",     766783_022),
    "B.B. Giygas - Right Chest 2":                                        FNaFB2LocationData("General",     766783_023),
    "B.B. Giygas - Right Chest 3":                                        FNaFB2LocationData("General",     766783_024),
    # Quests
    "Turn in Sex Toy Voucher to B.B.":                                    FNaFB2LocationData("Quests",      766783_025),
    "Kid's Cove - Return Sex Toy":                                        FNaFB2LocationData("Quests",      766783_026),
    "Vending Machine - Turn in Sex Toy Voucher":                          FNaFB2LocationData("Quests",      766783_027),
    # Trade-Ins
    "Dining Area - Trade Alpha Voucher":                                  FNaFB2LocationData("Trade",       766783_028),
    "Dining Area - Trade Beta Voucher":                                   FNaFB2LocationData("Trade",       766783_029),
    "Dining Area - Trade Gamma Voucher":                                  FNaFB2LocationData("Trade",       766783_030),
    "Dining Area - Trade Delta Voucher":                                  FNaFB2LocationData("Trade",       766783_031),
    "Dining Area - Trade Omega Voucher":                                  FNaFB2LocationData("Trade",       766783_032),
    #Cassettes
    "Show Stage - Cassette Radar Chest":                                  FNaFB2LocationData("Cassette",    766783_033),
    "Kid's Cove - Cassette":                                              FNaFB2LocationData("Cassette",    766783_034),
    "Parts/Service - Cassette":                                           FNaFB2LocationData("Cassette",    766783_035),
    "Men's Bathroom - Cassette":                                          FNaFB2LocationData("Cassette",    766783_036),
    "Women's Bathroom - Cassette":                                        FNaFB2LocationData("Cassette",    766783_037),
    "Office - Cassette":                                                  FNaFB2LocationData("Cassette",    766783_038),
    "Office Hall - Cassette":                                             FNaFB2LocationData("Cassette",    766783_039),
    "Party Room 1 - Cassette":                                            FNaFB2LocationData("Cassette",    766783_040),
    "Party Room 2 - Cassette":                                            FNaFB2LocationData("Cassette",    766783_041),
    "Party Room 3 - Cassette":                                            FNaFB2LocationData("Cassette",    766783_042),
    "Party Room 4 - Cassette":                                            FNaFB2LocationData("Cassette",    766783_043),
    #Keystones
    "Kid's Cove - Chest":                                                 FNaFB2LocationData("Keystones",   766783_044),
    "Women's Bathroom - Chest":                                           FNaFB2LocationData("Keystones",   766783_045),
    "Office - Left Chest":                                                FNaFB2LocationData("Keystones",   766783_046),
    "Office - Right Chest":                                               FNaFB2LocationData("Keystones",   766783_047),
    # Bosses
    "Party Room 4 - Withered Foxy":                                       FNaFB2LocationData("Boss",        766783_048),
    "Women's Bathroom - Splash Woman":                                    FNaFB2LocationData("Boss",        766783_049),
    "The Puppet":                                                         FNaFB2LocationData("Boss",        766783_050),
    "The Puppet - Rod of Femininity A":                                   FNaFB2LocationData("Boss",        766783_051),
    "Party Room 1 - Withered Bonnie":                                     FNaFB2LocationData("Boss",        766783_051),
    "Party Room 2 - Withered Chica":                                      FNaFB2LocationData("Boss",        766783_052),
    "Party Room 3 - Withered Freddy":                                     FNaFB2LocationData("Boss",        766783_053),
    "Party Room 4 - Withered Foxy Rematch":                               FNaFB2LocationData("Boss",        766783_054),
    "The Second Puppet":                                                  FNaFB2LocationData("Boss",        766783_055),
    "The Second Puppet - Rod of Femininity B":                            FNaFB2LocationData("Boss",        766783_056),
    "Women's Bathroom - Shadow Bonnie":                                   FNaFB2LocationData("Boss",        766783_057),
    "Office - Rap God":                                                   FNaFB2LocationData("Cassette",    766783_058),
    "Boss Rush":                                                          FNaFB2LocationData("Boss",        766783_059),
    "B.B.'s Lair - B.B.":                                                 FNaFB2LocationData("Boss",        766783_060),
    "B.B. Giygas":                                                        FNaFB2LocationData("Boss",        766783_061),
    "Refurbs":                                                            FNaFB2LocationData("Refurbs",     766783_062),
    # Shops
    **{f"Main Hall B.B. - Item {i + 1}":                                  FNaFB2LocationData("MainHallBB",  766783_063 + i) for i in range(6)},
    **{f"Party Room 3 B.B. - Item {i + 1}":                               FNaFB2LocationData("PartyRoomBB", 766783_069 + i) for i in range(8)},
    **{f"Kid's Cove B.B. - Item {i + 1}":                                 FNaFB2LocationData("KidsCoveBB",  766783_077 + i) for i in range(10)},
    **{f"Office B.B. - Item {i + 1}":                                     FNaFB2LocationData("OfficeBB",    766783_088 + i) for i in range(12)},
    # Cameras
    "Show Stage - Camera":                                                FNaFB2LocationData("Cameras",     766783_100),
    "Game Room - Camera":                                                 FNaFB2LocationData("Cameras",     766783_101),
    "Prize Corner - Camera":                                              FNaFB2LocationData("Cameras",     766783_102),
    "Main Hall - Camera":                                                 FNaFB2LocationData("Cameras",     766782_103),
    "Kid's Cove - Camera":                                                FNaFB2LocationData("Cameras",     766783_104),
    "Parts/Service - Camera":                                             FNaFB2LocationData("Cameras",     766783_105),
    "Office - Camera":                                                    FNaFB2LocationData("Cameras",     766783_106),
    "Left Vent - Camera":                                                 FNaFB2LocationData("Cameras",     766783_107),
    "Right Vent - Camera":                                                FNaFB2LocationData("Cameras",     766783_108),
    "Party Room 1 - Camera":                                              FNaFB2LocationData("Cameras",     766783_109),
    "Party Room 2 - Camera":                                              FNaFB2LocationData("Cameras",     766783_110),
    "Party Room 3 - Camera":                                              FNaFB2LocationData("Cameras",     766783_111),
    "Party Room 4 - Camera":                                              FNaFB2LocationData("Cameras",     766783_112),
    # Protection Hats
    "Kid's Cove - Protection Hat":                                        FNaFB2LocationData("PartyHats",   766783_113),
    "Main Hall - Protection Hat":                                         FNaFB2LocationData("PartyHats",   766783_114),
    "Office - Protection Hat":                                            FNaFB2LocationData("PartyHats",   766783_115),
    "Party Room 3 - Protection Hat":                                      FNaFB2LocationData("PartyHats",   766783_116),
    # Levels
    **{f"Toy Freddy - Level {i + 1}":                                     FNaFB2LocationData("Levelsanity", 766783_117 + i) for i in range(20)},
    **{f"Toy Bonnie - Level {i + 1}":                                     FNaFB2LocationData("Levelsanity", 766783_137 + i) for i in range(20)},
    **{f"Toy Chica - Level {i + 1}":                                      FNaFB2LocationData("Levelsanity", 766783_157 + i) for i in range(20)},
    **{f"Mangle - Level {i + 1}":                                         FNaFB2LocationData("Levelsanity", 766783_177 + i) for i in range(20)}, 
    # Abilities
    "Toy Freddy - Tophat Slash":                                          FNaFB2LocationData("Levelsanity", 766783_197),
    "Toy Freddy - Tophat Dash":                                           FNaFB2LocationData("Levelsanity", 766783_198),
    "Toy Freddy - Tophat Crash":                                          FNaFB2LocationData("Levelsanity", 766783_199),
    "Toy Freddy - Tophat Smash":                                          FNaFB2LocationData("Levelsanity", 766783_200),
    "Toy Freddy - Use Tophat Slash 20 times":                             FNaFB2LocationData("Levelsanity", 766783_201),
    "Toy Freddy - Use Tophat Slash 40 times":                             FNaFB2LocationData("Levelsanity", 766783_202),
    "Toy Freddy - Use Tophat Dash 20 times":                              FNaFB2LocationData("Levelsanity", 766783_203),
    "Toy Freddy - Use Tophat Dash 40 times":                              FNaFB2LocationData("Levelsanity", 766783_204),
    "Toy Freddy - Use Tophat Crash 20 times":                             FNaFB2LocationData("Levelsanity", 766783_205),
    "Toy Freddy - Use Tophat Crash 40 times":                             FNaFB2LocationData("Levelsanity", 766783_206),
    "Toy Freddy - Use Tophat Smash 20 times":                             FNaFB2LocationData("Levelsanity", 766783_207),
    "Toy Freddy - Use Tophat Smash 40 times":                             FNaFB2LocationData("Levelsanity", 766783_208),
    "Mangle - Electroshock":                                              FNaFB2LocationData("Levelsanity", 766783_209),
    "Mangle - Paravolt":                                                  FNaFB2LocationData("Levelsanity", 766783_210),
    "Mangle - Somnojolt":                                                 FNaFB2LocationData("Levelsanity", 766783_211),
    "Mangle - Lightningbolt":                                             FNaFB2LocationData("Levelsanity", 766783_212),
    "Toy Chica - Healing Wing":                                           FNaFB2LocationData("Levelsanity", 766783_213),
    "Toy Chica - Curing Wing":                                            FNaFB2LocationData("Levelsanity", 766783_214),
    "Toy Chica - Raising Wing":                                           FNaFB2LocationData("Levelsanity", 766783_215),
    "Toy Chica - Recovery Wing":                                          FNaFB2LocationData("Levelsanity", 766783_216),
    "Toy Bonnie - Grab Bag":                                              FNaFB2LocationData("Levelsanity", 766783_217),
    "Toy Bonnie - Status Bomb":                                           FNaFB2LocationData("Levelsanity", 766783_218),
    "Toy Bonnie - Spread Bomb":                                           FNaFB2LocationData("Levelsanity", 766783_219),
    "Toy Bonnie - Timer Flip":                                            FNaFB2LocationData("Levelsanity", 766783_220),
    "Toy Freddy - Death Inhale":                                          FNaFB2LocationData("Levelsanity", 766783_221),
    "Toy Bonnie - Terror Fever":                                          FNaFB2LocationData("Levelsanity", 766783_222),
    "Toy Chica - Avian Strike":                                           FNaFB2LocationData("Levelsanity", 766783_223),
    "Mangle - Disassembly":                                               FNaFB2LocationData("Levelsanity", 766783_224),
    # Arcade Minigames
    "Foxy's Steppin' Cove":                                               FNaFB2LocationData("Arcade",      766783_225),
    "Puppet Man Dating Sim":                                              FNaFB2LocationData("Arcade",      766783_226),
    "SEND CAKE TO CHILD":                                                 FNaFB2LocationData("Arcade",      766783_227),
    # Gems for critical mode
    "Kid's Cove - Tophat Slash Gem":                                      FNaFB2LocationData("Gem",         766783_228),
    "Kid's Cove - Status Bomb Gem":                                       FNaFB2LocationData("Gem",         766783_229),
    "Men's Bathroom - Paravolt Gem":                                      FNaFB2LocationData("Gem",         766783_230),
    "Men's Bathroom - Tophat Dash Gem":                                   FNaFB2LocationData("Gem",         766783_231),
    "Women's Bathroom - Grab Bag Gem":                                    FNaFB2LocationData("Gem",         766783_232),
    "Women's Bathroom - Somnojolt Gem":                                   FNaFB2LocationData("Gem",         766783_233),
    "Office - Electroshock Gem":                                          FNaFB2LocationData("Gem",         766783_234),
    "Office - Recovery Wing Gem":                                         FNaFB2LocationData("Gem",         766783_235),
    "Office - Spread Bomb Gem":                                           FNaFB2LocationData("Gem",         766783_236),
    "Office - Tophat Crash Gem":                                          FNaFB2LocationData("Gem",         766783_237),
    "Party Room 1 - Timer Flip Gem":                                      FNaFB2LocationData("Gem",         766783_238),
    "Party Room 2 - Healing Wing Gem":                                    FNaFB2LocationData("Gem",         766783_239),
    "Party Room 3 - Curing Wing Gem":                                     FNaFB2LocationData("Gem",         766783_240),
    "Party Room 4 - Raising Wing Gem":                                    FNaFB2LocationData("Gem",         766783_241),
    "Party Room 4 - Tophat Smash Gem":                                    FNaFB2LocationData("Gem",         766783_242),
    "Party Room 4 - Lightningbolt Gem":                                   FNaFB2LocationData("Gem",         766783_243)
}
