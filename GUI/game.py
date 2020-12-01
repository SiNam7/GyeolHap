from PyQt5.QtWidgets import *
from GUI.layout import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QGridLayout()

        self.l = LogLayout()
        tl = TileLayout(self)
        pl1 = PlayerLayout(self)
        pl2 = PlayerLayout(self)
        self.al = AnswerLayout(self)

        mainLayout.addLayout(self.l, 0, 0)
        mainLayout.addLayout(tl, 0, 1)
        mainLayout.addLayout(pl1, 1, 0)
        mainLayout.addLayout(self.al, 1, 1)
        mainLayout.addLayout(pl2, 1, 2)

        self.setGeometry(300, 300, 450, 350)
        self.setLayout(mainLayout)
        self.show()

    def buttonClicked(self):
        btn = self.sender()
        key = btn.text()
        # TODO Connect to gyeolhap.py
        if key == "Hap":
            print("Hap")
            #TODO Call Plyername
            temp = self.al.answerSet
            self.l.addTable("player1", temp)

        elif key == "Gyeol":
            print("Gyeol")

    #TODO 이 방식대로 진행할지 아님 인스턴스에 담긴 집합을 직접 불러와 수정하면서 진행할지
    def slot_toggle(self, state):
        btn = self.sender()
        if state:
            answerSet = self.al.addAnswerSet(int(btn.toolTip()))
            self.al.setAnwerEdit(answerSet)
        else:
            answerSet = self.al.removeAnswerSet(int(btn.toolTip()))
            self.al.setAnwerEdit(answerSet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
