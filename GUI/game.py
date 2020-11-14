import sys, random
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from GUI.UI import imagePathList, functionList

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

        self.figureLayout = QGridLayout()
        randomList = random.sample([i for i in range(27)], 9)
        r, c = 0, 0

        for randomnum in randomList:
            pixmap = QPixmap(imagePathList[randomnum])
            pixmap = pixmap.scaledToHeight(50)

            figureLabel = QLabel(self)
            figureLabel.setPixmap(pixmap)

            self.figureLayout.addWidget(figureLabel, r, c)
            r += 1

            if r >= 3:
                r = 0
                c += 1

        self.logLayout = QVBoxLayout()

        for i in range(12):
            edit = LineEdit()
            self.logLayout.addWidget(edit)

        self.centerLayout.addWidget(self.roundLabel, 0, 0)
        self.centerLayout.addLayout(self.figureLayout, 0, 1)
        self.centerLayout.addLayout(self.logLayout, 0, 2)

        self.answerEdit = LineEdit()

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

    def buttonClicked(self):
        btn = self.sender()
        key = btn.text()
        if key == 'enter':
            return 0
        elif key == "del":
            newtext = self.answerEdit.text()[:-1]
            self.answerEdit.setText(newtext)
        elif key == "clear":
            self.answerEdit.setText('0')
        elif self.answerEdit.text() == '0':
            self.answerEdit.setText(key)
        else:
            if len(self.answerEdit.text()) >= 3:
                return 0
            self.answerEdit.setText(self.answerEdit.text() + key)



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
