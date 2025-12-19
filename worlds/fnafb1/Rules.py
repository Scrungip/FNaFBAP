from BaseClasses import CollectionState, Location, Region, Item
from .Regions import connect_regions
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import FNaFB1World

def FreddyStat(state: CollectionState, player: int) -> int:
    if state.has("Freddy", player):
        return state.count("Progressive Microphone", player)
    else:
        return 0

def BonnieStat(state: CollectionState, player: int) -> int:
    if state.has("Bonnie", player):
        return state.count("Progressive Guitar", player)
    else:
        return 0

def ChicaStat(state: CollectionState, player: int) -> int:
    if state.has("Chica", player):
        return state.count("Progressive Cupcakes", player)
    else:
        return 0
    
def FoxyStat(state: CollectionState, player: int) -> int:
    if state.has("Foxy", player):
        return state.count("Progressive Hook", player)
    else:
        return 0
    
def FreddySkill(state: CollectionState, player: int) -> int:
    if state.has("Freddy", player):
        return state.count("Tophat Toss", player) \
        + state.count("Lead Stinger", player) \
        + state.count("Toreador March", player)
    else: return 0

def BonnieSkill(state: CollectionState, player: int) -> int:
    if state.has("Bonnie", player):
        return state.count("Bunny Hop", player) \
        + state.count("Backup Bash", player)
    else:
        return 0
    
def ChicaSkill(state: CollectionState, player: int) -> int:
    if state.has("Chica", player):
        return state.count("Fearless Flight", player)
    else:
        return 0
    
def FoxySkill(state: CollectionState, player: int) -> int:
    if state.has("Foxy", player):
        return state.count("Rushdown", player) \
        + state.count("Plank Walk", player)
    else:
        return 0
    
def FreddyCanSkill(state: CollectionState, player: int) -> bool:
    return FreddySkill(state, player) >= 1

def BonnieCanSkill(state: CollectionState, player: int) -> bool:
    return BonnieSkill(state, player) >= 1

def ChicaCanSkill(state: CollectionState, player: int) -> bool:
    return ChicaSkill(state, player) >= 1

def FoxyCanSkill(state: CollectionState, player: int) -> bool:
    return FoxySkill(state, player) >= 1

def PartyCount(state: CollectionState, player: int) -> int:
    return state.count("Freddy", player) \
    + state.count("Bonnie", player) \
    + state.count("Chica", player) \
    + state.count("Foxy", player)

def PartyCanSkill(state: CollectionState, player: int) -> int:
    partyskill = 0
    if FreddyCanSkill(state, player):
        partyskill += 1
    if BonnieCanSkill(state, player):
        partyskill += 1
    if ChicaCanSkill(state, player):
        partyskill += 1
    if FoxyCanSkill(state, player):
        partyskill += 1
    return partyskill

def TotalAttack(state: CollectionState, player: int) -> int:
    return FreddyStat(state, player) \
    + BonnieStat(state, player) \
    + ChicaStat(state, player) \
    + FoxyStat(state, player)

def TotalSkills(state: CollectionState, player: int) -> int:
    return FreddySkill(state, player) \
    + BonnieSkill(state, player) \
    + ChicaSkill(state, player) \
    + FoxySkill(state, player)

# Endoskeletons provide more defense so we should treat it as such
def TotalDefense(state: CollectionState, player: int) -> int:
    return state.count("Progressive Body Endoskeletons", player) * 5 \
    + state.count("Progressive Head Endoskeletons", player) * 5 \
    + state.count("Progressive Pizza Shields", player) \
    + state.count("Progressive Caffeine Sodas", player)


def can_fight_earlygame(state: CollectionState, player: int) -> bool:
    return TotalAttack(state, player) >= 1


def can_fight_midgame(state: CollectionState, player: int) -> bool:
    return TotalAttack(state, player) >= 3 \
    and TotalDefense(state, player) >= 8 \
    and PartyCount(state, player) >= 2 \
    and PartyCanSkill(state, player) >= 1


def can_fight_lategame(state: CollectionState, player: int) -> bool:
    return TotalAttack(state, player) >= 17 \
    and TotalDefense(state, player) >= 32 \
    and PartyCount(state, player) >= 4 \
    and PartyCanSkill(state, player) >= 3


def can_fight_postgame(state: CollectionState, player: int) -> bool:
    return TotalAttack(state, player) >= 23 \
    and TotalDefense(state, player) >= 45 \
    and PartyCount(state, player) >= 4 \
    and FreddySkill(state, player) >= 3 \
    and BonnieSkill(state, player) >= 2 \
    and ChicaSkill(state, player) >= 1 \
    and FoxySkill(state, player) >= 2


def set_rules(world: "FNaFB1World", player: int):
    # Bosses
    world.get_location("Show Stage - Toy Freddy").access_rule = \
        lambda state: can_fight_lategame(state, player) and FreddyStat(state, player) >= 5
    
    world.get_location("Backroom - Toy Bonnie").access_rule = \
        lambda state: can_fight_lategame(state, player) and BonnieStat(state, player) >= 5
    
    world.get_location("Pirate Cove - Mangle").access_rule = \
        lambda state: can_fight_lategame(state, player) and FoxyStat(state, player) >= 5
    
    world.get_location("Restrooms - Toy Chica").access_rule = \
        lambda state: can_fight_lategame(state, player) and ChicaStat(state, player) >= 5
    
    world.get_location("Restrooms - The Puppet").access_rule = \
        lambda state: can_fight_lategame(state, player) and \
            state.can_reach("Show Stage - Toy Freddy", 'Location', player) and \
            state.can_reach("Backroom - Toy Bonnie", 'Location', player) and \
            state.can_reach("Pirate Cove - Mangle", 'Location', player) and \
            state.can_reach("Restrooms - Toy Chica", 'Location', player)
    
    world.get_location("Office - Golden Freddy").access_rule = \
        lambda state: can_fight_lategame(state, player)
    

    # Shop Gates
    world.get_location("Restrooms - Beta Party Hat").access_rule = \
        lambda state: can_fight_earlygame(state, player)
    
    world.get_location("Supply Closet - Gamma Party Hat").access_rule = \
        lambda state: can_fight_midgame(state, player)

    world.get_location("East Hall Corner - Omega Party Hat").access_rule = \
        lambda state: can_fight_lategame(state, player)
    
    # Cameras
    world.get_location("Show Stage - Camera").access_rule = \
        lambda state: can_fight_midgame(state, player)
    world.get_location("Dining Area - Camera").access_rule = \
        lambda state: can_fight_midgame(state, player)
    world.get_location("Backroom - Camera").access_rule = \
        lambda state: can_fight_midgame(state, player)
    world.get_location("Restrooms - Camera").access_rule = \
        lambda state: can_fight_midgame(state, player)
    world.get_location("East Hall - Camera").access_rule = \
        lambda state: can_fight_midgame(state, player)
    world.get_location("West Hall - Camera").access_rule = \
        lambda state: can_fight_midgame(state, player)
    
    world.get_location("Supply Closet - Camera").access_rule = \
        lambda state: can_fight_lategame(state, player)
    world.get_location("Pirate Cove - Camera").access_rule = \
        lambda state: can_fight_lategame(state, player)
    world.get_location("West Hall Corner - Camera").access_rule = \
        lambda state: can_fight_lategame(state, player)
    world.get_location("East Hall Corner - Camera").access_rule = \
        lambda state: can_fight_lategame(state, player)
    
    # Stage Chests
    world.get_location("Show Stage - Left Chest").access_rule = \
        lambda state: can_fight_midgame(state, player)
    world.get_location("Show Stage - Right Chest").access_rule = \
        lambda state: can_fight_lategame(state, player)
    
    # Final Version Additions
    world.get_location("Dining Area - Chest").access_rule = \
        lambda state: can_fight_midgame(state, player)
    world.get_location("Backroom - Chest").access_rule = \
        lambda state: can_fight_midgame(state, player)
    world.get_location("Pirate Cove - Chest").access_rule = \
        lambda state: can_fight_midgame(state, player) and state.has("Lighter", player)
    world.get_location("West Hall - Chest").access_rule = \
        lambda state: can_fight_lategame(state, player)
    world.get_location("East Hall Corner - Chest").access_rule = \
        lambda state: can_fight_lategame(state, player)
    world.get_location("Dining Area - Dragon Dildo Ritual").access_rule = \
        lambda state: state.has("Progressive Dragon Dildo", player) and state.has("Freddy", player)

    # Story Quests
    world.get_location("Restrooms - Turn in Bonnie's Head Voucher").access_rule = \
        lambda state: state.can_reach("Restrooms - Beta Party Hat", 'Location', player) and state.has("Bonnie's Head Voucher", player)
    world.get_location("Backroom - Return Bonnie's Head").access_rule = \
        lambda state: state.has("Bonnie's Head", player)
    world.get_location("Pirate Cove - Burn the place to the ground").access_rule = \
        lambda state: state.has("Lighter", player)
    world.get_location("Kitchen - Chica").access_rule = \
        lambda state: state.has("Kitchen Key", player)
    

    # Enemy Trade Item Drops
    if world.options.trade_quest:
        world.get_location("Show Stage - Trade Beta Voucher").access_rule = \
            lambda state: can_fight_earlygame(state, player)
    
    if world.options.trade_quest:
        world.get_location("Show Stage - Trade Gamma Voucher").access_rule = \
            lambda state: can_fight_midgame(state, player)
    if world.options.trade_quest:
        world.get_location("Show Stage - Trade Omega Voucher").access_rule = \
            lambda state: can_fight_lategame(state, player)
    
    if world.options.trade_quest and world.options.interior_walls:
        world.get_location("Show Stage - Trade Hearts Voucher").access_rule = \
            lambda state: can_fight_postgame(state, player) and state.has("Reveal Interior Walls", player)
    if world.options.trade_quest and world.options.interior_walls:
        world.get_location("Show Stage - Trade Spades Voucher").access_rule = \
            lambda state: can_fight_postgame(state, player) and state.has("Reveal Interior Walls", player)
    if world.options.trade_quest and world.options.interior_walls:
        world.get_location("Show Stage - Trade Clubs Voucher").access_rule = \
            lambda state: can_fight_postgame(state, player) and state.has("Reveal Interior Walls", player)
    if world.options.trade_quest and world.options.interior_walls:
        world.get_location("Show Stage - Trade Diamonds Voucher").access_rule = \
            lambda state: can_fight_postgame(state, player) and state.has("Reveal Interior Walls", player)
        
    # Levelsanity
    if world.options.levelsanity:
        # Freddy
        world.get_location("Freddy - Level 1").access_rule = \
            lambda state: state.has("Freddy", player)
        world.get_location("Freddy - Level 2").access_rule = \
            lambda state: state.has("Freddy", player)
        world.get_location("Freddy - Level 3").access_rule = \
            lambda state: state.has("Freddy", player)
        world.get_location("Freddy - Level 4").access_rule = \
            lambda state: state.has("Freddy", player)
        world.get_location("Freddy - Level 5").access_rule = \
            lambda state: state.has("Freddy", player)
        
        world.get_location("Freddy - Level 6").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Freddy", player)
        world.get_location("Freddy - Level 7").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Freddy", player)
        world.get_location("Freddy - Level 8").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Freddy", player)
        world.get_location("Freddy - Level 9").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Freddy", player)
        world.get_location("Freddy - Level 10").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Freddy", player)
        
        world.get_location("Freddy - Level 11").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Freddy", player)
        world.get_location("Freddy - Level 12").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Freddy", player)
        world.get_location("Freddy - Level 13").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Freddy", player)
        world.get_location("Freddy - Level 14").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Freddy", player)
        world.get_location("Freddy - Level 15").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Freddy", player)
        
        world.get_location("Freddy - Level 16").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Freddy", player)
        world.get_location("Freddy - Level 17").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Freddy", player)
        world.get_location("Freddy - Level 18").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Freddy", player)
        world.get_location("Freddy - Level 19").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Freddy", player)
        world.get_location("Freddy - Level 20").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Freddy", player)
        # Bonnie
        world.get_location("Bonnie - Level 1").access_rule = \
            lambda state: state.has("Bonnie", player)
        world.get_location("Bonnie - Level 2").access_rule = \
            lambda state: state.has("Bonnie", player)
        world.get_location("Bonnie - Level 3").access_rule = \
            lambda state: state.has("Bonnie", player)
        world.get_location("Bonnie - Level 4").access_rule = \
            lambda state: state.has("Bonnie", player)
        world.get_location("Bonnie - Level 5").access_rule = \
            lambda state: state.has("Bonnie", player)

        world.get_location("Bonnie - Level 6").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Bonnie", player)
        world.get_location("Bonnie - Level 7").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Bonnie", player)
        world.get_location("Bonnie - Level 8").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Bonnie", player)
        world.get_location("Bonnie - Level 9").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Bonnie", player)
        world.get_location("Bonnie - Level 10").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Bonnie", player)
        
        world.get_location("Bonnie - Level 11").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Bonnie", player)
        world.get_location("Bonnie - Level 12").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Bonnie", player)
        world.get_location("Bonnie - Level 13").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Bonnie", player)
        world.get_location("Bonnie - Level 14").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Bonnie", player)
        world.get_location("Bonnie - Level 15").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Bonnie", player)
        
        world.get_location("Bonnie - Level 16").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Bonnie", player)
        world.get_location("Bonnie - Level 17").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Bonnie", player)
        world.get_location("Bonnie - Level 18").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Bonnie", player)
        world.get_location("Bonnie - Level 19").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Bonnie", player)
        world.get_location("Bonnie - Level 20").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Bonnie", player)
        # Chica
        world.get_location("Chica - Level 1").access_rule = \
            lambda state: state.has("Chica", player)
        world.get_location("Chica - Level 2").access_rule = \
            lambda state: state.has("Chica", player)
        world.get_location("Chica - Level 3").access_rule = \
            lambda state: state.has("Chica", player)
        world.get_location("Chica - Level 4").access_rule = \
            lambda state: state.has("Chica", player)
        world.get_location("Chica - Level 5").access_rule = \
            lambda state: state.has("Chica", player)

        world.get_location("Chica - Level 6").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Chica", player)
        world.get_location("Chica - Level 7").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Chica", player)
        world.get_location("Chica - Level 8").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Chica", player)
        world.get_location("Chica - Level 9").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Chica", player)
        world.get_location("Chica - Level 10").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Chica", player)
        
        world.get_location("Chica - Level 11").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Chica", player)
        world.get_location("Chica - Level 12").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Chica", player)
        world.get_location("Chica - Level 13").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Chica", player)
        world.get_location("Chica - Level 14").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Chica", player)
        world.get_location("Chica - Level 15").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Chica", player)
        
        world.get_location("Chica - Level 16").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Chica", player)
        world.get_location("Chica - Level 17").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Chica", player)
        world.get_location("Chica - Level 18").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Chica", player)
        world.get_location("Chica - Level 19").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Chica", player)
        world.get_location("Chica - Level 20").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Chica", player)
        # Foxy
        world.get_location("Foxy - Level 1").access_rule = \
            lambda state: state.has("Foxy", player)
        world.get_location("Foxy - Level 2").access_rule = \
            lambda state: state.has("Foxy", player)
        world.get_location("Foxy - Level 3").access_rule = \
            lambda state: state.has("Foxy", player)
        world.get_location("Foxy - Level 4").access_rule = \
            lambda state: state.has("Foxy", player)
        world.get_location("Foxy - Level 5").access_rule = \
            lambda state: state.has("Foxy", player)

        world.get_location("Foxy - Level 6").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Foxy", player)
        world.get_location("Foxy - Level 7").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Foxy", player)
        world.get_location("Foxy - Level 8").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Foxy", player)
        world.get_location("Foxy - Level 9").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Foxy", player)
        world.get_location("Foxy - Level 10").access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Foxy", player)
        
        world.get_location("Foxy - Level 11").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Foxy", player)
        world.get_location("Foxy - Level 12").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Foxy", player)
        world.get_location("Foxy - Level 13").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Foxy", player)
        world.get_location("Foxy - Level 14").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Foxy", player)
        world.get_location("Foxy - Level 15").access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Foxy", player)
        
        world.get_location("Foxy - Level 16").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Foxy", player)
        world.get_location("Foxy - Level 17").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Foxy", player)
        world.get_location("Foxy - Level 18").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Foxy", player)
        world.get_location("Foxy - Level 19").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Foxy", player)
        world.get_location("Foxy - Level 20").access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Foxy", player)
    
    # DLC
    if world.options.developer_intrusion:
        world.get_location("Hidden Room - Scrungip").access_rule = \
            lambda state: state.has("Reveal Interior Walls", player)
        world.get_location("Pirate Cove - Scrungip").access_rule = \
            lambda state: state.can_reach("Pirate Cove - Burn the place to the ground", 'Location', player)
        world.get_location("Backroom - The Mirror").access_rule = \
            lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_postgame(state, player)
        if world.options.levelsanity:
            world.get_location("Scrungip - Level 1").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player)
            world.get_location("Scrungip - Level 2").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player)
            world.get_location("Scrungip - Level 3").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player)
            world.get_location("Scrungip - Level 4").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player)
            world.get_location("Scrungip - Level 5").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player)
            world.get_location("Scrungip - Level 6").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_midgame(state, player)
            world.get_location("Scrungip - Level 7").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_midgame(state, player)
            world.get_location("Scrungip - Level 8").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_midgame(state, player)
            world.get_location("Scrungip - Level 9").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_midgame(state, player)
            world.get_location("Scrungip - Level 10").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_midgame(state, player)
            world.get_location("Scrungip - Level 11").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_lategame(state, player)
            world.get_location("Scrungip - Level 12").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_lategame(state, player)
            world.get_location("Scrungip - Level 13").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_lategame(state, player)
            world.get_location("Scrungip - Level 14").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_lategame(state, player)
            world.get_location("Scrungip - Level 15").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_lategame(state, player)
            world.get_location("Scrungip - Level 16").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_postgame(state, player)
            world.get_location("Scrungip - Level 17").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_postgame(state, player)
            world.get_location("Scrungip - Level 18").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_postgame(state, player)
            world.get_location("Scrungip - Level 19").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_postgame(state, player)
            world.get_location("Scrungip - Level 20").access_rule = \
                lambda state: state.can_reach("Hidden Room - Scrungip", 'Location', player) and state.can_reach("Pirate Cove - Scrungip", 'Location', player) and can_fight_postgame(state, player)
    if world.options.goal == "puppetmaster_bb":
        world.get_location("Show Stage - Puppetmaster BB").access_rule = \
            lambda state: can_fight_postgame(state, player)
    
    # Connect regions at rule runtime
    connect_regions(world, "Menu", "Show Stage")
    connect_regions(world, "Show Stage", "Backroom")
    connect_regions(world, "Show Stage", "Restrooms")
    connect_regions(world, "Show Stage", "Pirate Cove")
    connect_regions(world, "Show Stage", "West Hall")
    connect_regions(world, "Show Stage", "East Hall")
    if world.options.trade_quest:
        connect_regions(world, "Show Stage", "Trade Machine")
    if world.options.trade_quest and world.options.interior_walls:
        connect_regions(world, "Trade Machine", "Trade Machine IW")
    if world.options.levelsanity:
        connect_regions(world, "Show Stage", "Levelsanity")
    if world.options.interior_walls:
        connect_regions(world, "Show Stage", "Interior Walls", lambda state: can_fight_postgame(state, player) and state.has("Reveal Interior Walls", player))
    if world.options.developer_intrusion:
        connect_regions(world, "Show Stage", "Scrungip DLC", lambda state: state.has("Funky Scrungip Token", player))
        if world.options.levelsanity:
            connect_regions(world, "Scrungip DLC", "Scrungip DLC Levels")
    connect_regions(world, "Backroom", "Backroom BB", lambda state: state.has("Backroom BB", player))
    connect_regions(world, "Restrooms", "Restrooms BB", lambda state: state.can_reach("Restrooms - Beta Party Hat", 'Location', player) and state.has("Restrooms BB", player))
    connect_regions(world, "West Hall", "Supply Closet")
    connect_regions(world, "Supply Closet", "Supply Closet BB", lambda state: state.can_reach("Supply Closet - Gamma Party Hat", 'Location', player) and state.has("Supply Closet BB", player))
    connect_regions(world, "West Hall", "West Hall Corner")
    connect_regions(world, "West Hall Corner", "Office", lambda state: state.count("Office Key Piece", player) >= 4)
    connect_regions(world, "East Hall", "East Hall Corner")
    connect_regions(world, "East Hall Corner", "East Hall Corner BB", lambda state: state.can_reach("East Hall Corner - Omega Party Hat", 'Location', player) and state.has("East Hall Corner BB", player))
    connect_regions(world, "East Hall Corner", "Office", lambda state: state.count("Office Key Piece", player) >= 4)
    if world.options.goal == "puppetmaster_bb":
        connect_regions(world, "Office", "Puppetmaster BB")


    # Win Condition
    if world.options.goal == "golden_freddy":
        world.multiworld.completion_condition[player] = lambda state: state.can_reach("Office - Golden Freddy", 'Location', player)
    if world.options.goal == "puppetmaster_bb":
        world.multiworld.completion_condition[player] = lambda state: state.can_reach("Show Stage - Puppetmaster BB", 'Location', player)