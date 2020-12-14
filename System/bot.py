from System.gyeolhap import Player
import random


# TODO 봇 플레이어의 답안 제출 알고리즘
def botSolveAlgorithm(answerSet, bot: Player, correctRatio: dict):
    if len(answerSet) == 0:
        if random.randint(1, 100) <= 100 - correctRatio['G']:
            temp = [{0, 1, 2}]
            return bot.submitAnswer("H", *temp), "Hap", *temp  # Wrong Answer
        return bot.submitAnswer("G"), "Gyeol", None  # Correct Answer
    else:
        if random.randint(1, 100) <= 100 - correctRatio['H']:
            return bot.submitAnswer("G"), "Gyeol", None  # Wrong Answer
        temp = random.sample(answerSet, 1)
        return bot.submitAnswer("H", *temp), "Hap", *temp  # Correct Answer
