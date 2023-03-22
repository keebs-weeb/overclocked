import random

class bossClass:
    def __init__(self, bossName=False):
        bossNames = ["rogue warrior", "very large fish", "demon", "maddened mage", "dragon"]

        self.name = bossName if bossName else random.choice(bossNames)
        self.health = self.bossStats(self.name)["health"]
        self.damage = self.bossStats(self.name)["damage"]

    def bossStats(self, bossName):
        statsDict = {
            "rogue warrior": {
                "health": 13,
                "damage": 1,
            },
            "very large fish": {
                "health": 23,
                "damage": 1,
            },
            "demon": {
                "health": 18,
                "damage": 2,
            },
            "maddened mage": {
                "health": 11,
                "damage": 4,
            },
            "dragon": {
                "health": 25,
                "damage": 3,
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
            "health": self.health,
            "damage": self.damage,
        }

    def calcStat(self, statName):
        stats = self.getStats()[statName]
        return stats