from BaseClasses import CollectionState, MultiWorld, Location, Region, Item
from .Regions import connect_regions
from Options import Toggle

def party_count(state: CollectionState, player: int) -> int:
    return (
        state.count("Toy Bonnie", player)
        + state.count("Toy Chica", player) 
        + state.count("Mangle", player)
        + state.count("Withered Freddy", player)
        + state.count("Withered Bonnie", player)
        + state.count("Withered Chica", player)
        + state.count("Withered Foxy", player)
        + 1 # Toy Freddy
        )

# Check if the player has the party members before adding their power to the calculation
def attack_power(state: CollectionState, player: int) -> int:
    return (
    state.count("Progressive Microphone", player)
    + state.count("Toy Bonnie", player) * state.count("Progressive Guitar", player)
    + state.count("Toy Chica", player) * max((state.count("Progressive Cupcakes", player) - 1), 0) # -1 for the first cupcake
    + state.count("Mangle", player) * state.count("Progressive Hook", player)
    # Withered Animatronics start with Kingly Weapons
    + state.count("Withered Freddy", player) * 5
    + state.count("Withered Bonnie", player) * 5
    + state.count("Withered Chica", player) * 5
    + state.count("Withered Foxy", player) * 5
    )

# This one's a bit of a mess, might have to rethink it at a later time
def skills(state: CollectionState, player: int) -> int:
    return (
        (
            state.count("Progressive Tophat Slash", player)
            + state.count("Progressive Tophat Dash", player)
            + state.count("Progressive Tophat Crash", player)
            + state.count("Progressive Tophat Smash", player)
        ) 
        + state.count("Toy Bonnie", player) * (
            state.count("Grab Bag", player)
            + state.count("Status Bomb", player)
            + state.count("Spread Bomb", player)
        )
        + state.count("Toy Chica", player) * (
            state.count("Healing Wing", player)
            + state.count("Curing Wing", player)
            + state.count("Raising Wing", player)
            + state.count("Recovery Wing", player)
        )
        + state.count("Mangle", player) * (
            state.count("Electroshock", player)
            + state.count("Paravolt", player)
            + state.count("Somnojolt", player)
            + state.count("Lightningbolt", player)
        )
        # Withered Animatronics start with 3 skills
        + state.count("Withered Freddy", player) * 3
        + state.count("Withered Bonnie", player) * 3
        + state.count("Withered Chica", player) * 3
        + state.count("Withered Foxy", player) * 3
    )

# Endoskeletons provide more defense so we should treat it as such
def total_defense(state: CollectionState, player: int) -> int:
    return (
        (1 + state.count("Toy Bonnie", player) + state.count("Toy Chica", player) + state.count("Mangle", player)) * (
            state.count("Progressive Body Endoskeletons", player) * 4
            + state.count("Progressive Head Endoskeletons", player) * 4
            + state.count("Progressive Pizza Shields", player)
            + state.count("Progressive Caffeine Sodas", player)
        )
        # Each Withered starts with best defense items
        + state.count("Withered Freddy", player) * 40
        + state.count("Withered Bonnie", player) * 40
        + state.count("Withered Chica", player) * 40
        + state.count("Withered Foxy", player) * 40
    )


def can_fight_earlygame(state: CollectionState, player: int) -> bool:
    return (
        attack_power(state, player) >= 1
        and total_defense(state, player) >= 4 
        and skills(state, player) >= 1
    )


def can_fight_midgame(state: CollectionState, player: int) -> bool:
    return (
        attack_power(state, player) >= 3 
        and total_defense(state, player) >= 8
        and party_count(state, player) >= 2
        and skills(state, player) >= 2
    )

def can_fight_almostlategame(state: CollectionState, player: int) -> bool:
    return (
        attack_power(state, player) >= 10
        and total_defense(state, player) >= 20
        and party_count(state, player) >= 3
        and skills(state, player) >= 4
    )

def can_fight_lategame(state: CollectionState, player: int) -> bool:
    return (
        attack_power(state, player) >= 24
        and total_defense(state, player) >= 160
        and party_count(state, player) >= 4
        and skills(state, player) >= 20
    )


def can_fight_endgame(state: CollectionState, player: int) -> bool:
    return (
        attack_power(state, player) >= 40
        and total_defense(state, player) >= 300
        and party_count(state, player) >= 8
        and skills(state, player) >= 25
    )


def set_rules(multiworld: MultiWorld, player: int):
    # Bosses
    multiworld.get_location("Party Room 4 - Withered Foxy", player).access_rule = \
        lambda state: can_fight_midgame(state, player)

    # You can only fight Splash Woman with toy freddy
    multiworld.get_location("Women's Bathroom - Splash Woman", player).access_rule = \
        lambda state: (
            (state.count("Progressive Tophat Slash", player)
            + state.count("Progressive Tophat Dash", player)
            + state.count("Progressive Tophat Crash", player)
            + state.count("Progressive Tophat Smash", player)) >= 1
            and state.count("Progressive Microphone", player) >= 2
            and state.count("Progressive Body Endoskeletons", player) >= 1
            and state.count("Progressive Head Endoskeletons", player) >= 1
            and state.count("Progressive Pizza Shield", player) >= 1
            and state.count("Progressive Caffeine Sodas", player) >= 1
        )

    multiworld.get_location("The Puppet", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    multiworld.get_location("The Puppet - Rod of Femininity A", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    multiworld.get_location("Party Room 1 - Withered Bonnie", player).access_rule = \
        lambda state: can_fight_lategame(state, player) and state.has("Toy Bonnie", player)
    multiworld.get_location("Party Room 2 - Withered Chica", player).access_rule = \
        lambda state: can_fight_lategame(state, player) and state.has("Toy Chica", player)
    multiworld.get_location("Party Room 3 - Withered Freddy", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    multiworld.get_location("Party Room 4 - Withered Foxy Rematch", player).access_rule = \
        lambda state: can_fight_lategame(state, player) and state.has("Mangle", player)
    multiworld.get_location("The Second Puppet", player).access_rule = \
        lambda state: can_fight_endgame(state, player)
    multiworld.get_location("The Second Puppet - Rod of Femininity B", player).access_rule = \
        lambda state: can_fight_endgame(state, player)
    multiworld.get_location("Boss Rush", player).access_rule = \
        lambda state: can_fight_endgame(state, player)
    # Shops
    multiworld.get_location("Kid's Cove - Protection Hat", player).access_rule = \
        lambda state: can_fight_almostlategame(state, player)
    multiworld.get_location("Main Hall - Protection Hat", player).access_rule = \
        lambda state: can_fight_earlygame(state, player)
    multiworld.get_location("Party Room 3 - Protection Hat", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("Office - Protection Hat", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    
    # Cameras
    multiworld.get_location("Show Stage - Camera", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("Game Room - Camera", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("Prize Corner - Camera", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("Main Hall - Camera", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("Kid's Cove - Camera", player).access_rule = \
        lambda state: can_fight_almostlategame(state, player)
    multiworld.get_location("Parts/Service - Camera", player).access_rule = \
        lambda state: can_fight_almostlategame(state, player)
    multiworld.get_location("Office - Camera", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    multiworld.get_location("Left Vent - Camera", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    multiworld.get_location("Right Vent - Camera", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    multiworld.get_location("Party Room 1 - Camera", player).access_rule = \
        lambda state: can_fight_almostlategame(state, player)
    multiworld.get_location("Party Room 2 - Camera", player).access_rule = \
        lambda state: can_fight_almostlategame(state, player)
    multiworld.get_location("Party Room 3 - Camera", player).access_rule = \
        lambda state: can_fight_midgame(state, player)
    multiworld.get_location("Party Room 4 - Camera", player).access_rule = \
        lambda state: can_fight_almostlategame(state, player)

    # General
    multiworld.get_location("Show Stage - Lucky Soda Chest", player).access_rule = \
        lambda state: can_fight_almostlategame(state, player)
    multiworld.get_location("Show Stage - Double Pizza Chest", player).access_rule = \
        lambda state: can_fight_lategame(state, player)
    multiworld.get_location("Women's Bathroom - Toy Chica", player).access_rule = \
        lambda state: state.can_reach_location("Women's Bathroom - Splash Woman", player) and state.has("Progressive Cupcakes", player)
    multiworld.get_location("Right Vent - Toy Bonnie", player).access_rule = \
        lambda state: state.has("Stick", player)

    multiworld.get_location("Cave of the Past - Dragon Dildo A", player).access_rule = \
        lambda state: state.has("Stick", player)
    multiworld.get_location("Cave of the Past - Dragon Dildo B", player).access_rule = \
        lambda state: state.has("Progressive Dragon Dildo", player)
    multiworld.get_location("Cave of the Past - Dragon Dildo C", player).access_rule = \
        lambda state: state.has("Progressive Dragon Dildo", player, 2)
    multiworld.get_location("Cave of the Past - Dragon Dildo D", player).access_rule = \
        lambda state: state.has("Progressive Dragon Dildo", player, 3)
    multiworld.get_location("Cave of the Past - Dragon Dildo E", player).access_rule = \
        lambda state: state.has("Progressive Dragon Dildo", player, 4)
    multiworld.get_location("Cave of the Past - Dragon Dildo F", player).access_rule = \
        lambda state: state.has("Progressive Dragon Dildo", player, 5)

    # Story Quests
    multiworld.get_location("Turn in Sex Toy Voucher to BB", player).access_rule = \
        lambda state: state.can_reach_location("Kid's Cove - Protection Hat", player) \
            and state.has("Kid's Cove BB", player) and state.has("Sex Toy Voucher", player)
    multiworld.get_location("Kid's Cove - Return Sex Toy", player).access_rule = \
        lambda state: state.has("Sex Toy", player, 2)
    multiworld.get_location("Vending Machine - Turn in Sex Toy", player).access_rule = \
        lambda state: state.has("Sex Toy Voucher", player)

    # Enemy Trade Item Drops
    if multiworld.trade_quest[player] == Toggle.option_true:
        multiworld.get_location("Dining Area - Trade Beta Voucher", player).access_rule = \
            lambda state: can_fight_earlygame(state, player)
        multiworld.get_location("Dining Area - Trade Gamma Voucher", player).access_rule = \
            lambda state: can_fight_midgame(state, player)
        multiworld.get_location("Dining Area - Trade Delta Voucher", player).access_rule = \
            lambda state: can_fight_almostlategame(state, player)
        multiworld.get_location("Dining Area - Trade Omega Voucher", player).access_rule = \
            lambda state: can_fight_lategame(state, player)

    # Cassettes
    if multiworld.difficulty[player].value == 1:
        multiworld.get_location("Show Stage - Cassette Radar Chest", player).access_rule = \
            lambda state: can_fight_lategame(state, player)
        multiworld.get_location("Kid's Cove - Cassette", player).access_rule = \
            lambda state: state.has("Cassette Radar", player)
        multiworld.get_location("Parts/Service - Cassette", player).access_rule = \
            lambda state: state.has("Cassette Radar", player)
        multiworld.get_location("Men's Bathroom - Cassette", player).access_rule = \
            lambda state: state.has("Cassette Radar", player)
        multiworld.get_location("Women's Bathroom - Cassette", player).access_rule = \
            lambda state: state.has("Cassette Radar", player)
        multiworld.get_location("Office - Cassette", player).access_rule = \
            lambda state: state.has("Cassette Radar", player)
        multiworld.get_location("Office Hall - Cassette", player).access_rule = \
            lambda state: state.has("Cassette Radar", player)
        multiworld.get_location("Party Room 1 - Cassette", player).access_rule = \
            lambda state: state.has("Cassette Radar", player)
        multiworld.get_location("Party Room 2 - Cassette", player).access_rule = \
            lambda state: state.has("Cassette Radar", player)
        multiworld.get_location("Party Room 3 - Cassette", player).access_rule = \
            lambda state: state.has("Cassette Radar", player)
        multiworld.get_location("Party Room 4 - Cassette", player).access_rule = \
            lambda state: state.has("Cassette Radar", player)
        multiworld.get_location("Office - Rap God", player).access_rule = \
            lambda state: can_fight_endgame(state, player) and state.has("Cassette", player, 10)

    # Keystones
    multiworld.get_location("Kid's Cove - Chest", player).access_rule = \
        lambda state: can_fight_almostlategame(state, player) and state.has("Mangle", player)
    multiworld.get_location("Women's Bathroom - Chest", player).access_rule = \
        lambda state: can_fight_almostlategame(state, player) and state.has("Toy Chica", player)
    multiworld.get_location("Office - Left Chest", player).access_rule = \
        lambda state: can_fight_lategame(state, player) and state.has("Toy Bonnie", player)
    multiworld.get_location("Office - Right Chest", player).access_rule = \
        lambda state: can_fight_lategame(state, player)

    # Levelsanity
    if multiworld.levelsanity[player] == Toggle.option_true:
        for i in range(1, 21):
            if i < 6:
                multiworld.get_location(f"Toy Bonnie - Level {i}", player).access_rule = \
                    lambda state: state.has("Toy Bonnie", player)
                multiworld.get_location(f"Toy Chica - Level {i}", player).access_rule = \
                    lambda state: state.has("Toy Chica", player)
                multiworld.get_location(f"Mangle - Level {i}", player).access_rule = \
                    lambda state: state.has("Mangle", player)
            elif i < 11:
                multiworld.get_location(f"Toy Freddy - Level {i}", player).access_rule = \
                    lambda state: can_fight_earlygame(state, player)
                multiworld.get_location(f"Toy Bonnie - Level {i}", player).access_rule = \
                    lambda state: can_fight_earlygame(state, player) and state.has("Toy Bonnie", player)
                multiworld.get_location(f"Toy Chica - Level {i}", player).access_rule = \
                    lambda state: can_fight_earlygame(state, player) and state.has("Toy Chica", player)
                multiworld.get_location(f"Mangle - Level {i}", player).access_rule = \
                    lambda state: can_fight_earlygame(state, player) and state.has("Mangle", player)
            elif i < 16:
                multiworld.get_location(f"Toy Freddy - Level {i}", player).access_rule = \
                    lambda state: can_fight_midgame(state, player)
                multiworld.get_location(f"Toy Bonnie - Level {i}", player).access_rule = \
                    lambda state: can_fight_midgame(state, player) and state.has("Toy Bonnie", player)
                multiworld.get_location(f"Toy Chica - Level {i}", player).access_rule = \
                    lambda state: can_fight_midgame(state, player) and state.has("Toy Chica", player)
                multiworld.get_location(f"Mangle - Level {i}", player).access_rule = \
                    lambda state: can_fight_midgame(state, player) and state.has("Mangle", player)
            else:
                multiworld.get_location(f"Toy Freddy - Level {i}", player).access_rule = \
                    lambda state: can_fight_almostlategame(state, player)
                multiworld.get_location(f"Toy Bonnie - Level {i}", player).access_rule = \
                    lambda state: can_fight_almostlategame(state, player) and state.has("Toy Bonnie", player)
                multiworld.get_location(f"Toy Chica - Level {i}", player).access_rule = \
                    lambda state: can_fight_almostlategame(state, player) and state.has("Toy Chica", player)
                multiworld.get_location(f"Mangle - Level {i}", player).access_rule = \
                    lambda state: can_fight_almostlategame(state, player) and state.has("Mangle", player)
        
        # Failsafe is if you upgrade skill without using it 20 times, it will just send the check immediately
        multiworld.get_location("Toy Freddy - Tophat Slash LV2", player).access_rule = \
            lambda state: state.has("Progressive Tophat Slash", player)
        multiworld.get_location("Toy Freddy - Tophat Slash LVMAX", player).access_rule = \
            lambda state: state.has("Progressive Tophat Slash", player, 2)
        multiworld.get_location("Toy Freddy - Tophat Dash LV1", player).access_rule = \
            lambda state: can_fight_earlygame(state, player)
        multiworld.get_location("Toy Freddy - Tophat Dash LV2", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Progressive Tophat Dash", player)
        multiworld.get_location("Toy Freddy - Tophat Dash LVMAX", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Progressive Tophat Dash", player, 2)
        multiworld.get_location("Toy Freddy - Tophat Crash LV1", player).access_rule = \
            lambda state: can_fight_midgame(state, player)
        multiworld.get_location("Toy Freddy - Tophat Crash LV2", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Progressive Tophat Crash", player)
        multiworld.get_location("Toy Freddy - Tophat Crash LVMAX", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Progressive Tophat Crash", player, 2)
        multiworld.get_location("Toy Freddy - Tophat Smash LV1", player).access_rule = \
            lambda state: can_fight_almostlategame(state, player)
        multiworld.get_location("Toy Freddy - Tophat Smash LV2", player).access_rule = \
            lambda state: can_fight_almostlategame(state, player) and state.has("Progressive Tophat Smash", player)
        multiworld.get_location("Toy Freddy - Tophat Smash LVMAX", player).access_rule = \
            lambda state: can_fight_almostlategame(state, player) and state.has("Progressive Tophat Smash", player, 2)

        multiworld.get_location("Mangle - Electroshock", player).access_rule = \
            lambda state: state.has("Mangle", player)
        multiworld.get_location("Mangle - Paravolt", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Mangle", player)
        multiworld.get_location("Mangle - Somnojolt", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Mangle", player)
        multiworld.get_location("Mangle - Lightningbolt", player).access_rule = \
            lambda state: can_fight_almostlategame(state, player) and state.has("Mangle", player)
        
        multiworld.get_location("Toy Chica - Healing Wing", player).access_rule = \
            lambda state: state.has("Toy Chica", player)
        multiworld.get_location("Toy Chica - Curing Wing", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Toy Chica", player)
        multiworld.get_location("Toy Chica - Raising Wing", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Toy Chica", player)
        multiworld.get_location("Toy Chica - Recovery Wing", player).access_rule = \
            lambda state: can_fight_almostlategame(state, player) and state.has("Toy Chica", player)
        
        multiworld.get_location("Toy Bonnie - Grab Bag", player).access_rule = \
            lambda state: state.has("Toy Bonnie", player)
        multiworld.get_location("Toy Bonnie - Status Bomb", player).access_rule = \
            lambda state: can_fight_earlygame(state, player) and state.has("Toy Bonnie", player)
        multiworld.get_location("Toy Bonnie - Spread Bomb", player).access_rule = \
            lambda state: can_fight_midgame(state, player) and state.has("Toy Bonnie", player)
        multiworld.get_location("Toy Bonnie - Timer Flip", player).access_rule = \
            lambda state: can_fight_almostlategame(state, player) and state.has("Toy Bonnie", player)
        
        multiworld.get_location("Toy Freddy - Death Inhale", player).access_rule = \
            lambda state: state.has("Tophat Keystone", player)
        multiworld.get_location("Toy Bonnie - Terror Fever", player).access_rule = \
            lambda state: state.has("Terror Keystone", player) and state.has("Toy Bonnie", player)
        multiworld.get_location("Toy Chica - Avian Strike", player).access_rule = \
            lambda state: state.has("Avian Keystone", player) and state.has("Toy Chica", player)
        multiworld.get_location("Mangle - Disassembly", player).access_rule = \
            lambda state: state.has("Assembly Keystone", player) and state.has("Mangle", player)

    # Connect regions at rule runtime
    connect_regions(multiworld, player, "Menu", "Show Stage")
    connect_regions(multiworld, player, "Show Stage", "Kid's Cove")
    connect_regions(multiworld, player, "Show Stage", "Kid's Cove BB", lambda state: state.has("Kid's Cove BB", player))
    connect_regions(multiworld, player, "Show Stage", "Main Hall")
    if multiworld.trade_quest[player] == Toggle.option_true:
        connect_regions(multiworld, player, "Show Stage", "Trade Machine")
    if multiworld.levelsanity[player] == Toggle.option_true:
        connect_regions(multiworld, player, "Show Stage", "Levelsanity")
    connect_regions(multiworld, player, "Main Hall", "Main Hall BB", lambda state: state.has("Main Hall BB", player))
    connect_regions(multiworld, player, "Main Hall", "Men's Bathroom")
    connect_regions(multiworld, player, "Main Hall", "Women's Bathroom")
    connect_regions(multiworld, player, "Main Hall", "Parts/Service")
    connect_regions(multiworld, player, "Main Hall", "Office Hall")
    connect_regions(multiworld, player, "Office Hall", "Party Room 4")
    connect_regions(multiworld, player, "Office Hall", "Party Room 3")
    connect_regions(multiworld, player, "Party Room 3", "Party Room 3 BB", lambda state: state.has("Party Room 3 BB", player))
    connect_regions(multiworld, player, "Office Hall", "Party Room 1")
    connect_regions(multiworld, player, "Office Hall", "Party Room 2")
    connect_regions(multiworld, player, "Office Hall", "Office")
    connect_regions(multiworld, player, "Party Room 1", "Left Vent")
    connect_regions(multiworld, player, "Party Room 2", "Right Vent")
    connect_regions(multiworld, player, "Left Vent", "Office")
    connect_regions(multiworld, player, "Right Vent", "Office")
    connect_regions(multiworld, player, "Office", "Office BB", lambda state: state.has("Office BB", player))
    connect_regions(multiworld, player, "Office", "Cave of the Past", lambda state: can_fight_endgame(state, player) and state.has("BB's Essence", player, 4))
    connect_regions(multiworld, player, "Cave of the Past", "BB Giygas")
    if multiworld.Goal[player].value == 1:
        connect_regions(multiworld, player, "BB Giygas", "Refurbs")


    # Win Condition
    if multiworld.Goal[player].value == 0:
        multiworld.completion_condition[player] = lambda state: state.can_reach_location("BB Giygas", player)
    else:
        multiworld.completion_condition[player] = lambda state: state.can_reach_location("Refurbs", player)
