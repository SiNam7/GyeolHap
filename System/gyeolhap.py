# from typing import List
from System import logic
from System.logic import Round
from System.extra import Player
# from UI import ui


class Gyeolhap:

    rounds = 10
    # roundFigures: list[Round]
    timeout = 60  # seconds
    score = {'G': 1, 'H': 3}
    penalty = {'G': 1, 'H': 1}
    gyeolConfirmed = False
    players = []

    # default game start method: Gyeolhap(player1, player2)
    def __init__(self, player1: Player, player2: Player):

        # Player setup
        self.players = [player1, player2]
        for player in self.players:
            player.game = self
        # self.startplayer = self.players[random.randint(0, 2)]
        self.startplayer = player1

        # Round figure setup
        self.roundFigures = []
        for _ in range(self.rounds):
            self.roundFigures.append(Round())

        logic.roundFigures = self.roundFigures

        # Game start
        self.currentround = 1
        while self.currentround <= self.rounds:
            self.currentfigure = self.roundFigures[self.currentround - 1]
            # TODO sudo-code / add tiles to figureLayout
            pass

            while self.gyeolConfirmed is not True:
                pass
                # DEBUG
                self.gyeolConfirmed = True

            self.gyeolConfirmed = False
            self.currentround += 1

        # TODO / Game over
        pass

    @classmethod
    # custom game start method: Gyeolhap.customSetting(player1, player2, rounds, timeouts, score, penalty)
    def customSetting(cls, player1: Player, player2: Player, rounds: int, timeout: int, score: dict, penalty: dict):
        cls.rounds = rounds
        cls.timeout = timeout
        cls.score = score
        cls.penalty = penalty

        return cls(player1, player2)

    @classmethod
    # debug running setting: Gyeolhap()
    def defaultSetting(cls):
        cls.player1 = Player('A')
        cls.player2 = Player('B')

        return cls(cls.player1, cls.player2)


if __name__ == "__main__":
    game = Gyeolhap(Player('A'), Player('B'))
    print("Success")
