from . import logic

class Player:
    def __init__(self, name=None):
        self.game = None
        self.name = 'player' if name is None else name
        self.score = 0

    def submitAnswer(self, answerType: str, answer: set = None):  # answerType: 'G'결 / 'H'합
        if answerType == 'H':
            logic.checkHap(self, answer)
        elif answerType == 'G':
            logic.checkGyeol(self)


def addBotPlayer() -> Player:
    return Player('Bot')
