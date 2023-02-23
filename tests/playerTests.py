import random
import numpy
from contextlib import redirect_stdout
from modules import players, board, bosses, monsters
import time

def boardPlayTest():
    charNamesArr = ["mage", "barbarian", "ranger", "swordsman"]
    # charNamesArr = ["mage"]

    for name in charNamesArr:
        activeCharacterName = name
        samples = 1000000
        movementArr = []
        defeatArr = []
        modDict = {
            "health": [],
            "damage": [],
            "move": []
        }
        bossDefeatStatsDict = {}
        monsterDefeatStatsDict = {}

        bestRun = {"moves": 100, "bossDeaths": False, "monsterDeaths": False, "stats": False}
        worstRun = {"moves": 0, "bossDeaths": False, "monsterDeaths": False, "stats": False}

        for i in range(0,samples):
            activeCharacter = players.playerClass(activeCharacterName)
            activeBoard = board.boardClass()

            while activeCharacter.curSpace <= 100:
                activeCharacter.attemptedMove = activeCharacter.rollMove()
                activeCharacter = activeBoard.doMove(activeCharacter)
                if activeBoard.everyOtherTurn:
                    roll = random.randint(1,7)
                    if roll == 1:
                        activeCharacter.modHealth += random.randint(2,3)
                    elif roll == 2:
                        activeCharacter.modMove += random.randint(1,2)
                    elif roll == 3:
                        activeCharacter.modDamage += random.randint(1,2)
                activeCharacter.attemptedMove = 0
                # print("Moved to: ",activeCharacter.curSpace)
                # print("    Boss Index: ",activeBoard.bossIndex)
                # print("    Took",activeCharacter.timesMoved,"movements")

            # print(name+" Game Over. Took",activeCharacter.timesMoved,"movements")
            movementArr.append(activeCharacter.timesMoved)
            defeatArr.append(activeCharacter.defeatCounter['boss']['total']+activeCharacter.defeatCounter['monster']['total'])
            for key,value in activeCharacter.defeatCounter['boss'].items():
                if key == "total":
                    continue
                try:
                    bossDefeatStatsDict[key] += value
                except KeyError:
                    bossDefeatStatsDict[key] = value
            for key,value in activeCharacter.defeatCounter['monster'].items():
                if key == "total":
                    continue
                try:
                    monsterDefeatStatsDict[key] += value
                except KeyError:
                    monsterDefeatStatsDict[key] = value
            modDict["health"].append(activeCharacter.modHealth)
            modDict["damage"].append(activeCharacter.modDamage)
            modDict["move"].append(activeCharacter.modMove)
            if activeCharacter.timesMoved < bestRun["moves"]:
                bestRun["moves"] = activeCharacter.timesMoved
                bestRun["stats"] = activeCharacter.getStats()
                bestRun["bossDeaths"] = activeCharacter.defeatCounter['boss']['total']
                bestRun["monsterDeaths"] = activeCharacter.defeatCounter['monster']['total']
            if activeCharacter.timesMoved > worstRun["moves"]:
                worstRun["moves"] = activeCharacter.timesMoved
                worstRun["stats"] = activeCharacter.getStats()
                worstRun["bossDeaths"] = activeCharacter.defeatCounter['boss']['total']
                worstRun["monsterDeaths"] = activeCharacter.defeatCounter['monster']['total']
        print(name.capitalize()+" Average Moves: ",numpy.mean(movementArr),"(samples: ",samples,")")
        print(name.capitalize()+" Average Defeats: ",numpy.mean(defeatArr),"(samples: ",samples,")")
        print(name.capitalize()+" Average modHealth: ",numpy.mean(modDict["health"]),"(samples: ",samples,")")
        print(name.capitalize()+" Average modDamage: ",numpy.mean(modDict["damage"]),"(samples: ",samples,")")
        print(name.capitalize()+" Average modMove: ",numpy.mean(modDict["move"]),"(samples: ",samples,")")
        print(name.capitalize()+" Best Run: ",bestRun)
        print(name.capitalize()+" Worst Run: ",worstRun)
        # print(name.capitalize()+" Boss Defeat Stats: ",bossDefeatStatsDict)
        # print(name.capitalize()+" Monster Defeat Stats: ",monsterDefeatStatsDict)
        # print(name.capitalize()+" Ending Level: ",activeCharacter.level)
        # print(name.capitalize()+" Ending Stats: ",activeCharacter.getStats())
        print("\r")


def bossFightTest():
    bossNames = ["dragon", "rogue warrior", "demon", "very large fish"]
    charNames = ["mage", "barbarian", "ranger", "swordsman"]
    # charNames = ["swordsman"]
    samples = 10000

    for char in charNames:
        print(char.capitalize()+":")
        totalsArr = {"False": 0, "True": 0}
        for boss in bossNames:
            newBoss = bosses.bossClass(boss)
            newPlayer = players.playerClass(char)
            newPlayer.level = 0
            newPlayer.modDamage = 2
            newBoard = board.boardClass()

            resultArr = []
            for i in range(0, samples):
                result = newBoard.doFight(newPlayer, newBoss)
                resultArr.append(result)

            unique, counts = numpy.unique(resultArr, return_counts=True)
            print("\t",boss.capitalize()+" Results:")
            print("\t\t",dict(zip(unique, counts)))
            if counts[0] != samples:
                totalsArr["False"] += counts[0]
                totalsArr["True"] += counts[1]
            else:
                if unique[0] == True:
                    counts = numpy.append(counts, counts[0])
                    counts[0] = 0
                else:
                    counts = numpy.append(counts, [0])
                totalsArr["False"] += counts[0]
                totalsArr["True"] += counts[1]
            print("\t\tWin Percentage:", str(round((counts[1] / samples) * 100, 2)))
        print("\nOverall Win Percentage:", str(round((totalsArr["True"] / (samples * (len(bossNames))) * 100), 2)))
        print("\n")

def monsterPlayTest():
    charNames = ["mage", "barbarian", "ranger", "swordsman"]
    # charNames = ["ranger"]
    monsterNames = ['bird man', 'ghost', 'necromancer', 'royal archer', 'royal knight', 'ogre', 'scorpion', 'zombie']
    # monsterNames = ['scorpion']
    samples = 10000

    for char in charNames:
        print(char.capitalize()+":")
        totalsArr = {"False": 0, "True": 0}
        for monster in monsterNames:
            newMonster = monsters.monsterClass(monster)
            newPlayer = players.playerClass(char)
            newPlayer.level = 3
            newPlayer.modDamage = 0
            newPlayer.modHealth = 0
            newBoard = board.boardClass()

            resultArr = []
            for i in range(0, samples):
                result = newBoard.doFight(newPlayer, newMonster)
                resultArr.append(result)

            unique, counts = numpy.unique(resultArr, return_counts=True)
            print("\t",monster.capitalize()+" ("+newMonster.title+") Results:")
            print("\t\t",dict(zip(unique, counts)))
            if counts[0] != samples:
                totalsArr["False"] += counts[0]
                totalsArr["True"] += counts[1]
            else:
                if unique[0] == True:
                    counts = numpy.append(counts, counts[0])
                    counts[0] = 0
                else:
                    counts = numpy.append(counts, [0])
                totalsArr["False"] += counts[0]
                totalsArr["True"] += counts[1]
            print("\t\tWin Percentage:", str(round((counts[1] / samples) * 100, 2)))
        print("\nOverall Win Percentage:", str(round((totalsArr["True"] / (samples * (len(monsterNames))) * 100), 2)))
        print("\n")
    pass

startTime = time.time()
# bossFightTest()
boardPlayTest()
# monsterPlayTest()
print("--- Code Finished in %s seconds ---" % (time.time() - startTime))