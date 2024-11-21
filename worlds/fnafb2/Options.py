from typing import Dict
from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionSet


class Goal(Choice):
    """
    Choose which goal you want to beat.
    (Refurbs is not recommended for beginners.)
    """
    option_bb = 0
    option_refurbs = 1
    default = 0

class TradeQuest(Toggle):
    """
    Includes RNG Trade Item drops in the randomizer.
    (Adds 5 locations.)
    """
    display_name = "Include Trade Checks"

class Difficulty(Choice):
    """
    Playing on Proud will include the 3 extra chests on the show stage, the cassettes and rap god boss as locations.
    """
    display_name = "Difficulty"
    option_standard = 0
    option_proud = 1
    default = 0

class FemRods(DefaultOnToggle):
    """
    Turning this on will force both Rod of Femininity A and B to be filler items.
    """
    display_name = "Exclude Rod of Femininity"

class BossRush(DefaultOnToggle):
    """
    Turning this on will force Boss Rush to be a filler item.
    This setting is ignored if goal is set to refurbs.
    """
    display_name = "Exclude Boss Rush"
    
class Levelsanity(Toggle):
    """
    Includes each level up and each ability learned as an item location.
    (Adds 108 locations)
    """
    display_name = "Include Levelsanity"

#class DeathLink(Toggle):
#    """
#    If your party dies, so do your friends! The opposite is also true, of course.
#    """
#    display_name = "Deathlink"


fnafb2_options: Dict[str, type(Option)] = {
    "Goal": Goal,
    "trade_quest": TradeQuest,
    "difficulty": Difficulty,
    "fem_rods": FemRods,
    "boss_rush": BossRush,
    "levelsanity": Levelsanity
#    "death_link": DeathLink
}