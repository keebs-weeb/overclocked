# Changelog v0.3

- [Changelog v0.3](#changelog-v03)
  - [Gameplay Changes](#gameplay-changes)
    - [The Game](#the-game)
    - [Mods](#mods)
    - [Computers](#computers)
    - [Event Deck](#event-deck)
  - [Cards](#cards)
    - [Computers](#computers-1)
      - [Scamdeck](#scamdeck)
      - [Hand-Me-Down](#hand-me-down)
      - [Ol' Reliable](#ol-reliable)
      - [Crackbook](#crackbook)
      - [Gaming Laptop](#gaming-laptop)
      - [Pre-Built](#pre-built)
      - [Enthusiass Desktop](#enthusiass-desktop)
    - [Mods](#mods-1)
      - [Gameplay](#gameplay)
      - [Cheat](#cheat)
      - [Virus](#virus)
    - [System Settings](#system-settings)

## Gameplay Changes
### The Game
```
- 'The Game' board now features dedicated spaces in which players can choose to stop movement on to take actions 
- When a player lands or stops on an action space, they do not draw event cards
    - Monster Spaces
        - These spaces allow the player to fight a monster from the Monster deck
        - These spaces are more frequent at the start, and less frequent as 'The Game' goes on
        - Before the second boss, these spaces occur once every 2 spaces (roughly)
        - Before the fourth boss, these spaces occur once every 6 spaces (roughly)
        - Before the final boss, these spaces occur once every 10 spaces (roughly)
    - Vendor Spaces
        - These spaces allow cards purchased during the following maintenance phase to have -1 to cost
        - These spaces occur approximately every 20 spaces
    - Treasure Spaces
        - These spaces give the players a windfall of coins
        - These spaces are very few and far between, only 2 on the game board
        - When a player lands on it, a d12 is rolled and gold is given to the player equal to the roll plus the value listed on the board
```

### Mods
```
- Mods no longer have a 'Bug Check'
- Mods now have 2 sides to them: a 'Clean' side and a 'Buggy' side
    - Mods can be installed on either side you wish
    - Mods only give the effects based on which side they are installed on
- When uninstalled, Mods are not moved to the 'Uninstalled Mods' folder, and instead are just discarded
- Only Mods in the 'Mods Folder' can be sold to 'The Forums' during your maintenance phase 
```

### Computers
```
- Computers now have less resources
- Computer traits have been changed due to changes with other gameplay elements
```

### Event Deck
```
- Event cards will no longer have monster fights in the deck
- Event cards that have active effects on them, now are classified as either 'Buff' or 'Nerf' effects
```

----
## Cards

### Computers
#### Scamdeck
```
System Resources: 10
Bandwidth: 4
Trait: Can't install virus cards
```

#### Hand-Me-Down
```
System Resources: 10
Bandwidth: 5
Trait: At the start of your maintenance, you may flip a coin. If heads, go offline until your next turn
```

#### Ol' Reliable
```
System Resources: 11
Bandwidth: 5
Trait: On system crash, flip a coin. If heads, do not revert to the last checkpoint (Still take all other actions of a system crash)
```

#### Crackbook
```
System Resources: 12
Bandwidth: 6
Trait: System Settings cost 1 coin to play on this computer
```

#### Gaming Laptop
```
System Resources: 12
Bandwidth: 6
Trait: Can only install 1 system setting at a time
```

#### Pre-Built
```
System Resources: 12
Bandwidth: 6
Trait: Interacting with other players costs 1 additional bandwidth
```

#### Enthusiass Desktop
```
System Resources: 18
Bandwidth: 8
Trait: Each turn, skip either your play phase OR your maintenance phase each turn
```
----

### Mods
#### Gameplay
Armor Overhaul
```
Type: Gameplay
Installed Value: 2
Clean Effect: 
    +3 To Health
    -1 To Movement
Buggy Effect:
    +1 To Health
    -1 To Movement
    -1 To Damage
```
Better AI
```
Type: Gameplay
Installed Value: 3
Clean Effect: 
    +2 Coins Collected from Enemies
    +2 To Movement
    +1 Enemy Damage
Buggy Effect:
    +2 Coins Collected from Enemies
    +1 Enemy Damage
    -2 To Movement
```
Better UI
```
Type: Gameplay
Installed Value: 2
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
Installed Value: 2
Clean Effect: 
    -1 To Card Cost
Buggy Effect:
    -2 To Card Cost
    +2 To Installed Value
```
Big Heads
```
Type: Gameplay
Installed Value: 2
Clean Effect: 
    +3 To Movement
    +2 To Enemy Damage
Buggy Effect:
    +2 To Enemy Damage
```
Bigger Weapons
```
Type: Gameplay
Installed Value: 2
Clean Effect: 
    +3 To Damage
    -2 To Movement
Buggy Effect:
    +2 To Damage
    -3 To Movement
```
Consumable Items Overhaul
```
Type: Gameplay
Installed Value: 3
Clean Effect: 
    When a 'Buff' Active Effect would come into effect, you may place it onto this card. That effect does not go away until this mod is uninstalled.
Buggy Effect:
    When a 'Nerf' Active Effect would come into effect, place it onto this card. That effect does not go away until this mod is uninstalled.
```
Controller Remapping
```
Type: Gameplay
Installed Value: 2
Clean Effect: 
    +3 To Movement
    -1 To Damage
Buggy Effect:
    +1 To Movement
    -1 To Damage
```
Corporate Branding
```
Type: Gameplay
Installed Value: 2
Clean Effect: 
    +2 Coins at the start of each maintenance phase
Buggy Effect:
    +2 Coins at the start of each maintenance phase
    +1 To Installed Value
```
Custom Terrain
```
Type: Gameplay
Installed Value: 2
Clean Effect:
    +2 Movement
    +1 Enemy Damage
Buggy Effect:
    +1 Movement
    +1 Enemy Damage
```
Date NPCs
```
Type: Gameplay
Installed Value: 4
Clean Effect:
    +1 To Health
    +1 To Movement
    +2 To Damage
    +1 To Card Cost
Buggy Effect:
    +1 To Health
    +1 To Movement
    +1 To Damage
    +2 To Card Cost
```
Difficulty Patch
```
Type: Gameplay
Installed Value: 2
Clean Effect: 
    +3 To Movement
    +5 Coins Collected from Enemies
    +3 To Enemy Health
    +1 To Enemy Damage
Buggy Effect:
    +2 To Movement
    +2 To Enemy Health
    +2 To Enemy Damage
```
First Person Mode
```
Type: Gameplay
Installed Value: 1
Clean Effect: 
    +1 To Damage
Buggy Effect:
    +1 To Damage
    +1 To Installed Value
```
Furry Mod
```
Type: Gameplay
Installed Value: 4
Clean Effect:
    +2 To Health
    +4 To Movement
    +2 To Card Cost
Buggy Effect:
    +2 To Health
    +2 To Card Cost
    +1 To Enemy Damage
```
HD Music Pack
```
Type: Gameplay
Installed Value: 2
Clean Effect: 
    -1 To Mod Cost
Buggy Effect:
    -1 To Mod Cost
    +1 To Installed Value
```
HD Texture Pack
```
Type: Gameplay
Installed Value: 2
Clean Effect: 
    -1 To Mod Cost
Buggy Effect:
    -1 To Mod Cost
    +1 To Installed Value
```
Lore Update
```
Type: Gameplay
Installed Value: 2
Clean Effect: 
    +2 To Damage
    -1 To Movement
Buggy Effect:
    -1 To Movement
```
Lower Resolution Support
```
Type: Gameplay
Installed Value: 1
Clean Effect: 
    +1 To Movement
Buggy Effect:
    +1 To Enemy Health
```
Modern Weapons
```
Type: Gameplay
Installed Value: 4
Clean Effect: 
    +5 To Damage
    -2 To Movement
Buggy Effect:
    +2 To Damage
    -1 To Movement
```
Multiclass
```
Type: Gameplay
Installed Value: 3
Clean Effect: 
    Choose a stat: Increase that by +2 Per Level (Stats are Health, Movement, and Damage)
    All other stats are decreased by -3
Buggy Effect:
    Choose a stat: Increase that by +1 Per Level (Stats are Health, Movement, and Damage)
    All other stats are decreased by -3
```
No UI
```
Type: Gameplay
Installed Value: 2
Clean Effect: 
    +2 To Movement
    -1 To Damage
Buggy Effect:
    -1 To Damage
```
No Weapons
```
Type: Gameplay
Installed Value: 1
Clean Effect: 
    +3 To Movement
    -2 To Damage
Buggy Effect:
    +1 To Movement
    -1 To Damage
```
Nude Mod
```
Type: Gameplay
Installed Value: 2
Clean Effect: 
    +2 Coins Collected from Enemies
    +1 To Movement
    +2 To Enemy Damage
Buggy Effect:
    +1 Coins Collected from Enemies
    +2 To Enemy Damage
```
Player Skins
```
Type: Gameplay
Installed Value: 1
Clean Effect: 
    +2 To Damage
    +1 To Card Cost
Buggy Effect:
    +1 To Card Cost
```
Randomizer
```
Type: Gameplay
Installed Value: 0
Clean Effect: 
    When rolling for damage or movement, roll twice and take the higher value
    When rolling for anything else, roll twice and take the lower value
Buggy Effect:
    When rolling for anything besides damage and movement, roll twice and take the lower value
```
Revamped Sidequests
```
Type: Gameplay
Installed Value: 3
Clean Effect: 
    When you would draw an Event card, draw an additional one
    +2 To Movement
Buggy Effect:
    +1 To Movement
    +1 To Card Cost
```
Third Person Mode
```
Type: Gameplay
Installed Value: 1
Clean Effect: 
    +1 To Movement
Buggy Effect:
    -1 To Movement
```

#### Cheat
Cheat Engine (REMOVED)
```
REMOVED
```
Infinite Money
```
Type: Cheat
Installed Value: 6
Clean Effect: 
    Can draw 1 Mod or System Setting card for free each turn
Buggy Effect:
    Can draw 1 Mod or System Setting card for free each turn
    Can't Install 'Firewall' System Settings
```
Quicksaves
```
Type: Cheat
Installed Value: 4
Mod Effect: 
    Always checkpoint in front of bosses
Buggy Effect:
    Always checkpoint in front of bosses
    Upon player defeat, lose half your 'reliable' coins (Rounded Down)
```
Speedhack
```
Type: Cheat
Installed Value: 6
Mod Effect: 
    +10 To Movement
Buggy Effect:
    +5 To Movement
    -4 To Damage
```
Extra Lives (NEW)
```
Type: Cheat
Installed Value: 4
Mod Effect: 
    Once per fight, upon player death, ignore it and heal to full instead
Buggy Effect:
    Once per fight, upon player death, ignore it and heal to full instead
    -4 To Health
    -2 To Movement
```
God Mode (NEW)
```
Type: Cheat
Installed Value: 2
Mod Effect: 
    Ignore all reductions to your health
Buggy Effect:
    Ignore all reductions to your health
    +2 To Installed Value
```
Debug Console (NEW)
```
Type: Cheat
Installed Value: 2
Mod Effect: 
    Ignore all reductions to your damage
Buggy Effect:
    Ignore all reductions to your damage
    +2 To Installed Value
```
Free Movement
```
Type: Cheat
Installed Value: 2
Mod Effect: 
    Ignore all reductions to your movement
Buggy Effect:
    Ignore all reductions to your movement
    +2 To Installed Value
```

#### Virus
BonziBuddy
```
Type: Virus
Installed Value: 1
Mod Effect:
    At the end of each turn, discard a System Setting card from your hand
    Can only be uninstalled by 'Antivirus' System Setting
```
Ch3at3rsN3v3rW1n.exe
```
Type: Virus
Installed Value: 2
Mod Effect: 
    -3 To Health per Cheat Installed
    -3 To Damage per Cheat Installed
    -3 To Movement per Cheat Installed
    Can only be uninstalled by 'Antivirus' System Setting
```
CryptoLocker
```
Type: Virus
Installed Value: 2
Mod Effect: 
    Cannot install or uninstall Mods unless a card effect makes you.
    Can only be uninstalled by 'Antivirus' System Setting
```
Cryptominer
```
Type: Virus
Installed Value: 2
Mod Effect:     
    Gives the owner of this card +1 coin at the beginning of your maintenance phase
    Can only be uninstalled by 'Antivirus' System Setting
```
DDoS
```
Type: Virus
Installed Value: 0
Mod Effect: 
    You can have more than one 'DDoS' card installed
    On each of your turns, you have -1 to Bandwith
    Can only be uninstalled by 'Antivirus' System Setting
```
ILOVEYOU
```
Type: Virus
Installed Value: 1
Mod Effect:
    At the end of your maintenance phase, randomly uninstall one Mod
    Can only be uninstalled by 'Antivirus' System Setting
```
Meltdown
```
Type: Virus
Installed Value: 2
Mod Effect: 
    Can be installed on computers with 'Firewall' active
    Can only be uninstalled by 'Antivirus' System Setting
```
Memory Leak
```
Type: Virus
Installed Value: 1
Mod Effect: 
    Each turn, double this card's Installed Value cost
    Can only be uninstalled by 'Antivirus' System Setting
```
Pirated Game
```
Type: Virus
Installed Value: 5
Mod Effect: 
    Can only be uninstalled by 'Antivirus' System Setting
```
Spectre
```
Type: Virus
Installed Value: 2
Mod Effect: 
    Can be installed on computers with 'Firewall' active
    Can only be uninstalled by 'Antivirus' System Setting
```
Spyware
```
Type: Virus
Installed Value: 0
Mod Effect: 
    The original owner of this can play 1 System Settings card from your hand during their turn
    Can only be uninstalled by 'Antivirus' System Setting
```
Stuxnet
```
Type: Virus
Installed Value: 2
Mod Effect: 
    At the end of your maintenance phase, flip a coin. On heads, install this Mod on the previous player's computer. This action happens without need for any other effects. This action cannot happen if the previous player is 'Offline' or has a 'Firewall' active.
    Can only be uninstalled by 'Antivirus' System Setting
```

### System Settings
Administrator Account
```
Cost: 5 Bandwidth
Use: Permanent
Ability: +3 to Computer's System Resources (Down From +5)
```
Burstable Internet Uplink
```
Cost: 1 Bandwidth (Up From 0)
Use: Single Use
Ability: +3 To Bandwidth this turn (Up From +2)
```
CC Cleaner
```
Cost: 1 Bandwidth
Use: Single Use
Ability: Move all installed gameplay mods to your mods folder (From: "Move all uninstalled mods to your mods folder")
```
Cheat Engine (NEW)
```
Cost: 1 Bandwidth Per Turn
Use: Permanent
Ability: Can choose which mods to uninstall
```
Metasploit (Renamed From: "Kali Linux VM")
```
Cost: 2 Bandwidth Per Turn
Use: Permanent
Ability: Allows you to install mods and system settings on other player's computers (From: "Allows you to install mods on other player's computers")
```
Mod Manager
```
Cost: 2 Bandwidth (Down From 4)
Use: Single Use
Ability: Draw 4 mod cards. Pick one and either install or put it in your mods folder.  Shuffle the rest into the mods deck. (From: "Uninstall all installed mods.  Install all previously uninstalled mods.")
```
Multi-Factor Authentication
```
Cost: 5 Bandwidth
Use: Permanent
Ability: Immediately discard all 'Cheat' Mods installed. Cannot install 'Cheat' Mods. +2 To Bandwidth
```
Offline
```
Cost: 1 Bandwidth
Use: Single Use
Ability: Until your next turn you cannot: install mods or system settings on any other player's computers, have mods installed or system settings by other players, or draw any cards (From: "install mods, have mods installed, or draw system settings")
```
Overclocking
```
Cost: 2 Bandwidth
Use: Permanent (From Single Use)
Ability: When a system crash would occur, instead discard this setting and prevent it until the end of your NEXT maintenance phase
```
Registry Editor
```
Cost: 2 Bandwidth
Use: Permanent (From Single Use)
Ability: The next card you draw is free (does not have to be on this turn), then this discard this card
```
Remote Access Tool (NEW)
```
Cost: 1 Bandwidth Per Turn
Use: Permanent
Ability: Allows you to install system settings on other player's computers
```
Scriptkiddie
```
Cost: 1 Bandwidth
Use: Single Use
Ability: Install or uninstall 1 mod or system setting from another player's computer, or negate 1 system setting from another player's computer until your next turn (From: "install or uninstall 1 mod, or negate 1 system setting from another computer")
```