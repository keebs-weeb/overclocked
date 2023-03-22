import random

class monsterClass:
    def __init__(self, monsterZone=False, monsterName=False):
        monsterNames = [['bird man', 'scorpion', 'zombie'], ['necromancer', 'ghost', 'royal archer'], ['baby drake', 'royal knight', 'ogre']]
        # monsterTitles = ["normal", "normal", "normal", "normal", "lesser", "lesser", "lesser", "greater", "greater"]

        self.zone = int(monsterZone) if monsterZone else int(random.randint(0, len(monsterNames)))
        self.name = monsterName if monsterName else random.choice(monsterNames[self.zone])
        # self.title = monsterTitle if monsterTitle else random.choice(monsterTitles)
        self.health = self.monsterStats(self.name)["health"]
        self.damage = self.monsterStats(self.name)["damage"]
        # self.levelHealth = self.monsterStats(self.name)["level"]["health"]
        # self.levelDamage = self.monsterStats(self.name)["level"]["damage"]

    def monsterStats(self, monsterName):
        statsDict = {
            "bird man": {
                "health": 7,
                "damage": 1,
            },
            "scorpion": {
                "health": 2,
                "damage": 6,
            },
            "zombie": {
                "health": 4,
                "damage": 1,
            },
            "ghost": {
                "health": 9,
                "damage": 1,
            },
            "necromancer": {
                "health": 6,
                "damage": 2,
            },
            "royal archer": {
                "health": 14,
                "damage": 2,
            },
            "royal knight": {
                "health": 14,
                "damage": 2,
            },
            "ogre": {
                "health": 12,
                "damage": 3,
            },
            "baby drake": {
                "health": 18,
                "damage": 3,
            }
        }
        return statsDict[monsterName]
    
    def getNamesArr(self):
        arr = []
        for key in self.monsterStats:
            arr.append(key)
        return arr
    
    # def monsterTitleStats(self):
    #     statsDict = {
    #         "lesser": {
    #             "base": {
    #                 "health": -1,
    #                 "damage": -1
    #             },
    #             "level": {
    #                 "health": 0,
    #                 "damage": 0
    #             }
    #         },
    #         "normal": {
    #             "base": {
    #                 "health": 0,
    #                 "damage": 0
    #             },
    #             "level": {
    #                 "health": 0,
    #                 "damage": 0
    #             }
    #         },
    #         "greater": {
    #             "base": {
    #                 "health": 0,
    #                 "damage": 0
    #             },
    #             "level": {
    #                 "health": 1,
    #                 "damage": 1
    #             }
    #         }
    #     }
    #     return statsDict

    def getStats(self):
        return {
            "health": self.health,
            "damage": self.damage
        }

    def calcStat(self, statName):
        stats = self.getStats()
        base = stats[statName]
        return base