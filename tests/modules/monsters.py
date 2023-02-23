import random

class monsterClass:
    monsterNames = ['bird man', 'ghost', 'necromancer', 'royal archer', 'royal knight', 'ogre', 'scorpion', 'zombie']
    monsterTitles = ["normal", "normal", "normal", "normal", "lesser", "lesser", "lesser", "greater", "greater"]
    def __init__(self, monsterName=random.choice(monsterNames), monsterTitle=random.choice(monsterTitles)):
        self.name = monsterName
        self.title = "normal"
        self.baseHealth = self.monsterStats(monsterName)["base"]["health"]
        self.baseDamage = self.monsterStats(monsterName)["base"]["damage"]
        self.levelHealth = self.monsterStats(monsterName)["level"]["health"]
        self.levelDamage = self.monsterStats(monsterName)["level"]["damage"]

    def monsterStats(self, monsterName):
        statsDict = {
            "bird man": {
                "base": {
                    "health": 13,
                    "damage": 8,
                },
                "level": {
                    "health": 1,
                    "damage": 2,
                }
            },
            "ghost": {
                "base": {
                    "health": 13,
                    "damage": 8,
                },
                "level": {
                    "health": 1,
                    "damage": 1,
                }
            },
            "necromancer": {
                "base": {
                    "health": 12,
                    "damage": 8,
                },
                "level": {
                    "health": 1,
                    "damage": 2,
                }
            },
            "royal archer": {
                "base": {
                    "health": 15,
                    "damage": 7,
                },
                "level": {
                    "health": 2,
                    "damage": 2,
                }
            },
            "royal knight": {
                "base": {
                    "health": 15,
                    "damage": 7,
                },
                "level": {
                    "health": 3,
                    "damage": 2,
                }
            },
            "ogre": {
                "base": {
                    "health": 16,
                    "damage": 6,
                },
                "level": {
                    "health": 1,
                    "damage": 2,
                }
            },
            "scorpion": {
                "base": {
                    "health": 4,
                    "damage": 15,
                },
                "level": {
                    "health": 3,
                    "damage": 3,
                }
            },
            "zombie": {
                "base": {
                    "health": 12,
                    "damage": 5,
                },
                "level": {
                    "health": 2,
                    "damage": 1,
                }
            },
        }
        return statsDict[monsterName]
    
    def getNamesArr(self):
        arr = []
        for key in self.monsterStats:
            arr.append(key)
        return arr
    
    def monsterTitleStats(self):
        statsDict = {
            "lesser": {
                "base": {
                    "health": -1,
                    "damage": -1
                },
                "level": {
                    "health": -2,
                    "damage": -2
                }
            },
            "normal": {
                "base": {
                    "health": 0,
                    "damage": 0
                },
                "level": {
                    "health": 0,
                    "damage": 0
                }
            },
            "greater": {
                "base": {
                    "health": 1,
                    "damage": 1
                },
                "level": {
                    "health": 1,
                    "damage": 1
                }
            }
        }
        return statsDict

    def getStats(self):
        return {
            "baseHealth": self.baseHealth+self.monsterTitleStats()[self.title]["base"]["health"],
            "baseDamage": self.baseDamage+self.monsterTitleStats()[self.title]["base"]["damage"],
            "levelHealth": self.levelHealth+self.monsterTitleStats()[self.title]["level"]["health"],
            "levelDamage": self.levelDamage+self.monsterTitleStats()[self.title]["level"]["damage"]
        }

    def calcStat(self, statName, playerCharacter):
        curLevel = playerCharacter.level
        stats = self.getStats()
        base = stats["base"+statName.capitalize()]
        level = stats["level"+statName.capitalize()] * curLevel
        return base + level