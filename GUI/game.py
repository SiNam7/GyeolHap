import sys, time
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from GUI.UI import functionList, roundList, Tile
from Logic.gyeolhap import Round

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        """점수 저장 + 시간 기록 레이아웃"""
        self.scoreLayout = QHBoxLayout()

        self.player1NameLabel = QLabel("Player1")
        self.player1NameLabel.setFont(QFont("Arial", 15))
        self.player1ScoreEdit = LineEdit()

        self.player2NameLabel = QLabel("Player2")
        self.player2NameLabel.setFont(QFont("Arial", 15))
        self.player2ScoreEdit = LineEdit()

        self.timeNameLabel = QLabel("Time")
        self.timeNameLabel.setFont(QFont("Arial", 15))
        self.timeEdit = LineEdit()

        self.scoreLayout.addWidget(self.player1NameLabel)
        self.scoreLayout.addWidget(self.player1ScoreEdit)
        self.scoreLayout.addStretch()

        self.scoreLayout.addWidget(self.timeNameLabel)
        self.scoreLayout.addWidget(self.timeEdit)
        self.scoreLayout.addStretch()

        self.scoreLayout.addWidget(self.player2NameLabel)
        self.scoreLayout.addWidget(self.player2ScoreEdit)

        """센터 레이아웃"""
        self.centerLayout = QGridLayout()

        self.roundLabel = QLabel('Round 1')  # 라운드 변경 함수 추가
        self.roundLabel.setFont(QFont("Arial", 15))

        # TODO make row, column setting funciton
        figureLayout = QGridLayout()
        r, c = 0, 0
        cnt = 1

        for key in Round.tileList:
            Qicon = QIcon(Tile.tileDict[key][3])

            figureButton = QPushButton(self)
            figureButton.setIcon(Qicon)
            figureButton.setToolTip(str(cnt))
            figureButton.setCheckable(True)
            figureButton.resize(30, 30)
            figureButton.clicked[bool].connect(self.slot_toggle)

            self.figureLayout.addWidget(figureButton, r, c)
            r += 1
            if r >= 3:
                r = 0
                c += 1

        self.logLayout = QVBoxLayout()
        self.logLabel = QLabel('Log')
        self.logLabel.setFont(QFont("Arial", 15))
        self.logLayout.addWidget(self.logLabel)

        self.centerLayout.addWidget(self.roundLabel, 0, 0)
        self.centerLayout.addLayout(figureLayout, 0, 1)
        self.centerLayout.addLayout(self.logLayout, 0, 2)

        self.answerEdit = LineEdit()
        self.answerSet = {}

        self.buttonLayout = QGridLayout()
        self.numLayout = QGridLayout()
        self.funLayout = QVBoxLayout()

        r, c = 0, 0

        for num in range(1, 10):
            button = Button(str(num), self.buttonClicked)
            self.numLayout.addWidget(button, r, c)
            c += 1
            if c >= 3:
                c = 0
                r += 1

        for func in functionList:
            button = Button(func, self.buttonClicked)
            self.funLayout.addWidget(button)

        self.buttonLayout.addLayout(self.numLayout, 0, 0)
        self.buttonLayout.addLayout(self.funLayout, 0, 1)

        mainLayout = QGridLayout()

        mainLayout.addLayout(self.scoreLayout, 0, 0)
        mainLayout.addLayout(self.centerLayout, 1, 0)
        mainLayout.addWidget(self.answerEdit, 2, 0)
        mainLayout.addLayout(self.buttonLayout, 3, 0)

        self.setLayout(mainLayout)
        self.setGeometry(300, 300, 450, 450)
        self.show()

    #TODO add enter function / Call logPrint, Pass the key to logic.checkHap
    def buttonClicked(self):
        btn = self.sender()
        key = btn.text()
        if key == 'Gyeol':
            return 0
        elif key == 'Hap':
            result = map(int, self.answerEdit.text())
        elif key == "del":
            self.answerEdit.setText(self.answerEdit.text()[:-1])
        elif key == "clear":
            self.answerEdit.setText('0')
        elif self.answerEdit.text() == '0':
            self.answerEdit.setText(key)
        else:
            if len(self.answerEdit.text()) >= 3:
                return 0
            self.answerEdit.setText(self.answerEdit.text() + key)

    # TODO add enter function / Call logPrint, Pass the key to logic.checkHap
    def keyPressEvent(self, e):
        """Receives keyboard input and outputs"""
        try:
            if e.key() == Qt.Key_Escape:
                self.close()
            elif e.key() == Qt.Key_Backspace:
                self.answerEdit.setText(self.answerEdit.text()[:-1])
            elif len(self.answerEdit.text()) <= 2 and int(e.text()) in range(10):
                if self.answerEdit.text() == '0':
                    self.answerEdit.setText(e.text())
                else:
                    self.answerEdit.setText(self.answerEdit.text() + e.text())
        except ValueError as e:
            self.answerEdit.setText("Only numbers can be entered")

    def slot_toggle(self, state):
        btn = self.sender()
        if state:
            self.answerSet.add(int(btn.toolTip()))
            self.answerEdit.setText(str(self.answerSet))  # textEdit 출력을 정하는 함수 - 길이가 3이상이면 출력 x - 출력형식 다듬기
        else:
            self.answerSet.remove(int(btn.toolTip()))
            self.answerEdit.setText(str(self.answerSet))

    # TODO Add at after checkGyeol & add decision win and lose at after "else:"
    def roundPrint(self, before):
        """To mark next round when called"""
        temp = roundList[int(before[-1])]
        if temp <= 8:
            self.roundLabel.setText(temp)

    def setScore(self, score1, score2):
        """set player1ScoreEdit and player2ScoreEdit"""
        self.player1ScoreEdit.setText(score1)
        self.player2ScoreEdit.setText(score2)

    # TODO Add at after checkGyeol & adjustsize 이용
    def logProduce(self, s: set):
        self.logEdit = LineEdit()
        self.logEdit.setText(s)
        self.logLayout.addWidget(self.logEdit)

    # TODO 온라인 구현 할 때 추가 & QBasictimer module
    def timePrint(self):
        start = time.time()
        while t > 0:
            t = 30 - (time.time() - start)
            self.timeEdit.setText(t)
        self.timeEdit.setText("Time Over")


class Button(QPushButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class LineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setText('0')
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
