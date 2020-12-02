from System.gyeolhap import Player
import random

# TODO 봇 플레이어의 답안 제출 알고리즘
def botSolveAlgorithm(answerSet, bot: Player):
    if len(answerSet) == 0:
        pass
        return bot.submitAnswer("G"), "Gyeol", None
    else:
        pass
        temp = random.sample(answerSet, 1)
        return bot.submitAnswer("H", *temp), "Hap", *temp
