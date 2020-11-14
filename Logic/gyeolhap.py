import itertools
from random import random
from typing import List

from . import logic
from .extra import Player
from UI.game.tile import figure
from UI import ui


class Round:

    tileList = []
    answerSet: List[set] = []
    answerLog: List[set] = {}

    def __init__(self):
        tileNo = []
        while len(tileNo) < 9:
            rand = random.randint(0, 27)
            if rand not in tileNo:
                tileNo.append(rand)

        # TODO sudo-code / get figure from 'Tiles'
        tileList = []
        for i in tileNo:
            tileList.append(figure[i])

        self.tileList = tileList

        # TODO / pre-calculate all possible answer set, and save it to answerSet
        self.calculateHap()

    def calculateHap(self):
        possibleSets = list(itertools.combinations(self.tileList, 3))

        for possibleSet in possibleSets:
            logic.calculateHap(possibleSet)


class Gyeolhap:

    rounds = 10
    roundFigures: List[Round]
    timeout = 60  # seconds
    score = {'G': 1, 'H': 3}
    penalty = {'G': 1, 'H': 1}

    # default game start method: Gyeolhap(player1, player2)
    def __init__(self, player1: Player, player2: Player):

        self.players = (player1, player2)
        for player in self.players:
            player.game = self
        self.startplayer = self.players[random.randint(0, 2)]

        self.roundFigures = []
        for _ in range(self.rounds):
            self.roundFigures.append = Round()

        self.currentround = 1
        while self.currentround <= self.rounds:
            self.currentfigure = self.roundFigures[self.currentround - 1]
            # TODO sudo-code / add tiles to figureLayout
            ui.figureLayout.addFigure(self.currentfigure)

            while True:
                # TODO / break when Gyeol confirmed
                pass

            # TODO / go next round

    @classmethod
    # custom game start method: Gyeolhap.customSetting(player1, player2, rounds, timeouts, score, penalty)
    def customSetting(cls, player1: Player, player2: Player, rounds: int, timeout: int, score: dict, penalty: dict):
        cls.rounds = rounds
        cls.timeout = timeout
        cls.score = score
        cls.penalty = penalty

        return cls(player1, player2)

    def checkHap(self, player, answerlist):
        if logic.checkHap(answerlist, self.currentfigure):
            player.score += self.score['H']
        else:
            player.score -= self.penalty['H']

    def checkGyeol(self, player):
        if logic.checkGyeol(self.currentfigure):
            player.score += self.score['G']
            # TODO / go to next round
            pass
        else:
            player.score -= self.penalty['G']
