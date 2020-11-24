import itertools
import random

from GUI.UI import Tile
from System.extra import Player

# [(0, 'Square/Blue/White'), (1, ...]
allTileDictionary = [(i, k) for i, k in enumerate(Tile().tileDict.keys())]
roundFigures = []

class Round:
    # tileDict = {}
    # answerSet: list = []
    # answerLog: list = []

    def __init__(self):
        self.tileDict = {}  # {0: 'Triangle/Blue/Gray' (random), 1: ... }
        self.answerSet: list = []
        self.answerLog: list = []

        tileNo = []
        while len(tileNo) < 9:
            rand = random.randint(0, 26)
            if rand not in tileNo:
                tileNo.append(rand)

        for i, e in enumerate(tileNo):
            self.tileDict[i] = allTileDictionary[e][1]

        # TODO / pre-calculate all possible answer set, and save it to answerSet
        self.calculateHap()

    def calculateHap(self):
        possibleSets = set(itertools.combinations(range(9), 3))  # 숫자 3개
        for entry in possibleSets:
            notAnswer = False
            for i in range(0, 3):  # 0: shape, 1: color, 2: background
                e = set()
                for number in entry:
                    tileinfo = self.tileDict[number].split('/')
                    e.add(tileinfo[i])

                if len(entry) == 3:
                    pass
                else:
                    notAnswer = True
                    break
            if notAnswer:
                break

            self.answerSet.append(set(entry))


def checkHap(player: Player, submitAnswer: set):
    roundfigure = player.game.currentfigure
    if submitAnswer in roundfigure.answerSet:
        roundfigure.answerLog.append(submitAnswer)
        player.score += player.game.score['H']
        # TODO / add Changing turn functions
    else:
        player.score -= player.game.penalty['H']


def checkGyeol(player: Player):
    roundfigure = player.game.currentfigure
    if len(roundfigure.answerLog) == len(roundfigure.answerSet):
        player.score += player.game.score['G']
        player.game.gyeolConfirmed = True
        # TODO / add Changing turn functions
    else:
        player.score -= player.game.penalty['G']


def botSolveAlgorithm(bot: Player, r: Round):
    answerSet = set(r.answerSet)
    answerLog = set(r.answerLog)

    possibleAnswer = answerSet - answerLog
    if len(possibleAnswer) == 0:
        bot.submitAnswer("G")
    else:
        bot.submitAnswer("H", random.sample(possibleAnswer, 1))


