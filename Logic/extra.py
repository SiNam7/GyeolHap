from random import random

from Logic.gyeolhap import Round


class Player:
    def __init__(self, name=None):
        self.game = None
        self.__name = 'player' if name is None else name
        self.__score = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score: int):
        self.score = score

    # TODO sudo-code / determine type of answer (string or list or set)
    def submitAnswer(self, answerType: str, answer: set = None):  # answerType: 'G'결 / 'H'합
        if answerType == 'H':
            self.game.checkHap(answer)
        elif answerType == 'G':
            self.game.checkGyeol()


def addBotPlayer() -> Player:
    return Player('Bot')


def botSolveAlgorithm(r: Round) -> set:
    answerSet = set(r.answerSet)
    answerLog = set(r.answerLog)

    possibleAnswer = answerSet - answerLog
    return random.sample(possibleAnswer, 1)
