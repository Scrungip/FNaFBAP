from BaseClasses import CollectionState, MultiWorld, Location, Region, Item
from .Regions import connect_regions
from Options import Toggle

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
    return TotalAttack(state, player) >= 19 \
    and TotalDefense(state, player) >= 35 \
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


def set_rules(multiworld: MultiWorld, player: int):
    # Bosses
    multiworld.get_location("Show Stage - Toy Freddy", player).access_rule = \
        lambda state: can_fight_lategame(state, player) and FreddyStat(state, player) >= 5
    
    multiworld.get_location("Backroom - Toy Bonnie", player).access_rule = \
        lambda state: can_fight_lategame(state, player) and BonnieStat(state, player) >= 5
    
    multiworld.get_location("Pirate Cove - Mangle", player).access_rule = \
        lambda state: can_fight_lategame(state, player) and FoxyStat(state, player) >= 5
    
    multiworld.get_location("Restrooms - Toy Chica", player).access_rule = \
        lambda state: can_fight_lategame(state, player) and ChicaStat(state, player) >= 5
    
    multiworld.get_location("The Puppet", player).access_rule = \
        lambda state: can_fight_lategame(state, player) and \
            state.can_reach("Show Stage - Toy Freddy", 'Location', player) and \
            state.can_reach("Backroom - Toy Bonnie", 'Location', player) and \
            state.can_reach("Pirate Cove - Mangle", 'Location', player) and \
            state.can_reach("Restrooms - Toy Chica", 'Location', player)
    
    multiworld.get_location("Office - Golden Freddy", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    

    # Shop Gates
    multiworld.get_location("Restrooms - Beta Party Hat", player).access_rule = \
        lambda state: can_fight_earlygame(state, player)
    
    multiworld.get_location("Supply Closet - Gamma Party Hat", player).access_rule = \
        lambda state: can_fight_midgame(state, player)

    multiworld.get_location("East Hall Corner - Omega Party Hat", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    
    # Cameras
    multiworld.get_location("Show Stage - Camera", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("Dining Area - Camera", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("Backroom - Camera", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("Restrooms - Camera", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("East Hall - Camera", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("West Hall - Camera", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    
    multiworld.get_location("Supply Closet - Camera", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    multiworld.get_location("Pirate Cove - Camera", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    multiworld.get_location("West Hall Corner - Camera", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    multiworld.get_location("East Hall Corner - Camera", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    
    # Stage Chests
    multiworld.get_location("Show Stage - Left Chest", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("Show Stage - Right Chest", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    

    # Story Quests
    multiworld.get_location("Restrooms - Turn in Bonnie's Head Voucher", player).access_rule = \
        lambda state: state.can_reach("Restrooms - Beta Party Hat", 'Location', player) and state.has("Bonnie's Head Voucher", player)
    multiworld.get_location("Backroom - Return Bonnie's Head", player).access_rule = \
        lambda state: state.has("Bonnie's Head", player)
    multiworld.get_location("Pirate Cove - Burn the place to the ground", player).access_rule = \
        lambda state: state.has("Lighter", player)
    multiworld.get_location("Kitchen - Chica", player).access_rule = \
        lambda state: state.has("Kitchen Key", player)
    

    # Enemy Trade Item Drops
    if multiworld.trade_quest[player] == Toggle.option_true:
        multiworld.get_location("Dining Area - Trade Beta Voucher", player).access_rule = \
            lambda state: can_fight_earlygame(state, player)
    
    if multiworld.trade_quest[player] == Toggle.option_true:
        multiworld.get_location("Dining Area - Trade Gamma Voucher", player).access_rule = \
            lambda state: can_fight_midgame(state, player)
    if multiworld.trade_quest[player] == Toggle.option_true:
        multiworld.get_location("Dining Area - Trade Omega Voucher", player).access_rule = \
            lambda state: can_fight_lategame(state, player)
    
    if multiworld.trade_quest[player] == Toggle.option_true and multiworld.interior_walls[player] == Toggle.option_true:
        multiworld.get_location("Dining Area - Trade Hearts Voucher", player).access_rule = \
            lambda state: can_fight_postgame(state, player) and state.has("Reveal Interior Walls", player)
    if multiworld.trade_quest[player] == Toggle.option_true and multiworld.interior_walls[player] == Toggle.option_true:
        multiworld.get_location("Dining Area - Trade Spades Voucher", player).access_rule = \
            lambda state: can_fight_postgame(state, player) and state.has("Reveal Interior Walls", player)
    if multiworld.trade_quest[player] == Toggle.option_true and multiworld.interior_walls[player] == Toggle.option_true:
        multiworld.get_location("Dining Area - Trade Clubs Voucher", player).access_rule = \
            lambda state: can_fight_postgame(state, player) and state.has("Reveal Interior Walls", player)
    if multiworld.trade_quest[player] == Toggle.option_true and multiworld.interior_walls[player] == Toggle.option_true:
        multiworld.get_location("Dining Area - Trade Diamonds Voucher", player).access_rule = \
            lambda state: can_fight_postgame(state, player) and state.has("Reveal Interior Walls", player)
        
    # Levelsanity
    if multiworld.levelsanity[player] == Toggle.option_true:
        # Freddy
        multiworld.get_location("Freddy - Level 6", player).access_rule = \
            lambda state: can_fight_earlygame(state, player)
        multiworld.get_location("Freddy - Level 7", player).access_rule = \
            lambda state: can_fight_earlygame(state, player)
        multiworld.get_location("Freddy - Level 8", player).access_rule = \
            lambda state: can_fight_earlygame(state, player)
        multiworld.get_location("Freddy - Level 9", player).access_rule = \
            lambda state: can_fight_earlygame(state, player)
        multiworld.get_location("Freddy - Level 10", player).access_rule = \
            lambda state: can_fight_earlygame(state, player)
        
        multiworld.get_location("Freddy - Level 11", player).access_rule = \
            lambda state: can_fight_midgame(state, player)
        multiworld.get_location("Freddy - Level 12", player).access_rule = \
            lambda state: can_fight_midgame(state, player)
        multiworld.get_location("Freddy - Level 13", player).access_rule = \
            lambda state: can_fight_midgame(state, player)
        multiworld.get_location("Freddy - Level 14", player).access_rule = \
            lambda state: can_fight_midgame(state, player)
        multiworld.get_location("Freddy - Level 15", player).access_rule = \
            lambda state: can_fight_midgame(state, player)
        
        multiworld.get_location("Freddy - Level 16", player).access_rule = \
            lambda state: can_fight_lategame(state, player)
        multiworld.get_location("Freddy - Level 17", player).access_rule = \
            lambda state: can_fight_lategame(state, player)
        multiworld.get_location("Freddy - Level 18", player).access_rule = \
            lambda state: can_fight_lategame(state, player)
        multiworld.get_location("Freddy - Level 19", player).access_rule = \
            lambda state: can_fight_lategame(state, player)
        multiworld.get_location("Freddy - Level 20", player).access_rule = \
            lambda state: can_fight_lategame(state, player)
        # Bonnie
        multiworld.get_location("Bonnie - Level 1", player).access_rule = \
            lambda state: state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 2", player).access_rule = \
            lambda state: state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 3", player).access_rule = \
            lambda state: state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 4", player).access_rule = \
            lambda state: state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 5", player).access_rule = \
            lambda state: state.has("Bonnie", player)

        multiworld.get_location("Bonnie - Level 6", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 7", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 8", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 9", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 10", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Bonnie", player)
        
        multiworld.get_location("Bonnie - Level 11", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 12", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 13", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 14", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 15", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Bonnie", player)
        
        multiworld.get_location("Bonnie - Level 16", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 17", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 18", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 19", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Bonnie", player)
        multiworld.get_location("Bonnie - Level 20", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Bonnie", player)
        # Chica
        multiworld.get_location("Chica - Level 1", player).access_rule = \
            lambda state: state.has("Chica", player)
        multiworld.get_location("Chica - Level 2", player).access_rule = \
            lambda state: state.has("Chica", player)
        multiworld.get_location("Chica - Level 3", player).access_rule = \
            lambda state: state.has("Chica", player)
        multiworld.get_location("Chica - Level 4", player).access_rule = \
            lambda state: state.has("Chica", player)
        multiworld.get_location("Chica - Level 5", player).access_rule = \
            lambda state: state.has("Chica", player)

        multiworld.get_location("Chica - Level 6", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Chica", player)
        multiworld.get_location("Chica - Level 7", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Chica", player)
        multiworld.get_location("Chica - Level 8", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Chica", player)
        multiworld.get_location("Chica - Level 9", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Chica", player)
        multiworld.get_location("Chica - Level 10", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Chica", player)
        
        multiworld.get_location("Chica - Level 11", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Chica", player)
        multiworld.get_location("Chica - Level 12", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Chica", player)
        multiworld.get_location("Chica - Level 13", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Chica", player)
        multiworld.get_location("Chica - Level 14", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Chica", player)
        multiworld.get_location("Chica - Level 15", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Chica", player)
        
        multiworld.get_location("Chica - Level 16", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Chica", player)
        multiworld.get_location("Chica - Level 17", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Chica", player)
        multiworld.get_location("Chica - Level 18", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Chica", player)
        multiworld.get_location("Chica - Level 19", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Chica", player)
        multiworld.get_location("Chica - Level 20", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Chica", player)
        # Foxy
        multiworld.get_location("Foxy - Level 1", player).access_rule = \
            lambda state: state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 2", player).access_rule = \
            lambda state: state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 3", player).access_rule = \
            lambda state: state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 4", player).access_rule = \
            lambda state: state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 5", player).access_rule = \
            lambda state: state.has("Foxy", player)

        multiworld.get_location("Foxy - Level 6", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 7", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 8", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 9", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 10", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Foxy", player)
        
        multiworld.get_location("Foxy - Level 11", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 12", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 13", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 14", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 15", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Foxy", player)
        
        multiworld.get_location("Foxy - Level 16", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 17", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 18", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 19", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Foxy", player)
        multiworld.get_location("Foxy - Level 20", player).access_rule = \
            lambda state: can_fight_lategame(state, player) and state.has("Foxy", player)
    
    # Connect regions at rule runtime
    connect_regions(multiworld, player, "Menu", "Show Stage")
    connect_regions(multiworld, player, "Show Stage", "Backroom")
    connect_regions(multiworld, player, "Show Stage", "Restrooms")
    connect_regions(multiworld, player, "Show Stage", "Pirate Cove")
    connect_regions(multiworld, player, "Show Stage", "West Hall")
    connect_regions(multiworld, player, "Show Stage", "East Hall")
    if multiworld.trade_quest[player] == Toggle.option_true:
        connect_regions(multiworld, player, "Show Stage", "Trade Machine")
    if multiworld.trade_quest[player] == Toggle.option_true and multiworld.interior_walls[player] == Toggle.option_true:
        connect_regions(multiworld, player, "Trade Machine", "Trade Machine IW")
    if multiworld.levelsanity[player] == Toggle.option_true:
        connect_regions(multiworld, player, "Show Stage", "Levelsanity")
    if multiworld.interior_walls[player] == Toggle.option_true:
        connect_regions(multiworld, player, "Show Stage", "Interior Walls", lambda state: can_fight_postgame(state, player) and state.has("Reveal Interior Walls", player))
    connect_regions(multiworld, player, "Backroom", "Backroom BB", lambda state: state.has("Backroom BB", player))
    connect_regions(multiworld, player, "Restrooms", "Restrooms BB", lambda state: state.can_reach("Restrooms - Beta Party Hat", 'Location', player) and state.has("Restrooms BB", player))
    connect_regions(multiworld, player, "West Hall", "Supply Closet")
    connect_regions(multiworld, player, "Supply Closet", "Supply Closet BB", lambda state: state.can_reach("Supply Closet - Gamma Party Hat", 'Location', player) and state.has("Supply Closet BB", player))
    connect_regions(multiworld, player, "West Hall", "West Hall Corner")
    connect_regions(multiworld, player, "West Hall Corner", "Office", lambda state: state.count("Office Key Piece", player) >= 4)
    connect_regions(multiworld, player, "East Hall", "East Hall Corner")
    connect_regions(multiworld, player, "East Hall Corner", "East Hall Corner BB", lambda state: state.can_reach("East Hall Corner - Omega Party Hat", 'Location', player) and state.has("East Hall Corner BB", player))
    connect_regions(multiworld, player, "East Hall Corner", "Office", lambda state: state.count("Office Key Piece", player) >= 4)


    # Win Condition
    multiworld.completion_condition[player] = lambda state: state.can_reach("Office - Golden Freddy", 'Location', player)
