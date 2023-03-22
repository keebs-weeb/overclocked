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
    bossNames = ["dragon", "rogue warrior", "demon", "very large fish"]
    charNames = ["mage", "barbarian", "ranger", "swordsman"]
    samples = 10000

    summaryDict = {"mage": {}, "barbarian": {}, "ranger": {}, "swordsman": {}}
    for level in range(0,4):
        print("***************")
        print("LEVEL",level+1,"RESULTS")
        print("***************\n")
        for char in charNames:
            totalsArr = {"False": 0, "True": 0}
            mostDifficult = []
            print(char.capitalize()+":")
            newPlayer = players.playerClass(char)
            newPlayer.level = level
            newPlayer.modDamage = 1
            newPlayer.modHealth = 2
            print("Damage Mod Value:",newPlayer.modDamage)
            print("Health Mod Value:",newPlayer.modHealth)
            summaryDict[char][level] = {"level": level}
            summaryDict[char][level]["modDamage"] = newPlayer.modDamage
            summaryDict[char][level]["modHealth"] = newPlayer.modHealth
            summaryDict[char][level]["monster"] = {}
            for monster in bossNames:
                summaryDict[char][level]["monster"][monster] = {}
                newMonster = bosses.bossClass(monster)
                newBoard = board.boardClass()
                resultArr = []

                for i in range(0, samples):
                    result = newBoard.doFight(newPlayer, newMonster)
                    resultArr.append(result)

                unique, counts = np.unique(resultArr, return_counts=True)
                print("\t",monster.capitalize()+" Results:")
                print("\t\t",dict(zip(unique, counts)))
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
                print("\t\tWin Percentage:", str(winPercentage))
                summaryDict[char][level]["monster"][monster] = winPercentage
                if len(mostDifficult) == 0:
                    mostDifficult.append({"name": newMonster.name, "winPercentage": winPercentage})
                elif len(mostDifficult) <= 10:
                    for i in range(0, len(mostDifficult)):
                        if winPercentage < mostDifficult[i]["winPercentage"]:
                            monsterInformation = {"name": newMonster.name, "winPercentage": winPercentage}
                            if i == 9:
                                mostDifficult[i] = monsterInformation
                            else:
                                mostDifficult.insert(i, monsterInformation)
                                mostDifficult.pop()
                            break
                        elif len(mostDifficult) < 10:
                            mostDifficult.append({"name": newMonster.name, "winPercentage": winPercentage})
                            break

            print("\t\tHardest Bosses:",mostDifficult)
            print("\nOverall Win Percentage:", str(round((totalsArr["True"] / (samples * (len(bossNames) * 3)) * 100), 2)))
            summaryDict[char][level]["overall"] = round((totalsArr["True"] / (samples * (len(bossNames) * 3)) * 100), 2)
            print("\n")
        print("\n")
    f.close()
    sys.stdout = printToConsole
    print(summaryDict)
    heatmapGenerator.main(summaryDict, os.path.dirname(__file__), True)
    pass

def monsterPlayTest(printToConsole=True):
    if not printToConsole:
        printToConsole = sys.stdout
        f = open(os.devnull, 'w')
        sys.stdout = f
    charNames = ["mage", "barbarian", "ranger", "swordsman"]
    monsterNames = ['bird man', 'ghost', 'necromancer', 'royal archer', 'royal knight', 'ogre', 'scorpion', 'zombie']
    monsterTitles = ["lesser", "normal", "greater"]
    samples = 10000

    summaryDict = {"mage": {}, "barbarian": {}, "ranger": {}, "swordsman": {}}

    for level in range(0,4):
        print("***************")
        print("LEVEL",level+1,"RESULTS")
        print("***************\n")
        for char in charNames:
            totalsArr = {"False": 0, "True": 0}
            mostDifficult = []
            print(char.capitalize()+":")
            newPlayer = players.playerClass(char)
            newPlayer.level = level
            newPlayer.modDamage = 1
            newPlayer.modHealth = 2
            print("Damage Mod Value:",newPlayer.modDamage)
            print("Health Mod Value:",newPlayer.modHealth)
            summaryDict[char][level] = {"level": level}
            summaryDict[char][level]["modDamage"] = newPlayer.modDamage
            summaryDict[char][level]["modHealth"] = newPlayer.modHealth
            summaryDict[char][level]["monster"] = {}
            for monster in monsterNames:
                summaryDict[char][level]["monster"][monster] = {}
                for title in monsterTitles:
                    newMonster = monsters.monsterClass(monster, title)
                    newBoard = board.boardClass()
                    resultArr = []

                    for i in range(0, samples):
                        result = newBoard.doFight(newPlayer, newMonster)
                        resultArr.append(result)

                    unique, counts = np.unique(resultArr, return_counts=True)
                    print("\t",monster.capitalize()+" ("+newMonster.title+") Results:")
                    print("\t\t",dict(zip(unique, counts)))
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
                    print("\t\tWin Percentage:", str(winPercentage))
                    summaryDict[char][level]["monster"][monster][title] = winPercentage
                    if len(mostDifficult) == 0:
                        mostDifficult.append({"title": newMonster.title, "name": newMonster.name, "winPercentage": winPercentage})
                    elif len(mostDifficult) <= 10:
                        for i in range(0, len(mostDifficult)):
                            if winPercentage < mostDifficult[i]["winPercentage"]:
                                monsterInformation = {"title": newMonster.title, "name": newMonster.name, "winPercentage": winPercentage}
                                if i == 9:
                                    mostDifficult[i] = monsterInformation
                                else:
                                    mostDifficult.insert(i, monsterInformation)
                                    mostDifficult.pop()
                                break
                            elif len(mostDifficult) < 10:
                                mostDifficult.append({"title": newMonster.title, "name": newMonster.name, "winPercentage": winPercentage})
                                break

            print("\t\tHardest Monsters:",mostDifficult)
            # summaryDict[char][level]["hardestMonsters"] = mostDifficult
            print("\nOverall Win Percentage:", str(round((totalsArr["True"] / (samples * (len(monsterNames) * 3)) * 100), 2)))
            summaryDict[char][level]["overall"] = round((totalsArr["True"] / (samples * (len(monsterNames) * 3)) * 100), 2)
            print("\n")
        print("\n")
    f.close()
    sys.stdout = printToConsole
    print(summaryDict)
    heatmapGenerator.main(summaryDict, os.path.dirname(__file__))
    pass

startTime = time.time()
boardPlayTest()
# bossFightTest(False)
# monsterPlayTest(False)
print("--- Code Finished in %s seconds ---" % (time.time() - startTime))