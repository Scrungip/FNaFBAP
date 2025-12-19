from typing import Dict
from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionSet, PerGameCommonOptions

from dataclasses import dataclass

class Goal(Choice):
    """
    Specify which ending you'll be required to achieve.
    """
    display_name = "Goal"
    default = 0
    option_golden_freddy = 0
    option_puppetmaster_bb = 1

class StartingCharacter(Choice):
    """
    Choose the character you will have at the start of the game.
    Dialogue will be changed according to the character you start the game with.
    """
    display_name = "Starting Character"
    default = "random"
    option_freddy = 0
    option_bonnie = 1
    option_chica = 2
    option_foxy = 3


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


class DeveloperIntrusion(Toggle):
    """
    Find my checks.
    (Adds 6 or 26 locations depending on settings.)
    """
    display_name = "Allow Scrungip to enter this Multiworld"


#class DeathLink(Toggle):
#    """
#    If your party dies, so do your friends! The opposite is also true, of course.
#    """
#    display_name = "Deathlink"


@dataclass
class FNaFB1Options(PerGameCommonOptions):
    goal: Goal
    starter: StartingCharacter
    trade_quest: TradeQuest
    interior_walls: InteriorWalls
    levelsanity: Levelsanity
    developer_intrusion: DeveloperIntrusion
#    death_link: DeathLink
