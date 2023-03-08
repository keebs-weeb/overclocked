import random

class bossClass:
    def __init__(self, bossName=False):
        bossNames = ["dragon", "rogue warrior", "demon", "very large fish"]

        self.name = bossName if bossName else random.choice(bossNames)
        self.baseHealth = self.bossStats(self.name)["base"]["health"]
        self.baseDamage = self.bossStats(self.name)["base"]["damage"]
        self.levelHealth = self.bossStats(self.name)["level"]["health"]
        self.levelDamage = self.bossStats(self.name)["level"]["damage"]

    def bossStats(self, bossName):
        statsDict = {
            "dragon": {
                "base": {
                    "health": 13,
                    "damage": 3,
                },
                "level": {
                    "health": 2,
                    "damage": 4,
                }
            },
            "rogue warrior": {
                "base": {
                    "health": 16,
                    "damage": 6,
                },
                "level": {
                    "health": 2,
                    "damage": 1,
                }
            },
            "demon": {
                "base": {
                    "health": 18,
                    "damage": 6,
                },
                "level": {
                    "health": 3,
                    "damage": 1,
                }
            },
            "very large fish": {
                "base": {
                    "health": 24,
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