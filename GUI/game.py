from PyQt5.QtWidgets import QWidget, QGridLayout
from GUI.layout import *
from System.gyeolhap import Gyeolhap, Player
from System.bot import botSolveAlgorithm
import sys
import traceback


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.playerDict = {1: [Player("You"), PlayerLayout(self)], 2: [Player("Bot"), PlayerLayout(self)]}

        self.gl = Gyeolhap(self.playerDict[1][0], self.playerDict[2][0])

        self.mainLayout = QGridLayout()

        self.l = LogLayout()
        self.tl = TileLayout(self, self.gl)
        self.al = AnswerLayout(self)

        self.playerDict[1][1].setUserLabel(self.playerDict[1][0].name)
        self.playerDict[2][1].setUserLabel(self.playerDict[2][0].name)

        self.mainLayout.addLayout(self.l, 0, 0)
        self.mainLayout.addLayout(self.tl, 0, 1)
        self.mainLayout.addLayout(self.playerDict[1][1], 1, 0)
        self.mainLayout.addLayout(self.al, 1, 1)
        self.mainLayout.addLayout(self.playerDict[2][1], 1, 2)

        self.isSinglePlay = True

        self.setGeometry(300, 300, 450, 350)
        self.setLayout(self.mainLayout)
        self.setWindowTitle("Gyeolhap Game")
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def buttonClicked(self):
        try:
            btn = self.sender()
            key = btn.text()
            print(self.gl.currentround)

            player = self.playerDict[1]
            if player[0].turn is False:
                return

            if key == "Hap":
                if player[0].submitAnswer("H", self.al.answerSet):
                    self.hapCorrect(player)
                else:
                    self.wrong(player)
            elif key == "Gyeol":
                if player[0].submitAnswer("G", self.al.answerSet):
                    self.gyeolCorrect(player)
                else:
                    self.wrong(player)
            self.turnChange(self.playerDict[1][0], self.playerDict[2][0])
        except Exception as e:
            traceback.print_exc()

    def slot_toggle(self, state):
        btn = self.sender()
        if state:
            answerSet = self.al.addAnswerSet(int(btn.toolTip()))
            self.al.setAnwerEdit(answerSet)
        else:
            answerSet = self.al.removeAnswerSet(int(btn.toolTip()))
            self.al.setAnwerEdit(answerSet)

    def hapCorrect(self, p, answer=None):
        if answer is None:
            temp = self.al.answerSet
            self.l.addTable(p[0].name, temp)
            p[1].setUserScoreLabel(str(p[0].score))
        else:
            self.l.addTable(p[0].name, answer)
            p[1].setUserScoreLabel(str(p[0].score))

    def gyeolCorrect(self, p):
        self.gl.gyeolConfirmed = True
        p[1].setUserScoreLabel(str(p[0].score))
        self.gl.currentround += 1

        if self.gl.currentround > self.gl.rounds:
            return 0

        self.gl.currentfigure = self.gl.roundFigures[self.gl.currentround - 1]

        self.l.setRound(self.gl.currentround)
        self.l.createTable()

        self.tl = TileLayout(self, self.gl)
        self.mainLayout.addLayout(self.tl, 0, 1)

        self.al.setAnwerEdit("")

    def wrong(self, p):
        p[1].setUserScoreLabel(str(p[0].score))

    def turnChange(self, p1: Player, p2: Player):
        if self.isSinglePlay is False:
            if p1.turn:
                p1.turn = False
                p2.turn = True
            else:
                p1.turn = True
                p2.turn = False
        else:
            result, answerType, answer = botSolveAlgorithm(self.gl.currentfigure.answerSet, self.playerDict[2][0])

            player = self.playerDict[2]

            if answerType == "Hap":
                if result:
                    self.hapCorrect(player, answer=answer)
                else:
                    self.wrong(player)
            elif answerType == "Gyeol":
                if result:
                    self.gyeolCorrect(player)
                else:
                    self.wrong(player)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
