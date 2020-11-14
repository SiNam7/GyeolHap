import sys, random
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from GUI.UI import imagePathList

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        """점수 저장 + 시간 기록 레이아웃"""
        self.scoreLayout = QHBoxLayout()

        self.player1NameLabel = QLabel("Player1")
        self.player1NameLabel.setFont(QFont("Arial", 15))
        self.player1ScoreEdit = QLineEdit('0')
        self.player1ScoreEdit.setReadOnly(True)
        self.player1ScoreEdit.setAlignment(Qt.AlignCenter)

        self.player2NameLabel = QLabel("Player2")
        self.player2NameLabel.setFont(QFont("Arial", 15))
        self.player2ScoreEdit = QLineEdit('0')
        self.player2ScoreEdit.setReadOnly(True)
        self.player2ScoreEdit.setAlignment(Qt.AlignCenter)

        self.timeNameLabel = QLabel("Time")
        self.timeNameLabel.setFont(QFont("Arial", 15))
        self.timeEdit = QLineEdit('0')
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setAlignment(Qt.AlignCenter)

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

        self.logLayout = QGridLayout()

        self.centerLayout.addWidget(self.roundLabel, 0, 0)
        self.centerLayout.addLayout(self.figureLayout, 0, 1)
        self.centerLayout.addLayout(self.logLayout, 0, 2)

        """메인 레이아웃"""
        mainLayout = QGridLayout()

        mainLayout.addLayout(self.scoreLayout, 0, 0)
        mainLayout.addLayout(self.centerLayout, 1, 0)

        self.setLayout(mainLayout)
        self.setGeometry(300, 300, 450, 450)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
