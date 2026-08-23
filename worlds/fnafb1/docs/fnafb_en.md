# Five Nights at Fuckboy's Setup Guide

## Required Software

- Five Nights at Fuckboy's Archipelago from the
  [Five Nights at Fuckboy's Archipelago Releases Page](https://github.com/Scrungip/FNaFBAP/releases/latest)
- [RPGMaker VX Ace's RTP](https://www.rpgmakerweb.com/run-time-package)

## Configuring your YAML file

### What is a YAML file and why do I need one?

Your YAML file contains a set of configuration options which provide the generator with information about how it should
generate your game. Each player of a multiworld will provide their own YAML file. This setup allows each player to enjoy
an experience customized for their taste, and different players in the same multiworld can all have different options.

### Where do I get a YAML file?

You can customize your options by visiting the [Five Nights at Fuckboy's Options Page](/games/Five%20Nights%20at%20Fuckboy%27s/player-options).

### Connect to the MultiServer

If you use a different install directory than the default for the RPGMaker VX Ace RTP, you'll want to edit this game's `mkxp.json` file to match your local install, the entry is at the bottom.

Open the game using Start_Game.bat, or open the game with the `debug` launch command. This will enable the developer console, which you need to connect to the multiworld. After this, simply start a new game and connection instructions will be given to you.
