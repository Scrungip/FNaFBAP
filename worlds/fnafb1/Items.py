from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification


class FNaFB1Item(Item):
    game: str = "Five Nights at Fuckboy's"


class FNaFB1ItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1


def get_items_by_category(category: str) -> Dict[str, FNaFB1ItemData]:
    item_dict: Dict[str, FNaFB1ItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)
    for name, data in other_game_item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict


item_table: Dict[str, FNaFB1ItemData] = {
    # Party Members
    "Freddy":                           FNaFB1ItemData("Party",            756782_999, ItemClassification.progression),
    "Bonnie":                           FNaFB1ItemData("Party",            756783_000, ItemClassification.progression),
    "Chica":                            FNaFB1ItemData("Party",            756783_001, ItemClassification.progression),
    "Foxy":                             FNaFB1ItemData("Party",            756783_002, ItemClassification.progression),

    # Weapons
    "Progressive Microphone":           FNaFB1ItemData("FreddyWeapons",    756783_003, ItemClassification.progression,                          6),
    "Progressive Guitar":               FNaFB1ItemData("BonnieWeapons",    756783_004, ItemClassification.progression,                          6),
    "Progressive Cupcakes":             FNaFB1ItemData("ChicaWeapons",     756783_005, ItemClassification.progression,                          6),
    "Progressive Hook":                 FNaFB1ItemData("FoxyWeapons",      756783_006, ItemClassification.progression,                          6),
    "Progressive Dragon Dildo":         FNaFB1ItemData("Dildo",            756783_007, ItemClassification.progression,                          2),

    # Skills
    "Tophat Toss":                      FNaFB1ItemData("FreddySkills",     756783_008, ItemClassification.progression),
    "Lead Stinger":                     FNaFB1ItemData("FreddySkills",     756783_009, ItemClassification.progression),
    "Toreador March":                   FNaFB1ItemData("FreddySkills",     756783_010, ItemClassification.progression),
    "Bunny Hop":                        FNaFB1ItemData("BonnieSkills",     756783_011, ItemClassification.progression),
    "Backup Bash":                      FNaFB1ItemData("BonnieSkills",     756783_012, ItemClassification.progression),
    "Guitar Riff":                      FNaFB1ItemData("BonnieSkills",     756783_013, ItemClassification.useful),
    "Fearless Flight":                  FNaFB1ItemData("ChicaSkills",      756783_014, ItemClassification.progression),
    "Pizza Pass":                       FNaFB1ItemData("ChicaSkills",      756783_015, ItemClassification.useful),
    "Caffeine Revival":                 FNaFB1ItemData("ChicaSkills",      756783_016, ItemClassification.useful),
    "Plank Walk":                       FNaFB1ItemData("FoxySkills",       756783_017, ItemClassification.progression),
    "Speed Share":                      FNaFB1ItemData("FoxySkills",       756783_018, ItemClassification.useful),
    "Rushdown":                         FNaFB1ItemData("FoxySkills",       756783_019, ItemClassification.progression),
    "Fazbear Combo":                    FNaFB1ItemData("FreddySkills",     756783_020, ItemClassification.useful),
    "Flighty Combo":                    FNaFB1ItemData("ChicaSkills",      756783_021, ItemClassification.useful),
    "Bonbon Combo":                     FNaFB1ItemData("BonnieSkills",     756783_022, ItemClassification.useful),
    "Pirate Combo":                     FNaFB1ItemData("FoxySkills",       756783_023, ItemClassification.useful),

    # Armor/Defense
    "Progressive Body Endoskeletons":   FNaFB1ItemData("Armor",            756783_024, ItemClassification.progression,                          4),
    "Progressive Head Endoskeletons":   FNaFB1ItemData("Armor",            756783_025, ItemClassification.progression,                          4),
    "Progressive Pizza Shields":        FNaFB1ItemData("Armor",            756783_026, ItemClassification.progression,                          4),
    "Progressive Caffeine Sodas":       FNaFB1ItemData("Armor",            756783_027, ItemClassification.progression,                          4),
    "Lucky Soda":                       FNaFB1ItemData("ExtraArmor",       756783_028, ItemClassification.useful),
    "Double Pizza":                     FNaFB1ItemData("ExtraArmor",       756783_029, ItemClassification.useful),
    "Ice Water":                        FNaFB1ItemData("ExtraArmor",       756783_030, ItemClassification.useful),
    "Sneaky Juice":                     FNaFB1ItemData("ExtraArmor",       756783_031, ItemClassification.useful),
    "Stealth Preserve":                 FNaFB1ItemData("ExtraArmor",       756783_032, ItemClassification.useful),
    "Heist Cream":                      FNaFB1ItemData("ExtraArmor",       756783_033, ItemClassification.useful),
    "Lunate Wine":                      FNaFB1ItemData("ExtraArmor",       756783_034, ItemClassification.useful),
    "Thrifty Pretzels":                 FNaFB1ItemData("ExtraArmor",       756783_035, ItemClassification.useful),

    # Progression
    "Lighter":                          FNaFB1ItemData("Quest",            756783_036, ItemClassification.progression),
    "Bonnie's Head Voucher":            FNaFB1ItemData("Quest",            756783_037, ItemClassification.progression),
    "Bonnie's Head":                    FNaFB1ItemData("Quest",            756783_038, ItemClassification.progression),
    "Kitchen Key":                      FNaFB1ItemData("Quest",            756783_039, ItemClassification.progression),
    "Reveal Interior Walls":            FNaFB1ItemData("Quest",            756783_040, ItemClassification.progression),
    "Office Key Piece":                 FNaFB1ItemData("Quest",            756783_041, ItemClassification.progression_skip_balancing,           4),
    "Backroom BB":                      FNaFB1ItemData("Quest",            756783_042, ItemClassification.progression),
    "Restrooms BB":                     FNaFB1ItemData("Quest",            756783_043, ItemClassification.progression),
    "Supply Closet BB":                 FNaFB1ItemData("Quest",            756783_044, ItemClassification.progression),
    "East Hall Corner BB":              FNaFB1ItemData("Quest",            756783_045, ItemClassification.progression),

    # Junk
    "Small Pizza":                      FNaFB1ItemData("Filler",           756783_046, weight=2),
    "Medium Pizza":                     FNaFB1ItemData("Filler",           756783_047, weight=4),
    "Large Pizza":                      FNaFB1ItemData("Filler",           756783_048, weight=3),
    "Small Soda":                       FNaFB1ItemData("Filler",           756783_049, weight=2),
    "Medium Soda":                      FNaFB1ItemData("Filler",           756783_050, weight=4),
    "Large Soda":                       FNaFB1ItemData("Filler",           756783_051, weight=3),
    "Pizza Slice":                      FNaFB1ItemData("Filler",           756783_052, weight=1),
    "Cake":                             FNaFB1ItemData("Filler",           756783_053, weight=2),
    "Birthday Present":                 FNaFB1ItemData("Filler",           756783_054, weight=1),
    "X-Large Pizza":                    FNaFB1ItemData("Filler",           756783_055, weight=2),
    "X-Large Soda":                     FNaFB1ItemData("Filler",           756783_056, weight=2),
    "HP Boost":                         FNaFB1ItemData("Filler",           756783_057, weight=1),
    "MP Boost":                         FNaFB1ItemData("Filler",           756783_058, weight=1),
    "Attack Boost":                     FNaFB1ItemData("Filler",           756783_059, weight=1),
    "Defense Boost":                    FNaFB1ItemData("Filler",           756783_060, weight=1),
    "Bonus Interior Walls Key":         FNaFB1ItemData("Filler",           756783_061, weight=1),
    "100 Tokens":                       FNaFB1ItemData("Filler",           756783_062, weight=3),
    "500 Tokens":                       FNaFB1ItemData("Filler",           756783_063, weight=2),

    # Randomizer DLC
    "Puppet's Strings":                 FNaFB1ItemData("DLC",              756783_064, ItemClassification.progression),
    "Funky Scrungip Token":             FNaFB1ItemData("DLC",              756783_065, ItemClassification.progression)
}

other_game_item_table: Dict[str, FNaFB1ItemData] = {
    "1-Up Mushroom":                    FNaFB1ItemData("SuperMario",       780000_001),
    "Hylian Shield":                    FNaFB1ItemData("3DZelda",          780000_002, ItemClassification.useful),
    "Chaos Emerald":                    FNaFB1ItemData("Sonic",            780000_003, ItemClassification.useful),
    "Dreamer's Crown":                  FNaFB1ItemData("Junko",            780000_004, ItemClassification.useful),
    "Blade":                            FNaFB1ItemData("CaveStory",        780000_005, ItemClassification.useful),
    "The Big Red Button":               FNaFB1ItemData("Clique",           780000_006, ItemClassification.useful),
    "Varia Suit":                       FNaFB1ItemData("Metroid",          780000_007, ItemClassification.useful),
    "Warp Star":                        FNaFB1ItemData("Kirby",            780000_008, ItemClassification.useful),
    "Dream Nail":                       FNaFB1ItemData("HollowKnight",     780000_009, ItemClassification.useful),
    "Moon Pearl":                       FNaFB1ItemData("LttP",             780000_010, ItemClassification.useful),
    "Mega Buster":                      FNaFB1ItemData("MegaMan",          780000_011, ItemClassification.useful),
    "Roc's Feather":                    FNaFB1ItemData("LADX",             780000_012, ItemClassification.useful),
    "Lawbot Disguise":                  FNaFB1ItemData("Toontown",         780000_013, ItemClassification.useful),
    "Hookshot Badge":                   FNaFB1ItemData("HatInTime",        780000_014, ItemClassification.useful),
    "Reflect Element":                  FNaFB1ItemData("KingdomHearts",    780000_015, ItemClassification.useful),
    "HM04 Strength":                    FNaFB1ItemData("Pokemon",          780000_016, ItemClassification.useful),
    "Toy Freddy":                       FNaFB1ItemData("Fuckboys2",        780000_017, ItemClassification.useful),
    "1 Puzzle Piece":                   FNaFB1ItemData("Jigsaw",           780000_018, ItemClassification.useful),
    "P":                                FNaFB1ItemData("LiesOfP",          780000_019, ItemClassification.useful),
    "Star Fox Credits Theme":           FNaFB1ItemData("SMZ3",             780000_020, ItemClassification.trap),
    "Scooby Snack":                     FNaFB1ItemData("Scooby",           780000_021),
    "Anime catboy transformation potion": FNaFB1ItemData("Undertale2",     780000_022, ItemClassification.trap),
    "Lava Badge":                       FNaFB1ItemData("SM64Romhack",      780000_023),
    "The Fog is Coming":                FNaFB1ItemData("PvZF",             780000_024)
}

full_table: Dict[str, FNaFB1ItemData] = {
    **item_table,
    **other_game_item_table
}