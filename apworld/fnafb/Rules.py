from BaseClasses import CollectionState, MultiWorld

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
    return (state.count("Tophat Toss", player) \
    + state.count("Lead Stinger", player) \
    + state.count("Toreador March", player) \
    + (state.count("Bunny Hop", player) \
    + state.count("Backup Bash", player) \
    + state.count("Guitar Smash", player)) \
    * state.count("Bonnie", player) \
    + (state.count("Pizza Pass", player) \
    + state.count("Caffeine Revival", player)) \
    * state.count("Chica", player) \
    + state.count("Rushdown", player)) \
    * (state.count("Plank Walk", player) \
    + (1 * state.count("Plank Walk", player))) \
    * state.count("Foxy", player)
    # Plank Walk is arguably the most important of the bunch so I want to make sure logic accounts for it, I guess (idk what the fuck im doing)

# Endoskeletons provide more defense so we should treat it as such
def total_defense(state: CollectionState, player: int) -> int:
    return (state.count("Progressive Body Endoskeletons", player) * 4 \
    + state.count("Progressive Head Endoskeletons", player) * 4 \
    + state.count("Progressive Pizza Shields") \
    + state.count("Progressive Caffeine Sodas")) \
    * party_count(state, player)


def can_fight_earlygame(state: CollectionState, player: int) -> bool:
    return attack_power(state, player) >= 8 \
    and total_defense(state, player) >= 10 \
    and party_count(state, player) >= 2 \
    and skills(state, player) >= 3


def can_fight_midgame(state: CollectionState, player: int) -> bool:
    return attack_power(state, player) >= 13 \
    and total_defense(state, player) >= 22 \
    and party_count(state, player) >= 3 \
    and skills(state, player) >= 4


def can_fight_lategame(state: CollectionState, player: int) -> bool:
    return attack_power(state, player) >= 18 \
    and total_defense(state, player) >= 36 \
    and party_count(state, player) >= 4 \
    and skills(state, player) >= 6


def can_fight_postgame(state: CollectionState, player: int) -> bool:
    return attack_power(state, player) >= 24 \
    and total_defense(state, player) >= 40 \
    and party_count(state, player) >= 4 \
    and skills(state, player) >= 10


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
    
    multiworld.get_entrance("Office", player).access_rule = \
        lambda state: state.count("Office Key", player) >= 8
    multiworld.get_location("Office - Golden Freddy", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    

    # Interior Walls
    multiworld.get_entrance("Interior Walls", player).access_rule = \
        lambda state: can_fight_postgame(state, player) and state.has("Interior Walls Unlock", player)
    

    # Balloon Boy Shops
    multiworld.get_entrance("Backroom BB", player).access_rule = \
        lambda state: state.has("Backroom BB", player)
    
    multiworld.get_location("Restrooms - Beta Party Hat", player).access_rule = \
        lambda state: can_fight_earlygame(state, player)
    multiworld.get_entrance("Restrooms BB", player).access_rule = \
        lambda state: state.can_reach("Restrooms - Beta Party Hat", 'Location', player) and state.has("Restrooms BB", player)
    
    multiworld.get_location("Supply Closet - Gamma Party Hat", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_entrance("Supply Closet BB", player).access_rule = \
        lambda state: state.can_reach("Supply Closet - Gamma Party Hat", 'Location', player) and state.has("Supply Closet BB", player)

    multiworld.get_location("East Hall Corner - Omega Party Hat", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    multiworld.get_entrance("East Hall Corner BB", player).access_rule = \
        lambda state: state.can_reach("East Hall Corner - Omega Party Hat", 'Location', player) and state.has("East Hall Corner BB", player)
    
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
    multiworld.get_location("Show Stage - Chest Left", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("Show Stage - Chest Right", player).access_rule = \
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
    multiworld.get_location("Dining Area - Trade Beta Voucher", player).access_rule = \
        lambda state: can_fight_earlygame(state, player)
    multiworld.get_location("Dining Area - Trade Gamma Voucher", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    
    multiworld.get_location("Dining Area - Trade Omega Voucher", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    
    multiworld.get_location("Dining Area - Trade Hearts Voucher", player).access_rule = \
        lambda state: can_fight_postgame(state, player)
    multiworld.get_location("Dining Area - Trade Spades Voucher", player).access_rule = \
        lambda state: can_fight_postgame(state, player)
    multiworld.get_location("Dining Area - Trade Clubs Voucher", player).access_rule = \
        lambda state: can_fight_postgame(state, player)
    multiworld.get_location("Dining Area - Trade Diamonds Voucher", player).access_rule = \
        lambda state: can_fight_postgame(state, player)

    
    # Win Condition
    multiworld.completion_condition[player] = lambda state: state.can_reach("Office - Golden Freddy", 'Location', player)
