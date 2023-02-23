import random
from modules import bosses, monsters

class boardClass:
    def __init__(self):
        self.maxSpaces = 100
        self.bossSpaces = [20, 40, 60, 80, 100]
        self.bossIndex = 0
        self.bossDefeatProb = .25
        self.monsterSpawnProb = .50
        self.monsterDefeatProb = .10
        self.everyOtherTurn = True
    
    def doMove(self, playerCharacter):
        # Roll for movement, ensure min move is 1
        attemptMove = playerCharacter.attemptedMove
        if attemptMove <= 0:
            attemptMove = 1

        # Check for game winning conditions
        if playerCharacter.curSpace + attemptMove >= 100:
            # Check if player will defeat boss or not
            # if random.random() > self.bossDefeatProb:
            spawnedBoss = bosses.bossClass()
            if self.doFight(playerCharacter, spawnedBoss):
                self.bossIndex += 1
                playerCharacter.curSpace = 101
            else:
                playerCharacter.curSpace = 90
                playerCharacter.defeatCounter['boss']['total'] += 1
                try:
                    playerCharacter.defeatCounter['boss'][spawnedBoss.name] += 1
                except KeyError:
                    playerCharacter.defeatCounter['boss'][spawnedBoss.name] = 1
        # Check for general boss fighting conditions
        elif playerCharacter.curSpace + attemptMove >= self.bossSpaces[self.bossIndex]:
            # Check if player, on statistical average, will defeat boss or not
            # if random.random() > self.bossDefeatProb:
            spawnedBoss = bosses.bossClass()
            if self.doFight(playerCharacter, spawnedBoss):
                playerCharacter.curSpace = self.bossSpaces[self.bossIndex]
                self.bossIndex += 1
                playerCharacter.level += 1
            else:
                playerCharacter.curSpace = self.bossSpaces[self.bossIndex] - 10
                playerCharacter.defeatCounter['boss']['total'] += 1
                try:
                    playerCharacter.defeatCounter['boss'][spawnedBoss.name] += 1
                except KeyError:
                    playerCharacter.defeatCounter['boss'][spawnedBoss.name] = 1
        # Otherwise, just move
        else:
            # Check if a monster will spawn
            # If not, move to the space
            if random.random() > self.monsterSpawnProb:
                playerCharacter.curSpace += attemptMove
            # If it does, calculate chance player will defeat or not
            else:
                spawnedMonster = monsters.monsterClass()
                if self.doFight(playerCharacter, spawnedMonster):
                # if random.random() > self.monsterDefeatProb:
                    playerCharacter.curSpace += attemptMove
                else:
                    # mod10 = playerCharacter.curSpace % 10
                    # moveTo = playerCharacter.curSpace - mod10
                    # playerCharacter.curSpace = moveTo
                    playerCharacter.curSpace = playerCharacter.curSpace - (playerCharacter.curSpace % 10)
                    playerCharacter.defeatCounter['monster']['total'] += 1
                    try:
                        playerCharacter.defeatCounter['monster'][spawnedMonster.name] += 1
                    except KeyError:
                        playerCharacter.defeatCounter['monster'][spawnedMonster.name] = 1

        playerCharacter.timesMoved += 1
        self.everyOtherTurn = False if self.everyOtherTurn else True # Do something every other turn (increase power of player for instance)
        return playerCharacter

    def doFight(self, playerCharacter, enemyCharacter):
        playerHealth = playerCharacter.calcStat("health")
        enemyHealth = enemyCharacter.calcStat("health", playerCharacter)
        enemyDamage = enemyCharacter.calcStat("damage", playerCharacter)

        while playerHealth > 0 or enemyHealth > 0:
            # Player Damage Action
            playerDamage = playerCharacter.rollDamage()
            if enemyHealth - playerDamage <= 0:
                return True
            else:
                enemyHealth -= playerDamage
            # Enemy Damage Action
            if playerHealth - enemyDamage <= 0:
                return False
            else:
                playerHealth -= enemyDamage
