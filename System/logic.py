def checkHap(answerSet, submitAnswer: set):
    return True if submitAnswer in answerSet else False


def checkGyeol(answerSet):
    return True if len(answerSet) == 0 else False
