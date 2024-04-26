from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification


class FNaFBItem(Item):
    game: str = "Five Nights at F***boy's"


class FNaFBItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1


def get_items_by_category(category: str) -> Dict[str, FNaFBItemData]:
    item_dict: Dict[str, FNaFBItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict


item_table: Dict[str, FNaFBItemData] = {
    # Party Members
    "Bonnie":                   FNaFBItemData("Party",      756783_000, ItemClassification.progression),
    "Chica":                    FNaFBItemData("Party",      756783_001, ItemClassification.progression),
    "Foxy":                     FNaFBItemData("Party",      756783_002, ItemClassification.progression),

    # Weapons
    "Progressive Microphone":   FNaFBItemData("FreddyWeapons",    756783_003, ItemClassification.progression,                 6),
    "Progressive Guitar":       FNaFBItemData("BonnieWeapons",    756783_004, ItemClassification.progression,                 6),
    "Progressive Cupcakes":     FNaFBItemData("ChicaWeapons",     756783_005, ItemClassification.progression,                 6),
    "Progressive Hook":         FNaFBItemData("FoxyWeapons",      756783_006, ItemClassification.progression,                 6),
    "Dragon Dildo":             FNaFBItemData("Useful",           756783_007, ItemClassification.useful, 1),

    # Skills
    "Tophat Toss":              FNaFBItemData("FreddySkills",     756783_008, ItemClassification.progression),
    "Lead Stinger":             FNaFBItemData("FreddySkills",     756783_009, ItemClassification.progression),
    "Toreador March":           FNaFBItemData("FreddySkills",     756783_010, ItemClassification.progression),
    "Bunny Hop":                FNaFBItemData("BonnieSkills",     756783_011, ItemClassification.progression),
    "Backup Bash":              FNaFBItemData("BonnieSkills",     756783_012, ItemClassification.progression),
    "Guitar Smash":             FNaFBItemData("BonnieSkills",     756783_013, ItemClassification.progression),
    "Fearless Flight":          FNaFBItemData("Useful",           756783_014, ItemClassification.useful, 1),
    "Pizza Pass":               FNaFBItemData("ChicaSkills",      756783_015, ItemClassification.progression),
    "Caffeine Revival":         FNaFBItemData("ChicaSkills",      756783_016, ItemClassification.progression),
    "Plank Walk":               FNaFBItemData("FoxySkills",       756783_017, ItemClassification.progression),
    "Speed Share":              FNaFBItemData("Useful",           756783_018, ItemClassification.useful, 1),
    "Rushdown":                 FNaFBItemData("FoxySkills",       756783_019, ItemClassification.progression),
    "Fazbear Combo":            FNaFBItemData("Useful",           756783_020, ItemClassification.useful, 1),
    "Flighty Combo":            FNaFBItemData("Useful",           756783_021, ItemClassification.useful, 1),
    "Bonbon Combo":             FNaFBItemData("Useful",           756783_022, ItemClassification.useful, 1),
    "Pirate Combo":             FNaFBItemData("Useful",           756783_023, ItemClassification.useful, 1),

    # Armor/Defense
    "Progressive Body Endoskeletons":   FNaFBItemData("Armor", 756783_024, ItemClassification.progression,                4),
    "Progressive Head Endoskeletons":   FNaFBItemData("Armor", 756783_025, ItemClassification.progression,                4),
    "Progressive Pizza Shields":        FNaFBItemData("Armor", 756783_026, ItemClassification.progression,                4),
    "Progressive Caffeine Sodas":       FNaFBItemData("Armor", 756783_027, ItemClassification.progression,                4),
    "Lucky Soda":                       FNaFBItemData("Useful", 756783_028, ItemClassification.useful, 1),
    "Double Pizza":                     FNaFBItemData("Useful", 756783_029, ItemClassification.useful, 1),
    "Ice Water":                        FNaFBItemData("Useful", 756783_030, ItemClassification.useful, 1),
    "Sneaky Juice":                     FNaFBItemData("Useful", 756783_031, ItemClassification.useful, 1),
    "Stealth Preserve":                 FNaFBItemData("Useful", 756783_032, ItemClassification.useful, 1),
    "Heist Cream":                      FNaFBItemData("Useful", 756783_033, ItemClassification.useful, 1),
    "Lunate Wine":                      FNaFBItemData("Useful", 756783_034, ItemClassification.useful, 1),
    "Thrifty Pretzels":                 FNaFBItemData("Useful", 756783_035, ItemClassification.useful, 1),

    # Progression
    "Lighter":                          FNaFBItemData("Quest",      756783_036, ItemClassification.progression),
    "Bonnie's Head Voucher":            FNaFBItemData("Quest",      756783_037, ItemClassification.progression),
    "Bonnie's Head":                    FNaFBItemData("Quest",      756783_038, ItemClassification.progression),
    "Kitchen Key":                      FNaFBItemData("Quest",      756783_039, ItemClassification.progression),
    "Reveal Interior Walls":            FNaFBItemData("Quest",      756783_040, ItemClassification.progression),
    "Office Key Piece":                 FNaFBItemData("Quest",      756783_041, ItemClassification.progression_skip_balancing,           6),
    "Backroom BB":                      FNaFBItemData("Quest",      756783_042, ItemClassification.progression),
    "Restrooms BB":                     FNaFBItemData("Quest",      756783_043, ItemClassification.progression),
    "Supply Closet BB":                 FNaFBItemData("Quest",      756783_044, ItemClassification.progression),
    "East Hall Corner BB":              FNaFBItemData("Quest",      756783_045, ItemClassification.progression),

    # Junk
    "Small Pizza":              FNaFBItemData("Filler",     756783_046, weight=2),
    "Medium Pizza":             FNaFBItemData("Filler",     756783_047, weight=3),
    "Large Pizza":              FNaFBItemData("Filler",     756783_048, weight=4),
    "Small Soda":               FNaFBItemData("Filler",     756783_049, weight=2),
    "Medium Soda":              FNaFBItemData("Filler",     756783_050, weight=3),
    "Large Soda":               FNaFBItemData("Filler",     756783_051, weight=4),
    "Pizza Slice":              FNaFBItemData("Filler",     756783_052, weight=1),
    "Cake":                     FNaFBItemData("Filler",     756783_053, weight=3),
    "Birthday Present":         FNaFBItemData("Filler",     756783_054, weight=1),
    "X-Large Pizza":            FNaFBItemData("Filler",     756783_055, weight=2),
    "X-Large Soda":             FNaFBItemData("Filler",     756783_056, weight=2),
    "HP Boost":                 FNaFBItemData("Filler",     756783_057, weight=2),
    "MP Boost":                 FNaFBItemData("Filler",     756783_058, weight=2),
    "Attack Boost":             FNaFBItemData("Filler",     756783_059, weight=2),
    "Defense Boost":            FNaFBItemData("Filler",     756783_060, weight=2),
    "Interior Walls Key":       FNaFBItemData("Filler",     756783_061, weight=2)
}
