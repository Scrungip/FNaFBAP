from BaseClasses import CollectionState, MultiWorld, Location, Region, Item
from .Regions import connect_regions
from Options import Toggle

def party_count(state: CollectionState, player: int) -> int:
    return state.count("Bonnie", player) \
    + state.count("Chica", player) \
    + state.count("Foxy", player) \
    + 1 # This one's to account for Freddy

# Check if the player has the party members before adding their power to the calculation
def attack_power(state: CollectionState, player: int) -> int:
    return state.count("Progressive Microphone", player) \
    + state.count("Bonnie", player) * state.count("Progressive Guitar", player) \
    + state.count("Chica", player) * state.count("Progressive Cupcakes", player) \
    + state.count("Foxy", player) * state.count("Progressive Hook", player)

# This one's a bit of a mess, might have to rethink it at a later time
def skills(state: CollectionState, player: int) -> int:
    return state.count("Tophat Toss", player) \
    + state.count("Lead Stinger", player) \
    + state.count("Toreador March", player) \
    + (state.count("Bunny Hop", player) \
    + state.count("Backup Bash", player) \
    + state.count("Guitar Smash", player)) \
    * state.count("Bonnie", player) \
    + (state.count("Pizza Pass", player) \
    + state.count("Caffeine Revival", player)) \
    * state.count("Chica", player) \
    + (state.count("Rushdown", player) \
    + state.count("Plank Walk", player)) \
    * state.count("Foxy", player)

# Endoskeletons provide more defense so we should treat it as such
def total_defense(state: CollectionState, player: int) -> int:
    return (state.count("Progressive Body Endoskeletons", player) * 4 \
    + state.count("Progressive Head Endoskeletons", player) * 4 \
    + state.count("Progressive Pizza Shields", player) \
    + state.count("Progressive Caffeine Sodas", player)) \
    * party_count(state, player)


def can_fight_earlygame(state: CollectionState, player: int) -> bool:
    return attack_power(state, player) >= 2 \
    and total_defense(state, player) >= 4 \


def can_fight_midgame(state: CollectionState, player: int) -> bool:
    return attack_power(state, player) >= 4 \
    and total_defense(state, player) >= 10 \
    and party_count(state, player) >= 2 \
    and skills(state, player) >= 2


def can_fight_lategame(state: CollectionState, player: int) -> bool:
    return attack_power(state, player) >= 12 \
    and total_defense(state, player) >= 24 \
    and party_count(state, player) >= 3 \
    and skills(state, player) >= 6 \
    and state.has("Plank Walk", player) \
    and state.has("Foxy", player)


def can_fight_postgame(state: CollectionState, player: int) -> bool:
    return attack_power(state, player) >= 20 \
    and total_defense(state, player) >= 30 \
    and party_count(state, player) >= 4 \
    and skills(state, player) >= 8 \
    and state.count("Plank Walk", player) >= 1 \
    and state.count("Foxy", player) >= 1


def set_rules(multiworld: MultiWorld, player: int):
    # Bosses
    multiworld.get_location("Show Stage - Toy Freddy", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    
    multiworld.get_location("Backroom - Toy Bonnie", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    
    multiworld.get_location("Pirate Cove - Mangle", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    
    multiworld.get_location("Restrooms - Toy Chica", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    
    multiworld.get_location("The Puppet", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    
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
        lambda state: can_fight_earlygame(state, player)
    multiworld.get_location("Dining Area - Camera", player).access_rule = \
        lambda state: can_fight_earlygame(state, player)
    
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
        lambda state: state.has("Bonnie's Head Voucher", player) and state.has("Chica", player)
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
            lambda state: can_fight_postgame(state, player) and state.has("Interior Walls Unlock", player)
    if multiworld.trade_quest[player] == Toggle.option_true and multiworld.interior_walls[player] == Toggle.option_true:
        multiworld.get_location("Dining Area - Trade Spades Voucher", player).access_rule = \
            lambda state: can_fight_postgame(state, player) and state.has("Interior Walls Unlock", player)
    if multiworld.trade_quest[player] == Toggle.option_true and multiworld.interior_walls[player] == Toggle.option_true:
        multiworld.get_location("Dining Area - Trade Clubs Voucher", player).access_rule = \
            lambda state: can_fight_postgame(state, player) and state.has("Interior Walls Unlock", player)
    if multiworld.trade_quest[player] == Toggle.option_true and multiworld.interior_walls[player] == Toggle.option_true:
        multiworld.get_location("Dining Area - Trade Diamonds Voucher", player).access_rule = \
            lambda state: can_fight_postgame(state, player) and state.has("Interior Walls Unlock", player)
    
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
    if multiworld.interior_walls[player] == Toggle.option_true:
        connect_regions(multiworld, player, "Show Stage", "Interior Walls", lambda state: can_fight_postgame(state, player) and state.has("Interior Walls Unlock", player))
    connect_regions(multiworld, player, "Backroom", "Backroom BB", lambda state: state.has("Backroom BB", player))
    connect_regions(multiworld, player, "Restrooms", "Restrooms BB", lambda state: state.can_reach("Restrooms - Beta Party Hat", 'Location', player) and state.has("Restrooms BB", player))
    connect_regions(multiworld, player, "West Hall", "Supply Closet")
    connect_regions(multiworld, player, "Supply Closet", "Supply Closet BB", lambda state: state.can_reach("Supply Closet - Gamma Party Hat", 'Location', player) and state.has("Supply Closet BB", player))
    connect_regions(multiworld, player, "West Hall", "West Hall Corner")
    connect_regions(multiworld, player, "West Hall Corner", "Office", lambda state: state.count("Office Key Piece", player) >= 4)
    connect_regions(multiworld, player, "East Hall", "East Hall Corner")
    connect_regions(multiworld, player, "East Hall Corner", "Office", lambda state: state.count("Office Key Piece", player) >= 4)


    # Win Condition
    multiworld.completion_condition[player] = lambda state: state.can_reach("Office - Golden Freddy", 'Location', player)
