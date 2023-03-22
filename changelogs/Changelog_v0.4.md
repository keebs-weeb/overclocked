# Changelog v0.4

- [Changelog v0.4](#changelog-v04)
  - [Gameplay Changes](#gameplay-changes)
    - [Starting Gameplay](#starting-gameplay)
    - [The Game](#the-game)
    - [Player Interaction](#player-interaction)
    - [Mods](#mods)
    - [Players, Monsters, Bosses, and Dice](#players-monsters-bosses-and-dice)
    - [System Settings](#system-settings)
  - [Cards](#cards)
    - [Players](#players)
      - [Swordsman](#swordsman)
      - [Ranger](#ranger)
      - [Barbarian](#barbarian)
      - [Mage](#mage)
    - [Mods](#mods-1)
      - [Gameplay](#gameplay)
      - [Cheat](#cheat)
      - [Virus](#virus)
    - [System Settings](#system-settings-1)
    - [Monsters](#monsters)
    - [Bosses](#bosses)

## Gameplay Changes
### Starting Gameplay
```
- Players now draw 5 System Settings cards to begin with
- Players now draw 3 Gameplay mod cards to begin with (Redraw a new card if you draw a Virus or Cheat mod)
```
### The Game
```
- 'The Game' board is now 50 spaces long
- 'The Game' board now has dedicated Boss monsters on each space
- Frequency and amount of Action spaces has been adjusted
```
### Player Interaction
```
- To interact with any other player's computer, no additional cards are needed
- Players always have the choice to install mods and System Settings on ANY computer during their Maintenance Phase
- Playing cards on another's computers costs 1 Bandwidth + the cost of the card being played
```
### Mods
```
- Adjusted the layout of Mod cards
- Added specific values for bandwidth cost for each mod
```

### Players, Monsters, Bosses, and Dice
```
- Players and enemies all have their base numeric values reduced.  This is to promote not needing to do so much math, and will break down into simply 'cylces' of how many turns a player has to defeat certain enemies
- Player movement and damage has been stunted quite severly as a result, only being able to roll a d6 instead of a d12
```

### System Settings
```
- Removed all player interaction System Settings (Youtube Tutorial, Scriptkiddie, Metasploit, etc)
```

----
## Cards
### Players
#### Swordsman
```
Base:
	Health: 4
	Movement: 1d6 + 1
	Damage: 1d6 + 0
Level Up:
	Health: +1
	Movement: +2
	Damage: +1
```
#### Ranger
```
Base:
	Health: 3
	Movement: 1d6 + 2
	Damage: 1d6 + 0
Level Up:
	Health: +1
	Movement: +3
	Damage: +1
```
#### Barbarian
```
Base:
	Health: 5
	Movement: 1d6 + 0
	Damage: 1d6 + 0
Level Up:
	Health: +2
	Movement: +1
	Damage: +0
```
#### Mage
```
Base:
	Health: 3
	Movement: 1d6 + 1
	Damage: 1d6 + 0
Level Up:
	Health: +0
	Movement: +1
	Damage: +3
```
----

### Mods
#### Gameplay
Armor Overhaul
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    +1 To Health
Buggy Effect:
    +1 To Health
    -1 To Movement
```
Better AI
```
Type: Gameplay
Clean Installed Value: 3
Clean Bandwidth Cost: 2
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    +2 Coins Collected from Enemies
    +2 To Movement
    -1 To Health
Buggy Effect:
    +2 Coins Collected from Enemies
    -1 To Health
```
Better UI
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    +1 To Movement
    +1 To Damage
Buggy Effect:
    +1 To Movement
    -1 To Damage
```
Better Vendors
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 5
Buggy Bandwidth Cost: 3
Clean Effect: 
    -1 To Card Cost
Buggy Effect:
    -2 To Card Cost
```
Big Heads
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    +1 To Health
    +1 To Damage
Buggy Effect:
    +1 To Health
    -1 To Damage
```
Bigger Weapons
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    +2 To Damage
    -1 To Movement
Buggy Effect:
    +2 To Damage
    -2 To Movement
```
Consumable Items Overhaul
```
Type: Gameplay
Clean Installed Value: 3
Clean Bandwidth Cost: 2 
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    When a 'Buff' Active Effect would come into effect, you may place it onto this card. That effect does not go away until this mod is uninstalled.
Buggy Effect:
    When a 'Nerf' Active Effect would come into effect, place it onto this card. That effect does not go away until this mod is uninstalled.
```
Controller Remapping
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    +2 To Movement
Buggy Effect:
    +1 To Movement
    -1 To Damage
```
Corporate Branding
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 4
Buggy Bandwidth Cost: 2
Clean Effect: 
    +2 Coins at the start of each maintenance phase
Buggy Effect:
    +2 Coins at the start of each maintenance phase
```
Custom Terrain
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect:
    +2 Movement
Buggy Effect:
    +1 Movement
```
Date NPCs
```
Type: Gameplay
Clean Installed Value: 5
Clean Bandwidth Cost: 3
Buggy Installed Value: 5
Buggy Bandwidth Cost: 3
Clean Effect:
    +3 To Health
    +2 To Movement
    +1 To Damage
    +1 To Card Cost
Buggy Effect:
    +1 To Health
    +1 To Movement
    +2 To Card Cost
```
Difficulty Patch
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    +3 To Movement
    +5 Coins Collected from Enemies
    -2 To Damage
Buggy Effect:
    +3 To Movement
    -2 To Damage
```
First Person Mode
```
Type: Gameplay
Clean Installed Value: 1
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    +1 To Damage
Buggy Effect:
    +1 To Damage
```
Furry Mod
```
Type: Gameplay
Clean Installed Value: 5
Clean Bandwidth Cost: 3
Buggy Installed Value: 4
Buggy Bandwidth Cost: 2
Clean Effect:
    +3 To Health
    +3 To Movement
    +1 To Card Cost
Buggy Effect:
    +1 To Health
    +1 To Movement
    +2 To Card Cost
```
HD Music Pack
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 4
Buggy Bandwidth Cost: 2
Clean Effect: 
    -1 To Card Cost
Buggy Effect:
    -1 To Card Cost
```
HD Texture Pack
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 4
Buggy Bandwidth Cost: 2
Clean Effect: 
    -1 To Card Cost
Buggy Effect:
    -1 To Card Cost
```
Lore Update
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    +1 To Damage
    -1 To Movement
Buggy Effect:
    -1 To Movement
```
Lower Resolution Support
```
Type: Gameplay
Clean Installed Value: 1
Clean Bandwidth Cost: 1
Buggy Installed Value: 1
Buggy Bandwidth Cost: 1
Clean Effect: 
    +1 To Movement
Buggy Effect:
    +1 To Movement
    -1 To Damage
```
Modern Weapons
```
Type: Gameplay
Clean Installed Value: 4
Clean Bandwidth Cost: 2
Buggy Installed Value: 4
Buggy Bandwidth Cost: 2
Clean Effect: 
    +5 To Damage
    -3 To Movement
Buggy Effect:
    +1 To Damage
    -2 To Movement
```
Multiclass
```
Type: Gameplay
Clean Installed Value: 3
Clean Bandwidth Cost: 2
Buggy Installed Value: 5
Buggy Bandwidth Cost: 2
Clean Effect: 
    Choose a stat: Increase that by +1 Per Level (Stats are Health, Movement, and Damage)
    All other stats are decreased by -1
Buggy Effect:
    Choose a stat: Increase that by +1 Per Level (Stats are Health, Movement, and Damage)
    All other stats are decreased by -1
```
No UI
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    +2 To Movement
    +1 To Health
Buggy Effect:
    +1 To Movement
```
No Weapons
```
Type: Gameplay
Clean Installed Value: 1
Clean Bandwidth Cost: 1
Buggy Installed Value: 1
Buggy Bandwidth Cost: 1
Clean Effect: 
    +4 To Movement
    -1 To Damage
Buggy Effect:
    +2 To Movement
    -2 To Damage
```
Nude Mod
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect:
    +4 To Movement
    -1 To Health
Buggy Effect:
    +1 To Movement
    -1 To Health
```
Player Skins
```
Type: Gameplay
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    +1 To Damage
    +1 To Health
    +1 To Card Cost
Buggy Effect:
    +1 To Card Cost
```
Randomizer
```
Type: Gameplay
Clean Installed Value: 0
Clean Bandwidth Cost: 1
Buggy Installed Value: 1
Buggy Bandwidth Cost: 1
Clean Effect: 
    When rolling for damage or movement, roll twice and take the higher value
    When rolling for anything else, roll twice and take the lower value
Buggy Effect:
    When rolling for damage and movement, roll twice and take the lower value
    +1 To Health
```
Revamped Sidequests
```
Type: Gameplay
Clean Installed Value: 3
Clean Bandwidth Cost: 2
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    When you would draw an Event card, draw an additional one
    +1 To Health
Buggy Effect:
    +1 To Health
    +1 To Card Cost
```
Third Person Mode
```
Type: Gameplay
Clean Installed Value: 1
Clean Bandwidth Cost: 1
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Clean Effect: 
    +1 To Movement
Buggy Effect:
    +1 To Health
```

#### Cheat
Difficulty Reduction
```
Type: Cheat
Clean Installed Value: 5
Clean Bandwidth Cost: 3
Buggy Installed Value: 3
Buggy Bandwidth Cost: 2
Clean Effect: 
    +4 To Health
    +5 To Movement
Buggy Effect:
    +1 To Health
    +1 To Movement
    +2 To Card Cost
```
Infinite Money
```
Type: Cheat
Clean Installed Value: 5
Clean Bandwidth Cost: 3
Buggy Installed Value: 4
Buggy Bandwidth Cost: 2
Clean Effect: 
    Can draw 1 Mod and System Setting card for free each turn
Buggy Effect:
    Can draw 1 Mod and System Setting card for free each turn
    Can't Install 'Firewall' System Settings
```
Quicksaves
```
Type: Cheat
Clean Installed Value: 4
Clean Bandwidth Cost: 2
Buggy Installed Value: 3
Buggy Bandwidth Cost: 2
Mod Effect: 
    Always checkpoint in front of bosses
Buggy Effect:
    Always checkpoint in front of bosses
    Upon player defeat, lose half your 'reliable' coins (Rounded Down)
```
Speedhack
```
Type: Cheat
Clean Installed Value: 5
Clean Bandwidth Cost: 3
Buggy Installed Value: 4
Buggy Bandwidth Cost: 2
Mod Effect: 
    +10 To Movement
Buggy Effect:
    +3 To Movement
    -2 To Damage
```
Extra Lives
```
Type: Cheat
Clean Installed Value: 4
Clean Bandwidth Cost: 2
Buggy Installed Value: 2
Buggy Bandwidth Cost: 1
Mod Effect: 
    Once per fight, upon player death, ignore it and heal to full instead
Buggy Effect:
    Once per fight, upon player death, ignore it and heal to full instead
    -2 To Health
    -2 To Movement
```
God Mode
```
Type: Cheat
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 4
Buggy Bandwidth Cost: 2
Mod Effect: 
    Ignore all Gameplay and Cheat mod reductions to your health
Buggy Effect:
    Ignore all Gameplay and Cheat mod reductions to your health
```
Debug Console
```
Type: Cheat
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 4
Buggy Bandwidth Cost: 2
Mod Effect: 
    Ignore all Gameplay and Cheat mod reductions to your damage
Buggy Effect:
    Ignore all Gameplay and Cheat mod reductions to your damage
```
Noclip
```
Type: Cheat
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Buggy Installed Value: 4
Buggy Bandwidth Cost: 2
Mod Effect: 
    Ignore all Gameplay and Cheat mod reductions to your movement
Buggy Effect:
    Ignore all Gameplay and Cheat mod reductions to your movement
```

#### Virus
Anti-Cheat Rootkit
```
Type: Virus
Clean Installed Value: 2
Clean Bandwidth Cost: 1
Mod Effect: 
    -1 To Health per Cheat Installed
    -1 To Damage per Cheat Installed
    -1 To Movement per Cheat Installed
    Can only be uninstalled by 'Antivirus' System Setting
```
BonziBuddy
```
Type: Virus
Installed Value: 1
Bandwidth Cost: 1
Mod Effect:
    At the end of each turn, discard a System Setting card from your hand
    Can only be uninstalled by 'Antivirus' System Setting
```
CryptoLocker
```
Type: Virus
Installed Value: 2
Bandwidth Cost: 1
Mod Effect: 
    Cannot install or uninstall Mods unless a card effect makes you.
    Can only be uninstalled by 'Antivirus' System Setting
```
Cryptominer
```.
Type: Virus
Installed Value: 2
Bandwidth Cost: 1
Mod Effect:     
    Gives the owner of this card +2 coin at the beginning of your maintenance phase
    Can only be uninstalled by 'Antivirus' System Setting
```
DDoS
```
Type: Virus
Installed Value: 0
Bandwidth Cost: 1
Mod Effect: 
    You can have more than one 'DDoS' card installed
    On each of your turns, you have -1 to Bandwith
    Can only be uninstalled by 'Antivirus' System Setting
```
ILOVEYOU
```
Type: Virus
Installed Value: 1
Bandwidth Cost: 1
Mod Effect:
    At the end of your maintenance phase, randomly uninstall one Mod. This effect can uninstall this mod
    Can only be uninstalled by 'Antivirus' System Setting
```
Meltdown
```
Type: Virus
Installed Value: 3
Bandwidth Cost: 2
Mod Effect: 
    Can be installed on computers with 'Firewall' active
    Can only be uninstalled by 'Antivirus' System Setting
```
Memory Leak
```
Type: Virus
Installed Value: 1
Bandwidth Cost: 1
Mod Effect: 
    At the start of your maintenance phase, double this card's Installed Value cost
    Can only be uninstalled by 'Antivirus' System Setting
```
Pirated Game
```
Type: Virus
Installed Value: 5
Bandwidth Cost: 3
Mod Effect: 
    Can only be uninstalled by 'Antivirus' System Setting
```
Spectre
```
Type: Virus
Installed Value: 3
Bandwidth Cost: 2
Mod Effect: 
    Can be installed on computers with 'Firewall' active
    Can only be uninstalled by 'Antivirus' System Setting
```
Spyware
```
Type: Virus
Installed Value: 0
Bandwidth Cost: 1
Mod Effect: 
    The original owner of this can play 1 System Settings card from your hand during their turn
    Can only be uninstalled by 'Antivirus' System Setting
```
Stuxnet
```
Type: Virus
Installed Value: 2
Bandwidth Cost: 1
Mod Effect: 
    At the end of your maintenance phase, flip a coin. On heads, install this Mod on the previous player's computer. This action happens without need for any other effects. This action cannot happen if the previous player is 'Offline' or has a 'Firewall' active.
    Can only be uninstalled by 'Antivirus' System Setting
```

### System Settings
Metasploit (REMOVED)
Remote Access Tool (REMOVED)
Scriptkiddie (REMOVED)
YouTube Hacking Tutorial (REMOVED)

### Monsters
Bird Man
```
	Health: 7
	Damage: 1
    Zone: 1
	Rewards: 3 Coins
```
Scorpion
```
	Health: 2
	Damage: 6
    Zone: 1
	Rewards: 5 Coins
```
Zombie
```
	Health: 4
	Damage: 1
    Zone: 1
	Rewards: 2 Coins
```
Ghost
```
	Health: 9
	Damage: 1
    Zone: 2
	Rewards: 5 Coins
```
Necromancer
```
	Health: 6
	Damage: 2
    Zone: 2
	Rewards: 5 Coins
```
Royal Archer
```
	Health: 14
	Damage: 2
    Zone: 2
	Rewards: 7 Coins
```
Royal Knight
```
	Health: 12
	Damage: 2
    Zone: 3
	Rewards: 8 Coins
```
Ogre
```
	Health: 12
	Damage: 3
    Zone: 3
	Rewards: 7 Coins
```
Baby Drake
```
	Health: 18
	Damage: 3
    Zone: 3
	Rewards: 10 Coins
```


### Bosses
Rogue Warrior
```
Level 1 Boss
Health: 13
Damage: 1
Rewards: 10 Coins
Defeat: 
```
Very Large Fish
```
Level 2 Boss
Health: 23
Damage: 1
Rewards: Draw 3 Event Cards. For each card, you may choose to active it's effects, or discard it.
Defeat: 
```
Demon
```
Level 3 Boss
Health: 18
Damage: 2
Rewards: 15 Coins
Defeat: 
```
Maddened Mage
```
Level 4 Boss
Health: 11
Damage: 4
Rewards: 20 Coins
Defeat: 
```
Dragon
```
Level 5 Boss
Health: 25
Damage: 3
Rewards: Win The Game
Defeat: 
```