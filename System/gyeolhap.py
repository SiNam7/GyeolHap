# from typing import List
import itertools
from random import random, sample

from GUI.UI import Tile
from System import logic

allTileDictionary = [(i, k) for i, k in enumerate(Tile().tileDict.keys())]


class Player:
    """
    플레이어 정보를 담는 객체.
    :var self.game: 플레이어가 참가중인 게임 객체 정보
    :var self.name: 플레이어 이름, default='player'
    :var self.score: 플레이어의 현재 점수
    """

    def __init__(self, name=None):
        self.game = None
        self.name = 'player' if name is None else name
        self.score = 0
        self.turn = False

    def submitAnswer(self, answerType: str, answer: set = None) -> bool:  # answerType: 'G'결 / 'H'합
        """
        답안을 제출하는 함수. logic에서 답안을 처리한다.
        :param answerType: (합: 'H', 결: 'G')
        :param answer: answerType이 합('H')일 경우 제출한 답안 set
        :return: 정답: True, 오답: False
        """
        if answerType == 'H':
            if logic.checkHap(self.game.currentfigure.answerSet, answer) is True:
                self.score += Gyeolhap.score['H']
                self.game.currentfigure.answerLog += answer
                self.game.currentfigure.answerSet.remove(answer)
                return True
            else:
                self.score -= Gyeolhap.penalty['H']
                return False
        elif answerType == 'G':
            if logic.checkGyeol(self.game.currentfigure.answerSet) is True:
                self.score += Gyeolhap.score['G']
                Gyeolhap.gyeolConfirmed = True
                return True
            else:
                self.score -= Gyeolhap.penalty['G']
                return False
        else:
            print("Invaild answer Type:", answerType)
            return False  # TODO 예외처리 시 리턴값에 대해


def addBotPlayer() -> Player:
    """
    새 봇 플레이어 추가
    :return: 'Bot' 이름의 Player 객체
    """
    return Player('Bot')


class Gyeolhap:
    """
    :cvar rounds: 총 라운드 수 (정수)
    :cvar timeout: 제한시간 (초)
    :cvar score: {'G': ?, 'H': ?} 형태의 정답 시 얻는 점수
    :cvar penalty: {'G': ?, 'H': ?} 형태의 오답 시 잃는 점수
    :cvar gyeolConfirmed: '결'이 선언되면 True로 변경, 다음 라운드로 넘어가는 trigger

    :var self.players: 플레이어 객체를 담아두는 리스트.
    :var self.roundFigures: 라운드 객체를 담는 리스트.
    :var self.currentround: 현재 라운드 넘버.
    :var self.currentfigure: 현재 라운드에 해당하는 라운드 객체.
    :var self.startplayer: 선 플레이어.
    """
    rounds = 10
    timeout = 60  # seconds
    score = {'G': 3, 'H': 1}
    penalty = {'G': 1, 'H': 1}
    gyeolConfirmed = False
    GameStarted = True

    # default game start method: Gyeolhap(player1, player2)
    def __init__(self, player1: Player, player2: Player):
        """
        게임 정보를 담은 객체
        :param player1: 플레이어 1
        :param player2: 플레이어 2
        """
        # Player setup
        self.players = [player1, player2]
        for player in self.players:
            player.game = self
        # self.startplayer = self.players[random.randint(0, 2)]
        self.players[0].turn = True

        # Round figure setup
        self.roundFigures = []
        for _ in range(self.rounds):
            self.roundFigures.append(Round())

        # Game start
        if self.GameStarted:
            self.currentround = 1
            self.currentfigure = self.roundFigures[self.currentround - 1]
            self.GameStarted = False

        if self.currentround <= self.rounds:
            self.gyeolConfirmed = False

        else:
            #TODO
            pass

    @classmethod
    @DeprecationWarning  # (!) 아직 작동이 확인되지 않음
    # custom game start method: Gyeolhap.customSetting(player1, player2, rounds, timeouts, score, penalty)
    def customSetting(cls, player1: Player, player2: Player, rounds: int, timeout: int, score: dict, penalty: dict):
        """
        게임 환경을 커스텀하기 위한 메소드.
        :param player1: 플레이어 1 객체
        :param player2: 플레이어 2 객체
        :param rounds: 총 라운드 수 (정수)
        :param timeout: 제한시간 (초)
        :param score: {'G': ?, 'H': ?} 형태의 정답 시 얻는 점수
        :param penalty: {'G': ?, 'H': ?} 형태의 오답 시 잃는 점수
        :return: 클래스 객체를 리턴함.
        """
        cls.rounds = rounds
        cls.timeout = timeout
        cls.score = score
        cls.penalty = penalty

        return cls(player1, player2)

    @classmethod
    @DeprecationWarning  # (!) 아직 작동이 확인되지 않음
    # debug running setting: Gyeolhap()
    def defaultSetting(cls):
        cls.player1 = Player('A')
        cls.player2 = Player('B')

        return cls(cls.player1, cls.player2)


class Round:
    """
    라운드 정보를 관리하는 클래스. 객체 생성 시 아래 answerSet이 채워짐
    :var self.tileDict: 0~8번까지의 타일 정보를 담은 딕셔너리
    :var self.answerSet: 합에 해당하는 답안 목록 (요소가 set로 이루어진 리스트)
    :var self.answerLog: 제출한 정답 목록 (요소가 set로 이루어진 리스트)
    """
    def __init__(self):
        self.tileDict = {}  # {0: 'Triangle/Blue/Gray' (random), 1: ... }
        self.answerSet: list = []
        self.answerLog: list = []

        tileNo = sample(range(0, 27), 9)

        for i, e in enumerate(tileNo):
            self.tileDict[i] = allTileDictionary[e][1]

        self.calculateHap()

    def calculateHap(self):
        """
        가능한 합 전체를 계산해 self.answerSet에 저장
        """
        possibleSets = set(itertools.combinations(range(9), 3))  # 숫자 3개
        for entry in possibleSets:
            notAnswer = False
            for i in range(0, 3):  # 0: shape, 1: color, 2: background
                e = set()
                for number in entry:
                    tileinfo = self.tileDict[number].split('/')
                    e.add(tileinfo[i])

                if len(e) != 2:
                    pass
                else:
                    notAnswer = True
                    break
            if notAnswer:
                continue

            self.answerSet.append(set(entry))


if __name__ == "__main__":
    game = Gyeolhap(Player('A'), Player('B'))
    print("Success")
