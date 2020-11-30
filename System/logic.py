import random
from System.gyeolhap import Round


def checkHap(r: Round, submitAnswer: set):
    possibleAnswers = set(r.answerSet) - set(r.answerLog)
    return True if submitAnswer in possibleAnswers else False


def checkGyeol(r: Round):
    return True if len(r.answerLog) == len(r.answerSet) else False


# TODO 봇 플레이어의 답안 제출 알고리즘
def botSolveAlgorithm(r: Round):
    answerSet = set(r.answerSet)
    answerLog = set(r.answerLog)

    possibleAnswer = answerSet - answerLog
    if len(possibleAnswer) == 0:
        pass
        # bot.submitAnswer("G")
    else:
        pass
        # bot.submitAnswer("H", random.sample(possibleAnswer, 1))
