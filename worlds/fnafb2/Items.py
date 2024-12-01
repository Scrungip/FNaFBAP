from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification


class FNaFB2Item(Item):
    game: str = "Five Nights at Fuckboy's 2"


class FNaFB2ItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1


def get_items_by_category(category: str) -> Dict[str, FNaFB2ItemData]:
    item_dict: Dict[str, FNaFB2ItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict


item_table: Dict[str, FNaFB2ItemData] = {
    # Party Members
    "Toy Bonnie":                       FNaFB2ItemData("Party",                 766783_000, ItemClassification.progression),
    "Toy Chica":                        FNaFB2ItemData("Party",                 766783_001, ItemClassification.progression),
    "Mangle":                           FNaFB2ItemData("Party",                 766783_002, ItemClassification.progression),
    "Withered Freddy":                  FNaFB2ItemData("Party",                 766783_003, ItemClassification.progression),
    "Withered Bonnie":                  FNaFB2ItemData("Party",                 766783_004, ItemClassification.progression),
    "Withered Chica":                   FNaFB2ItemData("Party",                 766783_005, ItemClassification.progression),
    "Withered Foxy":                    FNaFB2ItemData("Party",                 766783_006, ItemClassification.progression),

    # Weapons
    "Progressive Microphone":           FNaFB2ItemData("TFreddyWeapons",        766783_007, ItemClassification.progression,                 6),
    "Progressive Guitar":               FNaFB2ItemData("TBonnieWeapons",        766783_008, ItemClassification.progression,                 6),
    # First progressive cupcake is to recruit Toy Chica
    "Progressive Cupcakes":             FNaFB2ItemData("TChicaWeapons",         766783_009, ItemClassification.progression,                 7),
    "Progressive Hook":                 FNaFB2ItemData("MangleWeapons",         766783_010, ItemClassification.progression,                 6),
    "Progressive Dragon Dildo":         FNaFB2ItemData("Useful",                766783_011, ItemClassification.progression,                 6),
    "Progressive Rod of Femininity":    FNaFB2ItemData("Useful",                766783_012, ItemClassification.useful,                      2),
    "Stick":                            FNaFB2ItemData("TFreddyWeapons",        766783_013, ItemClassification.progression),
    


    # Skills (Not including Bite of 87 because of how much it would break the game)
    "Progressive Tophat Slash":         FNaFB2ItemData("TFreddySkills",          766783_014, ItemClassification.progression,                3),
    "Progressive Tophat Dash":          FNaFB2ItemData("TFreddySkills",          766783_015, ItemClassification.progression,                3),
    "Progressive Tophat Crash":         FNaFB2ItemData("TFreddySkills",          766783_016, ItemClassification.progression,                3),
    "Progressive Tophat Smash":         FNaFB2ItemData("TFreddySkills",          766783_017, ItemClassification.progression,                3),
    "Electroshock":                     FNaFB2ItemData("MangleSkills",           766783_018, ItemClassification.progression),
    "Paravolt":                         FNaFB2ItemData("MangleSkills",           766783_019, ItemClassification.progression),
    "Somnojolt":                        FNaFB2ItemData("MangleSkills",           766783_020, ItemClassification.progression),
    "Lightningbolt":                    FNaFB2ItemData("MangleSkills",           766783_021, ItemClassification.progression),
    "Healing Wing":                     FNaFB2ItemData("TChicaSkills",           766783_022, ItemClassification.progression),
    "Curing Wing":                      FNaFB2ItemData("TChicaSkills",           766783_023, ItemClassification.progression),
    "Raising Wing":                     FNaFB2ItemData("TChicaSkills",           766783_024, ItemClassification.progression),
    "Recovery Wing":                    FNaFB2ItemData("TChicaSkills",           766783_025, ItemClassification.progression),
    "Grab Bag":                         FNaFB2ItemData("TBonnieSkills",          766783_026, ItemClassification.useful),
    "Status Bomb":                      FNaFB2ItemData("TBonnieSkills",          766783_027, ItemClassification.progression),
    "Spread Bomb":                      FNaFB2ItemData("TBonnieSkills",          766783_028, ItemClassification.progression),
    "Timer Flip":                       FNaFB2ItemData("TBonnieSkills",          766783_029, ItemClassification.filler),
    "Death Inhale":                     FNaFB2ItemData("TFreddySkills",          766783_030, ItemClassification.useful),
    "Terror Fever":                     FNaFB2ItemData("TBonnieSkills",          766783_031, ItemClassification.useful),
    "Avian Strike":                     FNaFB2ItemData("TChicaSkills",           766783_032, ItemClassification.useful),
    "Disassembly":                      FNaFB2ItemData("MangleSkills",           766783_033, ItemClassification.useful),
    
    # Armor/Defense
    "Progressive Body Endoskeletons":   FNaFB2ItemData("Armor",                  766783_034, ItemClassification.progression,                4),
    "Progressive Head Endoskeletons":   FNaFB2ItemData("Armor",                  766783_035, ItemClassification.progression,                4),
    "Progressive Pizza Shields":        FNaFB2ItemData("Armor",                  766783_036, ItemClassification.progression,                4),
    "Progressive Caffeine Sodas":       FNaFB2ItemData("Armor",                  766783_037, ItemClassification.progression,                4),
    "Lucky Soda":                       FNaFB2ItemData("Armor",                  766783_038, ItemClassification.useful),
    "Double Pizza":                     FNaFB2ItemData("Armor",                  766783_039, ItemClassification.useful),

    # Progression
    # One to turn into BB, one to turn into the vending machine
    "Sex Toy Voucher":                  FNaFB2ItemData("Quest",                  766783_040, ItemClassification.progression,                2),
    # First Sex Toy gets stolen so you need 2 to get Mangle 
    "Sex Toy":                          FNaFB2ItemData("Quest",                  766783_041, ItemClassification.progression,                2),
    "B.B.'s Essence":                   FNaFB2ItemData("Quest",                  766783_042, ItemClassification.progression_skip_balancing, 4),

    # Cassettes for proud mode
    "Cassette Radar":                   FNaFB2ItemData("Cassette",               766783_043, ItemClassification.progression),
    "Cassette":                         FNaFB2ItemData("Cassette",               766783_044, ItemClassification.progression,                10),

    # BB
    "Main Hall B.B.":                   FNaFB2ItemData("Quest",                  766783_045, ItemClassification.progression),
    "Party Room 3 B.B.":                FNaFB2ItemData("Quest",                  766783_046, ItemClassification.progression),
    "Kid's Cove B.B.":                  FNaFB2ItemData("Quest",                  766783_047, ItemClassification.progression),
    "Office B.B.":                      FNaFB2ItemData("Quest",                  766783_048, ItemClassification.progression),

    # Gems
    "Tophat Keystone":                  FNaFB2ItemData("Quest",                  766783_049, ItemClassification.progression),
    "Terror Keystone":                  FNaFB2ItemData("Quest",                  766783_050, ItemClassification.progression),
    "Avian Keystone":                   FNaFB2ItemData("Quest",                  766783_051, ItemClassification.progression),
    "Assembly Keystone":                FNaFB2ItemData("Quest",                  766783_052, ItemClassification.progression),

    # Junk
    "Small Pizza":                      FNaFB2ItemData("Filler",                 766783_053, weight=2),
    "Medium Pizza":                     FNaFB2ItemData("Filler",                 766783_054, weight=2),
    "Large Pizza":                      FNaFB2ItemData("Filler",                 766783_055, weight=2),
    "Small Soda":                       FNaFB2ItemData("Filler",                 766783_056, weight=2),
    "Medium Soda":                      FNaFB2ItemData("Filler",                 766783_057, weight=2),
    "Large Soda":                       FNaFB2ItemData("Filler",                 766783_058, weight=2),
    "Pizza Slice":                      FNaFB2ItemData("Filler",                 766783_059, weight=2),
    "Cake":                             FNaFB2ItemData("Filler",                 766783_060, weight=2),
    "Birthday Present":                 FNaFB2ItemData("Filler",                 766783_061, weight=2),
    "X-Large Pizza":                    FNaFB2ItemData("Filler",                 766783_062, weight=2),
    "X-Large Soda":                     FNaFB2ItemData("Filler",                 766783_063, weight=2),
    "Life Boost":                       FNaFB2ItemData("Filler",                 766783_064, weight=2),
    "Skill Boost":                      FNaFB2ItemData("Filler",                 766783_065, weight=2),
    "Attack Boost":                     FNaFB2ItemData("Filler",                 766783_066, weight=2),
    "Defense Boost":                    FNaFB2ItemData("Filler",                 766783_067, weight=2),
    "Donuts":                           FNaFB2ItemData("Filler",                 766783_068, weight=2)
}