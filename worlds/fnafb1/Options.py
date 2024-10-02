from typing import Dict
from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionSet


class TradeQuest(Toggle):
    """
    Includes RNG Trade Item drops in the randomizer.
    (Adds 4 locations, or 8 if Interior Walls is also enabled.)
    """
    display_name = "Include Trade Checks"


class InteriorWalls(Toggle):
    """
    Includes Interior Walls in the randomizer.
    (Adds 30 locations.)
    """
    display_name = "Include Interior Walls"


class Levelsanity(Toggle):
    """
    Includes each level up as an item location.
    (Adds 80 locations.)
    """
    display_name = "Include Levelsanity"


#class DeathLink(Toggle):
#    """
#    If your party dies, so do your friends! The opposite is also true, of course.
#    """
#    display_name = "Deathlink"


fnafb_options: Dict[str, type(Option)] = { 
    "trade_quest": TradeQuest,
    "interior_walls": InteriorWalls,
    "levelsanity": Levelsanity
#    "death_link": DeathLink
}