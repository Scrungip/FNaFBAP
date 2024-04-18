from typing import Dict

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionSet


class TradeQuest(Toggle):
    """
    Includes RNG Trade Item drops in logic.
    """
    display_name = "Include Trade Checks"


class InteriorWalls(Toggle):
    """
    Includes Interior Walls in logic.
    """
    display_name = "Include Interior Walls"


#class DeathLink(Toggle):
#    """
#    If your party dies, so do your friends! The opposite is also true, of course.
#    """
#    display_name = "Deathlink"


fnafb_options: Dict[str, type(Option)] = { 
    "trade_quest": TradeQuest,
    "interior_walls": InteriorWalls
#    "death_link": DeathLink
}
