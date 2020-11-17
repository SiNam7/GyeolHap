from UI.game.tile import tiles
from .gyeolhap import Round


# TODO removal of reducdancy
def calculateHap(answerSet) -> bool:

    background = set()
    for tile in answerSet:
        background.add(tile.background)

    if len(background) == 3:
        pass
    else:
        return False

    shape = set()
    for tile in answerSet:
        shape.add(tile.shape)

    if len(shape) == 3:
        pass
    else:
        return False

    color = set()
    for tile in answerSet:
        color.add(tile.color)

    if len(color) == 3:
        pass
    else:
        return False

    return True


def checkHap(answerSet: set, roundfigure: Round) -> bool:
    if answerSet in roundfigure.answerSet:
        roundfigure.answerLog.append(answerSet)
        return True


def checkGyeol(roundfigure: Round) -> bool:
    return True if len(roundfigure.answerLog) == len(roundfigure.answerSet) else False
