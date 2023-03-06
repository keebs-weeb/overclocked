- [Changelog v0.2](#changelog-v02)
  - [Maintenance Phase Mechanics:](#maintenance-phase-mechanics)
  - [Maintenance Phase Actions Available:](#maintenance-phase-actions-available)
  - [Bandwidth](#bandwidth)
  - [Saving](#saving)
  - [Crashing](#crashing)
  - [Coins](#coins)
  - [The Forums](#the-forums)
  - [The Game](#the-game)
  - [Player's Hands](#players-hands)
  - [Characters](#characters)
  - [Computers Changes](#computers-changes)
    - [Scamdeck](#scamdeck)
    - [Hand-Me-Down](#hand-me-down)
    - [Ol' Reliable](#ol-reliable)
    - [Crackbook](#crackbook)
    - [Gaming Laptop](#gaming-laptop)
    - [Pre-Built](#pre-built)
    - [Enthusiass Desktop](#enthusiass-desktop)
  - [Breakdown - Bosses](#breakdown---bosses)
    - [Demon](#demon)
    - [Dragon](#dragon)
    - [Very Large Fish (Renamed from 'Large Fish')](#very-large-fish-renamed-from-large-fish)
  - [Breakdown - Monsters](#breakdown---monsters)
  - [Mod Changes - Gameplay](#mod-changes---gameplay)
  - [Mod Changes - Cheat](#mod-changes---cheat)
  - [Mod Changes - Virus](#mod-changes---virus)
  - [System Settings Changes](#system-settings-changes)
  - [New Mods - Gameplay](#new-mods---gameplay)
  - [New Mods - Cheats](#new-mods---cheats)
  - [New Mods - Virus](#new-mods---virus)
  - [New System Settings](#new-system-settings)


# Changelog v0.2
----

## Maintenance Phase Mechanics:
```
- Removed 3 actions per Maintenance Phase restriction
- Added mechanic: Bandwidth
- Removed 'Soft Reset' action
```
## Maintenance Phase Actions Available:
```
- Purchase Mods
    - Purchase a Mod card for 5 coins (Up From 3 coins)
-Purchase System Settings
    - Purchase a System Settings card for 5 coins (Up From 3 coins)
```

## Bandwidth
```
NEW MECHANIC
Description: 
    - During each maintenance phase and lasting until their next turn, players have a certain amount of 'Bandwidth' they can use to perform actions
    - Bandwidth is refreshed at the start of a player's maintenance phase
    - The amount of bandwidth differs based on computer
    - Different actions cost different amounts of bandwidth to perform, described below

Action Cost:
    - 1 Bandwidth:
        - Drawing a Mod card
        - Draing a System Settings card
        - Installing a System Settings card on your computer
        - Selling a card to 'The Forums'
        - Installing a mod on another player's computer (this is in addition to the bandwidth cost of the card played)
    - 3 Bandwidth:
        - Installing a System Setting or Mod card on another player's computer
    - Varying Bandwidth:
        - Installing a mod costs X bandwidth, where X is half the value (rounded up) of the Installed System Resources value
        - System Settings each have their own bandwidth cost

Dev Notes:
    - This system will take a lot of balancing and number tweaking.
```

## Saving
```
- Removed the concept of per player saving
- Players now save at each 'checkpoint' that are located at static positions throughout the game board
- Checkpoints are now every 10 spaces on the board
- Players can choose which checkpoint to revert to
- Players can only save on a boss space after that boss has been defeated
```

## Crashing
```
Penalties:
~    - Player loses all of their unreliable coins (From Half their coins + Starting Value)
``` 

## Coins
```
- Coins in each player's bags are now split into 2 categories: 'reliable' and 'unreliable'
- 'Reliable' coins cannot be lost upon player defeat, but are still lost on system crash
- 'Unreliable' coins are all lost upon player defeat, and upon system crash
- When gathered by any means, all coins are 'unreliable'
- Coins become 'reliable' when the player passes a checkpoint
- Players may spend coins from either section when purchasing mods
- Players may now gain coins from selling Mod and System Settings cards to 'The Forums'
```

## The Forums
```
NEW MECHANIC
Description:
    - During their maintenence phase, a player may sell a Mod or a System Settings card to 'The Forums' for 2 coins
    - This uses up 1 Bandwidth
    - When selling a card, that card is sent directly to the discard pile
    - Cards can only be sold from your hand, or from your computer's Mods Folder
```

## The Game
```
- Changes to player defeat
    - On player defeat, that player reverts to last checkpoint on the board, and loses their 'unreliable' coins
    - On player defeat, that player may choose which passed checkpoint to restore to (does not have to be the most recent one)
    - Bosses now appear every 20 spaces
```

## Player's Hands
```
- Players hands can only hold up to 5 cards at a time
- In order to draw a new card, that player must discard a card before drawing the new card
- When discarding a card this way, that player does not get any coins for their card
```

## Characters
```
- Ranger:
    Base:
        12 Health (Unchanged)
        1d20 - 5 Movement (From 1d12)
            AVG 7.5
        1d20 - 10 Damage (From 1d12)
            AVG 5
    Level Up:
        +1 Health (Unchanged)
        +1 Movement (Down From +2)
        +2 Damage (Unchanged)
- Mage:
    Base:
        8 Health (Down From 10)
        1d20 - 10 Movement (From 1d12)
            AVG 5
        1d20 - 8 Damage (From 1d12)
            AVG 6
    Level Up:
        +1 Health (Up From +1)
        +1 Movement (Down From +2)
        +3 Damage (Down From +3)
- Barbarian:
    Base:
        18 Health
        1d20 - 12 Movement (From 1d8)
            AVG 4
        1d20 - 6 Damage (From)
            AVG 7
    Level Up:
        +1 Health (Unchanged)
        +2 Movement (Up From +1)
        +2 Damage (Down From +3)
- Swordsman:
    Base:
        14 Health
        1d20 - 8 Movement (From 1d8)
            AVG 6
        1d20 - 8 Damage (From 1d12)
            AVG 6
    Level Up:
        +1 Health (Down From +2)
        +2 Movement (Up From +1)
        +1 Damage (Down From +2)
```

## Computers Changes
### Scamdeck
```
System Resources: 10
~ Bandwidth: 5 (New)
Trait: Can't get a virus
```

### Hand-Me-Down
```
System Resources: 10
~ Bandwidth: 5 (New)
~ Trait: At the start of your Maintenance, you may flip a coin. If heads, go offline until your next turn (From "At the start of your turn, flip a coin. If heads, go offline until your next turn")
```

### Ol' Reliable
```
System Resources: 12
~ Bandwidth: 5 (New)
~ Trait: On system crash, flip a coin. If heads, uninstall all virus mods, then uninstall mods until you have at least 1 free System Resource (From "On system crash, flip a coin.  If heads, remove all mods and treat the crash like a player death"
```

### Crackbook
```
System Resources: 14
~ Bandwidth: 6 (New)
Trait: Your own System Settings cost 5 coins to play on this computer
```

### Gaming Laptop
```
System Resources: 16
~ Bandwidth: 6 (New)
~ Trait: 'Bug Check' roll values on mods are doubled(From "'Virus' mods have double the effect on this computer")
```

### Pre-Built
```
System Resources: 18
~ Bandwidth: 6 (New)
~ Trait: 'Virus' mods have double the effect on this computer (From "'Bug Check' roll values on mods are doubled")
```

### Enthusiass Desktop
```
System Resources: 20
~ Bandwidth: 8 (New)
Trait: Each turn, skip either your play phase OR your maintenance phase each turn
```


## Breakdown - Bosses
```
- All Bosses Base Damage Increased by 1
- All Bosses have -1 To Max Level (Because Player Will Only Ever Be Level 5)
```
### Demon
```
Level 1:
    Health: 15
    6 Damage
    Rewards: 10 Coins
~    Defeat Penalty: Uninstall 1 'Gameplay' Mod (From "Takes Up 1 System Resources")
Level Up:
    +3 Health
    +1 Damage
    Rewards: +3 Coins Per Level
~    Defeat Penalty: Uninstall .5 More 'Gameplay' Mods Per Level (Rounded Down) (From "Takes Up .5 More System Resources (Rounded Down)")
```
### Dragon
```
Level 1:
    Health: 20
    10 Damage
    Rewards: 20 Coins
~    Defeat Penalty: Takes Up 1 System Resources (From "Uninstall 1 'Gameplay' Mod")
Level Up:
    +3 Health
    +2 Damage
    Rewards: +5 Coins Per Level
~    Defeat Penalty: Takes Up .5 More System Resources (Rounded Down) (From "Uninstall .5 More 'Gameplay' Mods Per Level (Rounded Down)")
```
### Very Large Fish (Renamed from 'Large Fish')
```
Level 1:
    Health: 18
    5 Damage
    Rewards: Draw an Event Card, You may choose to activate it's effects or discard it
~    Defeat Penalty: Skip your next Maintenance phase (From "Skip your next Play phase")
Level Up:
    +3 Health
    +1 Damage
    Rewards: Draw another .5 Event Cards Per Level (Rounded Down), You may choose to activate it's effects or discard it
    Defeat Penalty: No Additional Penalties
```
## Breakdown - Monsters
```
- All Monsters Base Damage Increased by 1
```
---

## Mod Changes - Gameplay
Better AI
```
Type: Gameplay
Installed Value: 3 (Up From 2)
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +2 Coins Collected from Enemies
~        +2 To Movement (New)
    Cons:
~        (Removed +2 Enemy Health)
~        +1 Enemy Damage (New)
Bug Check:
~    Value: 4 (Up From 2)
    Bug: +2 Enemy Health
```
Better UI
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros: 
~        +1 To Movement (New)
        +1 To Damage
    Cons:
~        +2 To Enemy Damage (From '-2 To Movement')
Bug Check:
    Value: 5
    Bug: +2 To Installed Value
```
Controller Remapping
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros: 
~        +3 To Movement (Up From +1)
    Cons:
~       -1 To Damage (New)
Bug Check:
    Value: 5
    Bug: +1 To Installed Value (Down From +2)
```
Corporate Branding
```
Type: Gameplay
Installed Value: 2 (Up From 1)
Uninstalled Value: 1
Mod Effect: 
    Pros: 
        +2 Coins at the start of each maintenance phase
Bug Check:
    Value: 2
    Bug: +2 To Installed Value
```
Difficulty Patch
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros:
~        +3 To Movement (Up From +2)
        +5 Coins Collected from Enemies
    Cons:
        +4 To Enemy Health (Down From +5)
~        +1 To Enemy Damage (New)
Bug Check:
~    Value: 5 (Down From 6)
~    Bug: Upon player defeat, revert at least 2 checkpoints (From 'Revert to Last Save')
```
HD Music Pack
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros:
        -1 To Mod Cost
Bug Check:
    Value: 5
    Bug: +1 To Installed Value (From +1 To Installed AND Uninstalled Value)
```
HD Texture Pack
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros:
        -1 To Mod Price
Bug Check:
    Value: 5
    Bug: +1 To Installed Value (From '+1 To Installed AND Uninstalled Value')
```
Modern Weapons
```
Type: Gameplay
~Installed Value: 4
Uninstalled Value: 2
Mod Effect: 
    Pros:
~        +5 To Damage
    Cons:
~        -2 To Movement (Up From -3)
Bug Check:
    Value: 5
    Bug: +2 To Installed Value
```
No UI
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +2 To Movement
    Cons:
        -1 To Damage
Bug Check:
    Value: 5 (Up From 4)
    Bug: -1 To Damage (From '+2 To Installed Value')
```
Nude Mod
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +2 Coins Collected from Enemies
~        +1 To Movement (New)
    Cons:
~        +2 To Enemy Damage (New)
Bug Check:
    Value: 5
    Bug: -1 To Movement
```
Player Skins
```
Type: Gameplay
Installed Value: 1
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +2 To Damage (Up From +1)
    Cons:
        +1 To Card Cost
Bug Check:
    Value: 5
    Bug: +1 To Installed Value (From '+1 To Installed AND Uninstalled Value')
```

## Mod Changes - Cheat
Infinite Money
```
Type: Cheat
~Installed Value: 5 (Up From 2)
~Uninstalled Value: 2 (Down From 5)
Mod Effect: 
    Pros:
        Can draw Mods and System Settings for free
Bug Check:
~    Value: 10 (Down From 15)
~    Bug: Can't Install 'Firewall' System Settings (From 'Can no longer save game')
```
Quicksaves
```
Type: Cheat
~Installed Value: 2
~Uninstalled Value: 2 (Down From 5)
Mod Effect: 
    Pros:
~        Always checkpoint in front of bosses (From 'Save if you did not save last turn')
Bug Check:
~    Value: 10 (Down From 15)
~    Bug: Upon player defeat, lose half your 'reliable' coins (Rounded Down) (From 'When reverting saves, revert 2 instead')
```
Speedhack
```
Type: Cheat
~Installed Value: 5 (Up From 2)
~Uninstalled Value: 2 (Down From 5)
Mod Effect: 
    Pros:
        +10 To Movement
Bug Check:
~    Value: 15 (Up From 12)
    Bug: -10 To Damage
```

## Mod Changes - Virus
Spyware
```
Type: Virus
Installed Value: 0
Uninstalled Value: NONE
Mod Effect: 
    Cons:
~        The original owner of this can play 1 System Settings card from your hand during their turn (From 'Can play cards from your hand')
Bug Check:
~    Value: 5 (Up from 1)
~    Bug: The original owner of this card can install 1 mod from your mods folder during their turn (From 'All mods drawn are drawn by the original card owner instead')
```
Cryptominer
```
Type: Virus
Installed Value: 4
Uninstalled Value: NONE
Mod Effect:     
    Cons:
        Can only be uninstalled by 'Antivirus' System Setting
~        Gives the owner of this card +1 coin at the beginning of your maintenance phase (New)

Bug Check:
    Value: 10
    Bug: +2 To Installed Value
```

## System Settings Changes
Administrator Account
```
~ Cost: 5 Bandwidth (New)
Use: Permanent
Ability: +5 to Computer's System Resources
```
Antivirus
```
~ Cost: 1 Bandwidth (New)
Use: Single Use
Ability: Uninstall 1 'Virus' mod
```
CC Cleaner
```
~ Cost: 1 Bandwidth (New)
Use: Single Use
Ability: Move all uninstalled mods to your mods folder
```
Firewall
```
~ Cost: 1 Bandwidth (New)
Use: Single Use
Ability: Prevents any mods from being installed on your computer until your next turn
```
Kali Linux VM
```
~ Cost: 1 Bandwidth Per Turn (New)
Use: Permanent
Ability: Allows you to install mods on other player's computers
```
Offline
```
~ Cost: 1 Bandwidth (New)
Use: Single Use
Ability: Until your next turn you cannot: install mods on any other player's computers, have mods installed by other players, or draw system settings cards
```
Overclocking
```
~ Cost: 2 Bandwidth (New)
~ Use: Permanent (From Single Use)
Ability: When a system crash would occur, instead discard this setting and prevent it until the end of your NEXT maintenance phase
```
Scriptkiddie
```
~ Cost: 1 Bandwidth (New)
Use: Single Use
Ability: Install or uninstall 1 mod from another player's computer, or negate 1 system setting from another player's computer until your next turn
```

## New Mods - Gameplay
Armor Overhaul
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +3 To Health
    Cons:
        -1 To Movement
Bug Check:
    Value: 5
    Bug: +1 To Installed Value
```
Better Vendors
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros:
        -1 To Card Cost
Bug Check:
    Value: 5
    Bug: -1 To Movement
```
Big Head
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros: 
        +3 To Movement
    Cons:
        +2 To Enemy Damage
Bug Check:
    Value: 5
    Bug: -1 To Damage
```
Bigger Weapons
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +3 To Damage
    Cons:
        -1 To Movement
Bug Check:
    Value: 5
    Bug: +3 To Enemy Damage
```
Consumable Items Overhaul
```
Type: Gameplay
Installed Value: 3
Uninstalled Value: 1
Mod Effect: 
    Pros:
        Active Effects from Event cards do not expire
    Cons:
        You may only have 1 Active Effect from Event cards at a time (Discard the oldest one if a new one would go into effect)
Bug Check:
    Value: 5
    Bug: +1 To Card Cost
```
Custom Terrain
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +2 Movement
    Cons:
        +1 Enemy Damage
Bug Check:
    Value: 5
    Bug: +1 Enemy Damage
```
Date NPCs
```
Type: Gameplay
Installed Value: 4
Uninstalled Value: 2
Mod Effect: 
    Pros:
        +1 To Health
        +1 To Movement
        +2 To Damage
    Cons:
        +1 To Card Cost
Bug Check:
    Value: 5
    Bug: +2 To Card Cost
```
First Person Mode
```
Type: Gameplay
Installed Value: 1
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +1 To Damage
    Cons:
Bug Check:
    Value: 5
    Bug: +2 To Enemy Damage
```
Furry Mod
```
Type: Gameplay
Installed Value: 3
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +2 To Health
        +2 To Movement
    Cons:
        +2 To Card Cost
Bug Check:
    Value: 5
    Bug: Discard 2 of your unreliable coins at the end of your turn
```
Lore Update
```
Type: Gameplay
Installed Value: 2
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +2 To Damage
    Cons:
        -1 To Movement
Bug Check:
    Value: 5
    Bug: +1 To Card Cost
```
Lower Resolution Support
```
Type: Gameplay
Installed Value: 1
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +1 To Movement
    Cons:
Bug Check:
    Value: 5
    Bug: +1 To Enemy Health
```
Multiclass
```
Type: Gameplay
Installed Value: 3
Uninstalled Value: 2
Mod Effect: 
    Pros:
        Increase Your Lowest Stat By +2 Per Level (Changes if that stat without this increase is no longer your lowest)
    Cons:
        Decrease Your Higest Stat By -2 (Changes if that stat without this increase is no longer your Highest)
Bug Check:
    Value: 5
    Bug: +1 To Installed Value Per Level
```
No Weapons
```
Type: Gameplay
Installed Value: 1
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +3 To Movement
    Cons:
        -2 To Damage
Bug Check:
    Value: 5
    Bug: +2 To Enemy Health
```
Revamped Sidequests
```
Type: Gameplay
Installed Value: 3
Uninstalled Value: 2
Mod Effect: 
    Pros: 
        When you would draw an Event card, draw an additional one
        +2 To Movement
Bug Check:
    Value: 5
    Bug: +1 To Card Cost
```
Third Person Mode
```
Type: Gameplay
Installed Value: 1
Uninstalled Value: 1
Mod Effect: 
    Pros:
        +1 To Movement
    Cons:
Bug Check:
    Value: 5 
    Bug: +1 To Enemy Damage
```
MOD NAME
```
Type: Gameplay
Installed Value: 
Uninstalled Value: 
Mod Effect: 
    Pros:
    Cons:
Bug Check:
    Value:
    Bug:
```
## New Mods - Cheats
MOD NAME
```
Type: Cheat
Installed Value: 
Uninstalled Value: 
Mod Effect: 
    Pros:
    Cons:
Bug Check:
    Value:
    Bug:
```

## New Mods - Virus
Spectre
```
Type: Virus
Installed Value: 2
Uninstalled Value: NONE
Mod Effect: 
    Cons: 
        Can be installed on computers with 'Firewall' active
Bug Check:
    Value: 2
    Bug: +2 To Installed Value
```
Meltdown
```
Type: Virus
Installed Value: 2
Uninstalled Value: NONE
Mod Effect: 
    Cons: 
        Can be installed on computers with 'Firewall' active
Bug Check:
    Value: 2
    Bug: +2 To Installed Value
```
ILOVEYOU
```
Type: Virus
Installed Value: 1
Uninstalled Value: NONE
Mod Effect: 
    Cons: 
        At the end of your maintenance phase, randomly uninstall one Mod.
Bug Check:
    Value: 5
    Bug: +1 To Installed Value
```
CryptoLocker
```
Type: Virus
Installed Value: 2
Uninstalled Value: NONE
Mod Effect: 
    Cons: 
        Cannot install or uninstall Mods unless a card effect makes you.
Bug Check:
    Value: 5
    Bug: +1 To Installed Value
```
Stuxnet
```
Type: Virus
Installed Value: 3
Uninstalled Value: NONE
Mod Effect: 
    Cons: 
        At the end of your maintenance phase, flip a coin. On heads, install this Mod on the previous player's computer. This action happens without need for any other effects. This action cannot happen if the previous player is 'Offline' or has a 'Firewall' active.
Bug Check:
    Value: 5
    Bug: Flip a coin twice instead of once. Both flips must land on heads for this Mod to move.
```
DDoS
```
Type: Virus
Installed Value: 0
Uninstalled Value: NONE
Mod Effect: 
    Cons: 
        On each of your turns, you have -1 to Bandwith. This card can be played along side other 'DDoS' cards
Bug Check:
    Value: 2
    Bug: On each of your turns, you have and additional -1 to Bandwith
```
Ch3at3rsN3v3rW1n.exe
```
Type: Virus
Installed Value: 2
Uninstalled Value: NONE
Mod Effect: 
    Cons: 
        -3 To Health per Cheat Installed
        -3 To Damage per Cheat Installed
        -3 To Movement per Cheat Installed
Bug Check:
    Value: 5
    Bug: -2 To Health, Damage, and Movement per Cheat Installed
```

MOD NAME
```
Type: Virus
Installed Value: 
Uninstalled Value: NONE
Mod Effect: 
    Cons: 
Bug Check:
    Value: 
    Bug: 
```

## New System Settings
Burstable Internet Uplink
```
Cost: 0 Bandwidth
Use: Single Use
Ability: +2 To Bandwidth this turn
```
Forum Reputation
```
Cost: 1 Bandwidth
Use: Single Use
Ability: +2 To Coins received when selling on 'The Forums' This Turn
```
Multi-Factor Authentication
```
Cost: 5 Bandwidth
Use: Permanent
Ability: Immediately discard all 'Cheat' Mods installed. Cannot install 'Cheat' Mods. +2 To Bandwidth
```
BattleEye Anti-Cheat
```
Cost: 3 Bandwidth
Use: Single Use
Ability: Can play on another player's computer that has a 'Cheat' mod installed. Skip player's next turn.
```
Registry Editor
```
Cost: 2 Bandwidth
Use: Single Use
Ability: The next card you draw is free (does not have to be on this turn)
```
Honeypot
```
Cost: 3 Bandwidth (Taken at the start of your next maintenance phase)
Use: Permanent
Ability: May be played in response to a 'Virus' Mod being installed on your system. Immediately discard the next 'Virus' Mod installed on your system, then discard this card.
```
Loud, Clicky, Scratchy Keyboard
```
Cost: 0 Bandwidth
Use: Permanent
Ability: Annoys your friends. Stop it. (Does Nothing)
```
Messy Desk
```
Cost: 0 Bandwidth
Use: Permanent
Ability: How can you live like this? (Does Nothing)
```
Fresh Install
```
Cost: 2 Bandwidth
Use: Single Use
Ability: Move all mods to your Mod Folder. Discard all 'Virus' Mods.
```
Mod Loader
```
Cost: 1 Bandwidth
Use: Single Use
Ability: Installing mods costs 1 less Bandwidth this turn (Minimum 0).  Does not stack with other 'Mod Loader' cards.
```
Mod Manager
```
Cost: 4 Bandwidth
Use: Single Use
Ability: Uninstall all installed mods. Install all previously uninstalled mods.
```
SETTING NAME
```
Use: 
Ability: 
```