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
    "Men's Bathroom - Chest":                                             FNaFB2LocationData("General",     766783_005),
    "Women's Bathroom - Toy Chica":                                       FNaFB2LocationData("General",     766783_006),
    "Right Vent - Toy Bonnie":                                            FNaFB2LocationData("General",     766783_007),
    **{f"Cave of the Past - Dragon Dildo {chr(i + 65)}":                  FNaFB2LocationData("General",     766783_008 + i) for i in range(6)},
    "BB Giygas - Left Chest 1":                                           FNaFB2LocationData("General",     766783_014),
    "BB Giygas - Left Chest 2":                                           FNaFB2LocationData("General",     766783_015),
    "BB Giygas - Left Chest 3":                                           FNaFB2LocationData("General",     766783_016),
    "BB Giygas - Left Chest 4":                                           FNaFB2LocationData("General",     766783_017),
    "BB Giygas - Left Chest 5":                                           FNaFB2LocationData("General",     766783_018),
    "BB Giygas - Right Chest 1":                                          FNaFB2LocationData("General",     766783_019),
    "BB Giygas - Right Chest 2":                                          FNaFB2LocationData("General",     766783_020),
    "BB Giygas - Right Chest 3":                                          FNaFB2LocationData("General",     766783_021),
    # Quests
    "Turn in Sex Toy Voucher to BB":                                      FNaFB2LocationData("Quests",      766783_022),
    "Kid's Cove - Return Sex Toy":                                        FNaFB2LocationData("Quests",      766783_023),
    "Vending Machine - Turn in Sex Toy Voucher":                          FNaFB2LocationData("Quests",      766783_024),
    # Trade-Ins
    "Dining Area - Trade Alpha Voucher":                                  FNaFB2LocationData("Trade",       766783_025),
    "Dining Area - Trade Beta Voucher":                                   FNaFB2LocationData("Trade",       766783_026),
    "Dining Area - Trade Gamma Voucher":                                  FNaFB2LocationData("Trade",       766783_027),
    "Dining Area - Trade Delta Voucher":                                  FNaFB2LocationData("Trade",       766783_028),
    "Dining Area - Trade Omega Voucher":                                  FNaFB2LocationData("Trade",       766783_029),
    #Cassettes
    "Show Stage - Cassette Radar Chest":                                  FNaFB2LocationData("Cassette",    766783_030),
    "Kid's Cove - Cassette":                                              FNaFB2LocationData("Cassette",    766783_031),
    "Parts/Service - Cassette":                                           FNaFB2LocationData("Cassette",    766783_032),
    "Men's Bathroom - Cassette":                                          FNaFB2LocationData("Cassette",    766783_033),
    "Women's Bathroom - Cassette":                                        FNaFB2LocationData("Cassette",    766783_034),
    "Office - Cassette":                                                  FNaFB2LocationData("Cassette",    766783_035),
    "Office Hall - Cassette":                                             FNaFB2LocationData("Cassette",    766783_036),
    "Party Room 1 - Cassette":                                            FNaFB2LocationData("Cassette",    766783_037),
    "Party Room 2 - Cassette":                                            FNaFB2LocationData("Cassette",    766783_038),
    "Party Room 3 - Cassette":                                            FNaFB2LocationData("Cassette",    766783_039),
    "Party Room 4 - Cassette":                                            FNaFB2LocationData("Cassette",    766783_040),
    #Keystones
    "Kid's Cove - Chest":                                                 FNaFB2LocationData("Keystones",   766783_041),
    "Women's Bathroom - Chest":                                           FNaFB2LocationData("Keystones",   766783_042),
    "Office - Left Chest":                                                FNaFB2LocationData("Keystones",   766783_043),
    "Office - Right Chest":                                               FNaFB2LocationData("Keystones",   766783_044),
    # Bosses
    "Party Room 4 - Withered Foxy":                                       FNaFB2LocationData("Boss",        766783_045),
    "Women's Bathroom - Splash Woman":                                    FNaFB2LocationData("Boss",        766783_046),
    "The Puppet":                                                         FNaFB2LocationData("Boss",        766783_047),
    "The Puppet - Rod of Femininity A":                                   FNaFB2LocationData("Boss",        766783_048),
    "Party Room 1 - Withered Bonnie":                                     FNaFB2LocationData("Boss",        766783_049),
    "Party Room 2 - Withered Chica":                                      FNaFB2LocationData("Boss",        766783_050),
    "Party Room 3 - Withered Freddy":                                     FNaFB2LocationData("Boss",        766783_051),
    "Party Room 4 - Withered Foxy Rematch":                               FNaFB2LocationData("Boss",        766783_052),
    "The Second Puppet":                                                  FNaFB2LocationData("Boss",        766783_053),
    "The Second Puppet - Rod of Femininity B":                            FNaFB2LocationData("Boss",        766783_054),
    "Office - Rap God":                                                   FNaFB2LocationData("Cassette",    766783_055),
    "Boss Rush":                                                          FNaFB2LocationData("Boss",        766783_056),
    "BB Giygas":                                                          FNaFB2LocationData("Boss",        766783_057),
    "Refurbs":                                                            FNaFB2LocationData("Refurbs",     766783_058),
    # Shops
    **{f"Main Hall BB - Item {i + 1}":                                    FNaFB2LocationData("MainHallBB",  766783_059 + i) for i in range(6)},
    **{f"Party Room 3 BB - Item {i + 1}":                                 FNaFB2LocationData("PartyRoomBB", 766783_065 + i) for i in range(8)},
    **{f"Kid's Cove BB - Item {i + 1}":                                   FNaFB2LocationData("KidsCoveBB",  766783_073 + i) for i in range(10)},
    **{f"Office BB - Item {i + 1}":                                       FNaFB2LocationData("OfficeBB",    766783_083 + i) for i in range(12)},
    # Cameras
    "Show Stage - Camera":                                                FNaFB2LocationData("Cameras",     766783_095),
    "Game Room - Camera":                                                 FNaFB2LocationData("Cameras",     766783_096),
    "Prize Corner - Camera":                                              FNaFB2LocationData("Cameras",     766783_097),
    "Kid's Cove - Camera":                                                FNaFB2LocationData("Cameras",     766783_098),
    "Parts/Service - Camera":                                             FNaFB2LocationData("Cameras",     766783_099),
    "Office - Camera":                                                    FNaFB2LocationData("Cameras",     766783_100),
    "Left Vent - Camera":                                                 FNaFB2LocationData("Cameras",     766783_101),
    "Right Vent - Camera":                                                FNaFB2LocationData("Cameras",     766783_102),
    "Party Room 1 - Camera":                                              FNaFB2LocationData("Cameras",     766783_103),
    "Party Room 2 - Camera":                                              FNaFB2LocationData("Cameras",     766783_104),
    "Party Room 3 - Camera":                                              FNaFB2LocationData("Cameras",     766783_105),
    "Party Room 4 - Camera":                                              FNaFB2LocationData("Cameras",     766783_106),
    # Protection Hats
    "Kid's Cove - Protection Hat":                                        FNaFB2LocationData("PartyHats",   766783_107),
    "Main Hall - Protection Hat":                                         FNaFB2LocationData("PartyHats",   766783_108),
    "Office - Protection Hat":                                            FNaFB2LocationData("PartyHats",   766783_109),
    "Party Room 3 - Protection Hat":                                      FNaFB2LocationData("PartyHats",   766783_110),
    # Levels
    **{f"Toy Freddy - Level {i + 1}":                                     FNaFB2LocationData("Levelsanity", 766783_111 + i) for i in range(20)},
    **{f"Toy Bonnie - Level {i + 1}":                                     FNaFB2LocationData("Levelsanity", 766783_131 + i) for i in range(20)},
    **{f"Toy Chica - Level {i + 1}":                                      FNaFB2LocationData("Levelsanity", 766783_151 + i) for i in range(20)},
    **{f"Mangle - Level {i + 1}":                                         FNaFB2LocationData("Levelsanity", 766783_171 + i) for i in range(20)}, 
    # Abilities
    "Toy Freddy - Tophat Slash LV1":                                      FNaFB2LocationData("Levelsanity", 766783_191),
    "Toy Freddy - Tophat Slash LV2":                                      FNaFB2LocationData("Levelsanity", 766783_192),
    "Toy Freddy - Tophat Slash LVMAX":                                    FNaFB2LocationData("Levelsanity", 766783_193),
    "Toy Freddy - Tophat Dash LV1":                                       FNaFB2LocationData("Levelsanity", 766783_194),
    "Toy Freddy - Tophat Dash LV2":                                       FNaFB2LocationData("Levelsanity", 766783_195),
    "Toy Freddy - Tophat Dash LVMAX":                                     FNaFB2LocationData("Levelsanity", 766783_196),
    "Toy Freddy - Tophat Crash LV1":                                      FNaFB2LocationData("Levelsanity", 766783_197),
    "Toy Freddy - Tophat Crash LV2":                                      FNaFB2LocationData("Levelsanity", 766783_198),
    "Toy Freddy - Tophat Crash LVMAX":                                    FNaFB2LocationData("Levelsanity", 766783_199),
    "Toy Freddy - Tophat Smash LV1":                                      FNaFB2LocationData("Levelsanity", 766783_200),
    "Toy Freddy - Tophat Smash LV2":                                      FNaFB2LocationData("Levelsanity", 766783_201),
    "Toy Freddy - Tophat Smash LVMAX":                                    FNaFB2LocationData("Levelsanity", 766783_202),
    "Mangle - Electroshock":                                              FNaFB2LocationData("Levelsanity", 766783_203),
    "Mangle - Paravolt":                                                  FNaFB2LocationData("Levelsanity", 766783_204),
    "Mangle - Somnojolt":                                                 FNaFB2LocationData("Levelsanity", 766783_205),
    "Mangle - Lightningbolt":                                             FNaFB2LocationData("Levelsanity", 766783_206),
    "Toy Chica - Healing Wing":                                           FNaFB2LocationData("Levelsanity", 766783_207),
    "Toy Chica - Curing Wing":                                            FNaFB2LocationData("Levelsanity", 766783_208),
    "Toy Chica - Raising Wing":                                           FNaFB2LocationData("Levelsanity", 766783_209),
    "Toy Chica - Recovery Wing":                                          FNaFB2LocationData("Levelsanity", 766783_210),
    "Toy Bonnie - Grab Bag":                                              FNaFB2LocationData("Levelsanity", 766783_211),
    "Toy Bonnie - Status Bomb":                                           FNaFB2LocationData("Levelsanity", 766783_212),
    "Toy Bonnie - Spread Bomb":                                           FNaFB2LocationData("Levelsanity", 766783_213),
    "Toy Bonnie - Timer Flip":                                            FNaFB2LocationData("Levelsanity", 766783_214),
    "Toy Freddy - Death Inhale":                                          FNaFB2LocationData("Levelsanity", 766783_215),
    "Toy Bonnie - Terror Fever":                                          FNaFB2LocationData("Levelsanity", 766783_216),
    "Toy Chica - Avian Strike":                                           FNaFB2LocationData("Levelsanity", 766783_217),
    "Mangle - Disassembly":                                               FNaFB2LocationData("Levelsanity", 766783_218),
    # Arcade Minigames
    "Foxy's Steppin' Cove":                                               FNaFB2LocationData("Arcade",      766783_219),
    "Puppet Man Dating Sim":                                              FNaFB2LocationData("Arcade",      766783_220),
    "SEND CAKE TO CHILD":                                                 FNaFB2LocationData("Arcade",      766783_221),
    # Stuff added later and I'm too lazy to put them in the correct spot
    "Main Hall - Camera":                                                 FNaFB2LocationData("Cameras",     766782_222),
    "BB - Foam Cupcakes A":                                               FNaFB2LocationData("General",     766783_223),
    "BB's Lair - BB":                                                     FNaFB2LocationData("Boss",        766783_224),
    "Women's Bathroom - Shadow Bonnie":                                   FNaFB2LocationData("Boss",        766783_225),
    "Kid's Cove - Chest 1":                                               FNaFB2LocationData("General",     766783_226),
    "Kid's Cove - Chest 2":                                               FNaFB2LocationData("General",     766783_227),
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
