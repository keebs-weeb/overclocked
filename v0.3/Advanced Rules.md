- [Game Overview](#game-overview)
  - ["The Game"](#the-game)
  - [Winning](#winning)
  - [Player Characters](#player-characters)
  - [Player's Hands](#players-hands)
  - [Computers](#computers)
- [Gameplay Info](#gameplay-info)
  - [Battles](#battles)
  - [Coins](#coins)
  - [Combat](#combat)
  - [Crashing](#crashing)
  - [Enemies](#enemies)
  - [The Forums](#the-forums)
  - [Maintenance](#maintenance)
    - [Bandwidth](#bandwidth)
  - [Mods](#mods)
  - [Mods Folder](#mods-folder)
  - [Event Deck](#event-deck)
  - [Movement](#movement)
  - [Saving](#saving)
  - [System Settings](#system-settings)


## Game Overview
### "The Game"
```
Description:
    - "The Game" is the game that is being played by each player
    - "The Game" is the same length for each player, with the same number of bosses

The Game:
    - The board is 101 spaces long, with the start being 0 and the end being 100
    - Checkpoint spaces are located every 10 spaces, and if a player would lose to a monster/boss or a computer would crash, their character will begin play at the last passed checkpoint
    - Boss spaces are on spaces 20, 40, 60, 80, and 100
        - In order to beat "The Game" a player must defeat the boss on the final space
    - Scattered throughout, and marked with one of 3 different symbols, are 'Action' spaces that a player may choose to stop on if they would pass over it.
        - Monster Spaces
            - These spaces allow the player to fight a monster from the Monster deck
            - These spaces are more frequent at the start, and less frequent as 'The Game' goes on
        - Vendor Spaces
            - These spaces allow cards purchased during the following maintenance phase to have -1 to cost
            - These spaces occur approximately every 20 spaces
        - Treasure Spaces
            - These spaces give the players a windfall of coins and are very few and far between: only 2 on the game board
            - When a player lands on it, a d12 is rolled and gold is given to the player equal to the roll plus the value listed on the board
        - Cutscene Spaces
            - These spaces occur on checkpoint spaces without bosses
            - When a player lands on it, they may draw up to 2 event cards and take the actions listed
```
### Winning
```
Description:
    - A Player wins "The Game" when they defeat the boss on the final space without crashing or dying in the process
```
### Player Characters
```
Description:
    - At the start of the game, players choose a character to play with
    - Characters level up after each boss fight

Player Defeat:
    - If a player is reduced to 0 life before they kill the enemy they are fighting, they are defeated
    - On player defeat, that player loses their 'unreliable' coins
    - On player defeat, that player may choose which passed checkpoint to restore to (does not have to be the most recent one)
```
### Player's Hands
```
Description:
    - Players hands can only hold up to 5 cards at a time
    - In order to draw a new card, that player must discard a card before drawing the new card
    - When discarding a card this way, that player does not get any coins for their card
```
### Computers
```
Description:
    - The main tools that players work on, as they run "The Game".
    - Chosen at the beginning of gameplay and cannot be Modified during game
    - Have a limited number of system resources that they can install Mods with, determined by computer stats
    - Have a limited number of Bandwidth that the player can take actions with during the maintenance phase

System Settings:
    - Computers can be Modified with 'System Settings' to do things like free more resources, prevent getting hacked, and become overclocked
```

## Gameplay Info
### Battles
```
Description:
    - Battles take place between one player and one enemy.  Players roll damage, and enemies deal damage based on their stats, minus player character stats.

Winning and Losing:
    - If a player defeats an enemy, their movement for the turn is over, and they collect the rewards listed on the card
    - If a player is defeated by an enemy, their movement for the turn is over, and a debuff is placed on them by the enemy
```
> See Section [Player Characters](#player-characters) for more information on being defeated by an enemy

### Coins
```
Description:
    - Coins are used to draw cards in "The Game".
    - Coins are gathered upon defeating enemies based on enemy stats, plus any Mods values currently installed on a player's computer.
    - There is no maximum limit to how many coins a player can carry.
    - Coins are split in two categories: 'Reliable' and 'Unreliable' coins
        - 'Reliable' coins cannot be lost upon player defeat, but are still lost on system crash
        - 'Unreliable' coins are all lost upon player defeat, and upon system crash
    - When collected by any means, all coins are 'unreliable'
    - Coins become 'reliable' when the player passes a checkpoint
    - Players may spend coins from either section when purchasing mods
    - Upon a system crashing, half of a player's coins (rounded up) are lost
    - Upon death, all 'unreliable' coins are lost
```

### Combat
```
Description:
    - Combat is the action that happens when a player fights a monster or boss.  
    - The minimum amount of damage that can be done during combat is 1.

Order:
    - When fighting an enemy, the following combat rules are applied:
    - First, player rolls the dice and deals damage to the enemy
    - Next, the enemy deals a static damage value to othe player
    - This continues until either the player or enemy is defeated
    - After combat (win or lose), the player is healed to full health
```

### Crashing
```
Description:
    - When a computer exceeds the maximum system resources it can hold, it crashes and progress in "The Game" is lost
    - This happens immediately and players cannot take any further actions once it happens

Penalties:
    - Player loses all their 'Unreliable' coins
    - Player reverts to last checkpoint location in "The Game"
    - All 'Virus' Mods are removed
    - All 'Active Effects' are removed and discarded
    - Players must uninstall Mods (starting from the first installed) until their computer is at least half of the system resources are free
    - Players turn is immediately ended.  If system crash happens during another player's turn, the player with the crashed system's next turn is skipped.
```

### Enemies
```
Description:
    - Enemies are NPC units that appear throughout "The Game"
    - Enemies must be fought to progress, and upon beating then reward the character that defeated them with coins
    - Enemies are fought via the rules listed in the 'Combat' section above

Enemy Types:
    - Monster
        - Base enemy type, appears randomly throughout the board in Action Spaces
        - On Kill: Awards gold (dependant on card)
        - On Player Defeat: Takes up system resources, or have special actions (dependant on stats).  Place current monster card into 'Active Effects' board space.
        - Levels up with player, including it's active effects.  
            - For example, if a monster defeats the player at level 1 and the player eventually levels up to 2 then the monster's active effect will be at level 2.
    - Bosses
        - Bosses are enemies with static locations on the game board, and are harder than regular monsters
        - Occur every 20 spaces with the final boss on space 100
        - On Kill: Will either award gold, Mods, or special actions (dependant on the boss card)
        - On Player Defeat: Will either take up system resources, or have special actions (dependant on the boss card).  Place current boss card into 'Active Effects' board space, and draw another boss.
        - Levels up with player (up to level 5), including it's active effects.  
            - For example, if a boss defeats the player at level 1 and the player eventually levels up to 2 then the boss's active effect will be at level 2.
```
### The Forums
```
Description:
    - During their maintenence phase, a player may sell a Mod or a System Settings card to 'The Forums' for 2 coins
    - This action uses up 1 Bandwidth, and that card sold is sent directly to the discard pile
    - Cards can only be sold from your hand (System Settings), or from your computer's Mods Folder (Mods)
```

### Maintenance
```
Description:
    - The Maintenance phase is the phase after all in-game actions have been performed.
    - Each player can take any of these actions, based on the amount of Bandwidth that player's computer has

Actions Available:
    - Purchase Mods
        - Purchase a Mod card for coins from the Mod deck.  This can be installed immediately for no extra actions, or put it into your mods folder
    - Install, or uninstall mods
        - Install a Mod from the Mod folder
        - Uninstall a Mod from your computer
        - Install a Mod on another player's computer, if able
    - Purchase System Settings
        - Purchase a System Settings card for coins from the System Settings Deck.  This can be installed immediately for no extra actions, or put it into your hand
    - Play system settings
        - Play system settings from your hand
        - Activate effects of played system settings
    - Sell an item on The Forums
    - End turn
        - Always available to be taken, does not cost an action
        - Ends player's turn immediately
```

#### Bandwidth
```
Description: 
    - During each maintenance phase and lasting until their next turn, players have a certain amount of 'Bandwidth' they can use to perform actions
    - Bandwidth is refreshed at the start of a player's maintenance phase
    - The amount of bandwidth differs based on computer
    - Different actions cost different amounts of bandwidth to perform, described below

Action Cost:
    - 1 Bandwidth:
        - Drawing a Mod card
        - Drawing a System Settings card
        - Installing a System Settings card on your computer
        - Selling a card to 'The Forums'
    - Varying Bandwidth:
        - Installing a mod costs X bandwidth, where X is half the value (rounded up) of the Installed System Resources value
        - System Settings each have their own bandwidth cost
```

### Mods
```
Description:
    - Mods are the primary tool to augment 'The Game' and help you progress faster
    - Mods are located either in the Mods Deck, Mods Folder, or the Installed Mods section of your computer
    - Mods have two sides to each card, 'Clean', and 'Buggy.  Usually you would want to install these on the 'Clean' side on your system!
    - If a Mod is installed and it pushes a computer over it's maximum system resources, that player's computer crashes
    - Mods come in three general categories:
        - Gameplay: Mods that have benefits and drawbacks, giving a good balance
        - Cheat: Mods that are strictly advantageous, but have brutal downsides if installed Buggy
        - Virus: Mods that are big resource hogs, or have other detrimental effects. Play these ones on your friends!

Installing and Uninstalling Mods:
    - When installing mods, no more than one mod of the same name can be installed on your computer
    - When a mod is drawn from the Mod Deck, you may install it immediately onto your computer or place it into the Mods Folder
    - To uninstall a mod, you must uninstall them IN ORDER, starting from the oldest installed mod and working your way forward
        - This limit is overrided with certain System Settings cards
    - When uninstalling a mod, that card is immediately discarded
    - 'Virus' type mod cards cannot be normally uninstalled, as they require a System Setting or System Crash to be removed

'Clean' and 'Buggy' Mods:
    - Mods are split into two halves, a 'Clean' and a 'Buggy' side
    - Mods can be chosen to be installed in any way the installing player wishes
```
> See the Advanced Rules for more in-depth breakdown of mods, mod costs, installing mods, etc

### Mods Folder
```
Description:
    - The Mods Folder is where mods can be kept for future use
    - Mods in this folder don't count towards your system resources, and they do not provide any effects until they are installed
    - To install a mod from this folder, no coin payment is required
```
### Event Deck
```
Description:
    - A central deck of cards that players draw from immediately after the play phase
    - Contains bonus coins, computer events, or character effects
```
### Movement
```
Description:
    - Movement actions are determined by the player character stats and mods installed on a computer.
    - Movement is calculated as follows:
        - Base Movement Die Roll
        - Multiply if any multipliers present
        - Add in additional level and mod values
    - The Minimum amount of movement is 1, if mods make your roll negative or 0 then move only 1 space forward.
```
### Saving
```
Description:
    - Save points are locations in the game that a player reverts back to if certain events happen
    - These spaces occur every 10 spaces in the game
    - You only reach a checkpoint on a boss space after you defeat the boss

Examples:
    - System Crash (Revert to Last Save)
    - Player Death (Revert to Last Save, or Choose Which Space to Revert to)
```

### System Settings
```
Description:
    - System Settings are additional cards that can be played that modify a player's computer
    - System Settings must be played during your maintenance phase, with little exception
    - There can only be 2 'Permanent' system settings active on a player's computer at any given time
        - Players can discard an old System Setting and play a new one for one action
    - System Settings can be purchased from the System Settings deck for coins, and are drawn into the player's hand
    - In the maintenance phase, playing a system setting and activating a system setting each take up 1 Bandwidth
    - If a card lasts for a number of turns, the number of turns decreases by 1 at the START of that player's maintenance phase. 
        - For example 'Offline' lasts from when you play it until the start of your next maintenance phase

Permanent vs Single Use:
    - 'Permanent' Cards stick around until they are triggered, or they are discarded.
    - 'Single Use' Cards are played are discarded after use.  If there is an effect that lasts until your next turn, keep it in the 'Active Effects' zone on the board
```

---