import random

class playerClass:
    def __init__(self, characterName):
        self.level = 0
        self.name = characterName
        self.curSpace = 0
        self.timesMoved = 0
        self.defeatCounter = {
            "boss": {
                "total": 0
            }, 
            "monster": {
                "total": 0
            }, 
        }
        self.attemptedMove = 0
        self.baseHealth = self.classStats(characterName)["base"]["health"]
        self.baseMove = self.classStats(characterName)["base"]["move"]
        self.baseDamage = self.classStats(characterName)["base"]["damage"]
        self.levelHealth = self.classStats(characterName)["level"]["health"]
        self.levelMove = self.classStats(characterName)["level"]["move"]
        self.levelDamage = self.classStats(characterName)["level"]["damage"]
        self.modHealth = 0
        self.modMove = 0
        self.modDamage = 0

    def classStats(self, className):
        statsDict = {
            "swordsman": {
                "base": {
                    "health": 4,
                    "move": 0,
                    "damage": 0,
                },
                "level": {
                    "health": 1,
                    "move": 1,
                    "damage": 1,
                }
            },
            "ranger": {
                "base": {
                    "health": 3,
                    "move": 2,
                    "damage": 0,
                },
                "level": {
                    "health": 1,
                    "move": 2,
                    "damage": 1,
                }
            },
            "barbarian": {
                "base": {
                    "health": 5,
                    "move": 0,
                    "damage": 0,
                },
                "level": {
                    "health": 2,
                    "move": 0,
                    "damage": 0,
                }
            },
            "mage": {
                "base": {
                    "health": 3,
                    "move": 1,
                    "damage": 0,
                },
                "level": {
                    "health": 0,
                    "move": 0,
                    "damage": 3,
                }
            }
        }
        return statsDict[className]
    
    def getNamesArr(self):
        arr = []
        for key in self.classStats:
            arr.append(key)
        return arr
    
    def getStats(self):
        return {
            "baseHealth": self.baseHealth,
            "baseMove": self.baseMove,
            "baseDamage": self.baseDamage,
            "levelHealth": self.levelHealth,
            "levelMove": self.levelMove,
            "levelDamage": self.levelDamage,
            "modHealth": self.modHealth,
            "modMove": self.modMove,
            "modDamage": self.modDamage
        }

    def calcStat(self, statName):
        curLevel = self.level
        stats = self.getStats()
        base = stats["base"+statName.capitalize()]
        level = stats["level"+statName.capitalize()] * curLevel
        mod = stats["mod"+statName.capitalize()]
        return base + level + mod

    def rollMove(self, playerMove=False):
        if not playerMove:
            playerMove = random.randint(1,6) + self.calcStat("move")
        return playerMove

    def rollDamage(self, playerDamage=False):
        if not playerDamage:
            playerDamage = random.randint(1,6) + self.calcStat("damage") 
        return playerDamage