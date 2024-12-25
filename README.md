# Five Nights at F***boy's: Final Mix Archipelago Randomizer
 This is a mod for Five Night's at F***boy's that targets the Archipelago Multiworld Randomizer.
 The apworld code is heavily based on [Phar's work for Rogue Legacy](https://github.com/ArchipelagoMW/Archipelago/tree/main/worlds/rogue_legacy), as I'm new to coding and am still somewhat trying to make sense of this stuff personally.
 The game mod itself is using the [RPGMaker-VX-Ace-AP](https://github.com/EggonHub/RPGMaker-VX-Ace-AP) project by [EggonHub](https://github.com/EggonHub) to communicate with AP.

 Do note that this game is not, and never will be, supported by the main Archipelago team.
 This game is not permitted to be run or discussed in the official Archipelago Discord servers under any circumstances.

# Changes to base game of FNaFB1
 Some changes were made to make playing this randomizer a more seamless experience. Here's what you need to know.
 - Characters, Weapons, Armors, Key Items, and B.B. Shops have been shuffled into the item pool to find.
 - The Kingly/Godly Weapons have been removed from the RNG drops in place of Vouchers to be traded in on the Show Stage for checks (if enabled in the player's YAML).
 - The B.B. Shops each have a different amount of items for sale to send out to AP.
     - Backroom B.B. has 6
     - Restrooms B.B. has 8
     - Supply Closet B.B. has 10
     - East Hall Corner B.B. has 12
 - Some armors that don't normally show up during typical play appear in the randomizer to spice things up a bit.
 - A Vending Machine has been enabled in the Dining Area since B.B. no longer gives standard items.
 - The Puppet no longer has a timer and can be fought by interacting with it in the Restrooms.
 - Interior Walls will only open if the "Reveal Interior Walls" item has been recieved by the player.
 - The door to The Office requires 4 Key Pieces to be obtained before you're allowed to enter. You must also defeat all of the cameras as normal.
  
# Changes to base game of FNaFB2
 - Every change from FNaFB1 were implemented into here with a couple of differences.
 - Real Weapons have been removed from the RNG drops for vouchers if the setting is enabled.
 - B.B. Shops work the same as the FNaFB1 AP with the order being Main Hall B.B., Party Room 3 B.B., Kid's Cove B.B., Office B.B.
 - Both First and Second Puppet can be fought by interacting with it in either the Show Stage or the Women's Bathroom
 - The door to the Cave of the Past requires 4 B.B.'s Essence.
 - Mangle will no longer prevent you from shattering your masculinity before you enter the Women's Bathroom.
 - Toy Bonnie will still appear in the right vent if you get Toy Bonnie before you talk/free him.
 - Shadow Bonnie bossfight will appear if you have toy animatronics in your party, but they will be removed before you fight it.
 - Cake Minigame has been reduced to 10 times to feed the kid from 100.
 - The final cassette will no longer auto warp you to the rap god. There is another cassette in the bottom right corner of the Office for you to fight the rap god.

# APWorld Setup
 This randomizer uses [Archipelago](https://github.com/ArchipelagoMW/Archipelago) to handle seed generation.
 Do note that this game cannot be generated on the website, it must be done locally.
 To generate a game for Five Nights at Fuckboy's in Archipelago, you must do the following.
 - Download and install the Archipelago software from [their Releases page](https://github.com/ArchipelagoMW/Archipelago/releases/tag/0.5.0).
 - Download the latest APWorld and YAML files for FNaFB from [our Releases page](https://github.com/Scrungip/FNaFBAP/releases).
 - Open the Archipelago launcher and click "Install APWorld". Select the fnafb1.apworld you downloaded.
 - Open the provided template YAML and modify the settings to your liking.
 - All further instructions can be seen in the [official Archipelago Setup Guide](https://archipelago.gg/tutorial/Archipelago/setup/en#on-your-local-installation).

# Game Setup
 After a game has been generated and a room has been created, you may set up your game client.
 Setup for the Game Client is as follows.
 - Download and extract the latest version of Five Nights at Fuckboy's Archipelago from [our Releases page](https://github.com/Scrungip/FNaFBAP/releases).
 - Open mkxp.json in your text editor of choice. The instructions for that file are within.
 - Open Start Game.bat and begin playing whenever you and your group are ready.
 - It is HIGHLY recommended to have the Archipelago Text Client open alongside your game, as there are currently no indicators when you receive an item.
