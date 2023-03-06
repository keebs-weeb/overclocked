import random

class bossClass:
    bossNames = ["dragon", "rogue warrior", "demon", "very large fish"]
    def __init__(self, bossName=random.choice(bossNames)):
        self.name = bossName
        self.baseHealth = self.bossStats(bossName)["base"]["health"]
        self.baseDamage = self.bossStats(bossName)["base"]["damage"]
        self.levelHealth = self.bossStats(bossName)["level"]["health"]
        self.levelDamage = self.bossStats(bossName)["level"]["damage"]

    def bossStats(self, bossName):
        statsDict = {
            "dragon": {
                "base": {
                    "health": 16,
                    "damage": 8,
                },
                "level": {
                    "health": 1,
                    "damage": 2,
                }
            },
            "rogue warrior": {
                "base": {
                    "health": 14,
                    "damage": 7,
                },
                "level": {
                    "health": 1,
                    "damage": 2,
                }
            },
            "demon": {
                "base": {
                    "health": 15,
                    "damage": 6,
                },
                "level": {
                    "health": 1,
                    "damage": 1,
                }
            },
            "very large fish": {
                "base": {
                    "health": 18,
                    "damage": 5,
                },
                "level": {
                    "health": 0,
                    "damage": 1,
                }
            },
        }
        return statsDict[bossName]
    
    def getNamesArr(self):
        arr = []
        for key in self.bossStats:
            arr.append(key)
        return arr

    def getStats(self):
        return {
            "baseHealth": self.baseHealth,
            "baseDamage": self.baseDamage,
            "levelHealth": self.levelHealth,
            "levelDamage": self.levelDamage
        }

    def calcStat(self, statName, playerCharacter):
        curLevel = playerCharacter.level
        stats = self.getStats()
        base = stats["base"+statName.capitalize()]
        level = stats["level"+statName.capitalize()] * curLevel
        return base + level