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
    Playing on Critical will include everything on Proud plus each keystone for ability unlocks and 2 chests in Kid's Cove.
    """
    display_name = "Difficulty"
    option_standard = 0
    option_proud = 1
    option_critical = 2
    default = 0

class FemRods(DefaultOnToggle):
    """
    Turning this on will force both Rod of Femininity A and B to be filler items.
    If this is off, all locations in the women's bathroom won't be in logic until the second puppet is accessible.
    """
    display_name = "Exclude Rod of Femininity"

class ExtraChecks(DefaultOnToggle):
    """
    Turning this on will force Boss Rush and the Dragon Dildo F check to be a filler item.
    This setting is ignored if goal is set to refurbs.
    """
    display_name = "Exclude Extra Checks"
    
class ShadowBonnie(Toggle):
    """
    Turning this on will force the Shadow Bonnie bossfight check to be a filler item.
    This setting is only affected if the critical difficulty is enabled. 
    """
    display_name = "Exclude Shadow Bonnie"
    
class Levelsanity(Toggle):
    """
    Includes each level up and each ability learned as an item location.
    This setting is ignored if the difficulty is critical
    (Adds 100 locations)
    """
    display_name = "Include Levelsanity"
    
class GrindyChecks(Toggle):
    """
    Turning this on will exclude checks that involve toy freddy using his
    abilities 20 or 40 times.
    """
    display_name = "Exclude Grindy Checks"

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
    "extra_checks": ExtraChecks,
    "shadow_bonnie": ShadowBonnie,
    "levelsanity": Levelsanity,
    "grindy": GrindyChecks
#    "death_link": DeathLink
}