import random
import numpy as np
from contextlib import redirect_stdout
import time
import sys
import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from modules import players, board, bosses, monsters, heatmapGenerator

def boardPlayTest():
    charNamesArr = ["mage", "barbarian", "ranger", "swordsman"]

    for name in charNamesArr:
        activeCharacterName = name
        samples = 10000
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
                    roll = random.randint(1,4)
                    if roll == 1:
                        activeCharacter.modHealth += random.randint(1,2)
                    elif roll == 2:
                        activeCharacter.modMove += random.randint(1,2)
                    elif roll == 3:
                        activeCharacter.modDamage += random.randint(1,2)
                    # roll = random.randint(1,5)
                    # if roll == 1:
                    #     activeCharacter.modHealth -= random.randint(-1,1)
                    # elif roll == 2:
                    #     activeCharacter.modMove -= random.randint(-1,1)
                    # elif roll == 3:
                    #     activeCharacter.modDamage -= random.randint(-1,1)
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
        print(name.capitalize()+" Average Moves: ",np.mean(movementArr),"(samples: ",samples,")")
        print(name.capitalize()+" Average Defeats: ",np.mean(defeatArr),"(samples: ",samples,")")
        print(name.capitalize()+" Average modHealth: ",np.mean(modDict["health"]),"(samples: ",samples,")")
        print(name.capitalize()+" Average modDamage: ",np.mean(modDict["damage"]),"(samples: ",samples,")")
        print(name.capitalize()+" Average modMove: ",np.mean(modDict["move"]),"(samples: ",samples,")")
        print(name.capitalize()+" Best Run: ",bestRun)
        print(name.capitalize()+" Worst Run: ",worstRun)
        # print(name.capitalize()+" Boss Defeat Stats: ",bossDefeatStatsDict)
        # print(name.capitalize()+" Monster Defeat Stats: ",monsterDefeatStatsDict)
        # print(name.capitalize()+" Ending Level: ",activeCharacter.level)
        # print(name.capitalize()+" Ending Stats: ",activeCharacter.getStats())
        print("\r")


def bossFightTest(printToConsole=True):
    if not printToConsole:
        printToConsole = sys.stdout
        f = open(os.devnull, 'w')
        sys.stdout = f

    bossNames = ["rogue warrior",  "very large fish", "demon", "maddened mage", "dragon"]
    charNames = ["mage", "barbarian", "ranger", "swordsman"]
    summaryDict = {"mage": {}, "barbarian": {}, "ranger": {}, "swordsman": {}}
    samples = 10000

    for char in charNames:
        print("***************")
        print("Iterating "+char)
        print("***************")
        summaryDict[char] = {}

        for level in range(0,5):
            # Set up player character values
            totalsArr = {"False": 0, "True": 0}
            mostDifficult = []
            newPlayer = players.playerClass(char)
            newPlayer.level = level
            monster = bossNames[level]
            summaryDict[char][monster] = {}
            for healthMod in range(0, 5):
                summaryDict[char][monster][healthMod] = {}
                for damageMod in range(0,6):
                    summaryDict[char][monster][healthMod][damageMod] = {}
                    newPlayer.modDamage = damageMod
                    newPlayer.modHealth = healthMod
                    print("Damage Mod Value:",newPlayer.modDamage)
                    print("Health Mod Value:",newPlayer.modHealth)

                    # Fight boss at appropriate level
                    newMonster = bosses.bossClass(monster)
                    newBoard = board.boardClass()
                    resultArr = []
                    for i in range(0, samples):
                        result = newBoard.doFight(newPlayer, newMonster)
                        resultArr.append(result)

                    # Output results to console
                    unique, counts = np.unique(resultArr, return_counts=True)
                    print(monster.capitalize()+" Results:")
                    print("\t",dict(zip(unique, counts)))

                    # Calculate Win Percentage
                    if counts[0] != samples:
                        totalsArr["False"] += counts[0]
                        totalsArr["True"] += counts[1]
                    else:
                        if unique[0] == True:
                            counts = np.append(counts, counts[0])
                            counts[0] = 0
                        else:
                            counts = np.append(counts, [0])
                        totalsArr["False"] += counts[0]
                        totalsArr["True"] += counts[1]
                    winPercentage = round((counts[1] / samples) * 100, 2)
                    summaryDict[char][monster][healthMod][damageMod] = winPercentage

    # Close out function, generate heatmap
    print(summaryDict)
    if not printToConsole == True:
        f.close()
        sys.stdout = printToConsole
    heatmapGenerator.bossHeatmap(summaryDict, os.path.dirname(__file__))

def monsterPlayTest(printToConsole=True):
    if not printToConsole:
        printToConsole = sys.stdout
        f = open(os.devnull, 'w')
        sys.stdout = f

    monsterNames = [['bird man', 'scorpion', 'zombie'], ['necromancer', 'ghost', 'royal archer'], ['baby drake', 'royal knight', 'ogre']]
    charNames = ["mage", "barbarian", "ranger", "swordsman"]
    summaryDict = {"mage": {}, "barbarian": {}, "ranger": {}, "swordsman": {}}
    samples = 100

    for char in charNames:
        print("***************")
        print("Iterating "+char)
        print("***************")
        summaryDict[char] = {}

        for zone in range(0,3):
            # Set up player character values
            totalsArr = {"False": 0, "True": 0}
            newPlayer = players.playerClass(char)
            if zone == 0:
                newPlayer.level = 0
            elif zone == 1:
                newPlayer.level = 2
            elif zone == 2:
                newPlayer.level = 4
            for monster in monsterNames[zone]:
                summaryDict[char][monster] = {}
                for healthMod in range(0, 5):
                    summaryDict[char][monster][healthMod] = {}
                    for damageMod in range(0,6):
                        summaryDict[char][monster][healthMod][damageMod] = {}
                        newPlayer.modDamage = damageMod
                        newPlayer.modHealth = healthMod
                        print("Damage Mod Value:",newPlayer.modDamage)
                        print("Health Mod Value:",newPlayer.modHealth)

                        # Fight boss at appropriate level
                        newMonster = monsters.monsterClass(zone, monster)
                        newBoard = board.boardClass()
                        resultArr = []
                        for i in range(0, samples):
                            result = newBoard.doFight(newPlayer, newMonster)
                            resultArr.append(result)

                        # Output results to console
                        unique, counts = np.unique(resultArr, return_counts=True)
                        print(monster.capitalize()+" Results:")
                        print("\t",dict(zip(unique, counts)))

                        # Calculate Win Percentage
                        if counts[0] != samples:
                            totalsArr["False"] += counts[0]
                            totalsArr["True"] += counts[1]
                        else:
                            if unique[0] == True:
                                counts = np.append(counts, counts[0])
                                counts[0] = 0
                            else:
                                counts = np.append(counts, [0])
                            totalsArr["False"] += counts[0]
                            totalsArr["True"] += counts[1]
                        winPercentage = round((counts[1] / samples) * 100, 2)
                        summaryDict[char][monster][healthMod][damageMod] = winPercentage
    # Close out function, generate heatmap
    print(summaryDict)
    if not printToConsole == True:
        f.close()
        sys.stdout = printToConsole
    heatmapGenerator.monsterHeatmap(summaryDict, os.path.dirname(__file__))

startTime = time.time()
# boardPlayTest()
# bossFightTest(False)
monsterPlayTest(False)
print("--- Code Finished in %s seconds ---" % (time.time() - startTime))