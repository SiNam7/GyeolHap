import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QPushButton, QTextEdit, QLineEdit, QLabel
from PyQt5.QtCore import Qt

from UI import playersName, playersKind

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()


        """점수 저장 + 시간 기록 레이아웃"""
        scoreLayout = QGridLayout()

        player1NameLabel = QLabel("Player1")
        player1ScoreEdit = QLineEdit('0')
        player1ScoreEdit.setReadOnly(True)
        player1ScoreEdit.setMaximumWidth(40)
        player1ScoreEdit.setAlignment(Qt.AlignCenter)

        player2NameLabel = QLabel("Player2")
        player2ScoreEdit = QLineEdit('0')
        player2ScoreEdit.setReadOnly(True)
        player2ScoreEdit.setMaximumWidth(40)
        player2ScoreEdit.setAlignment(Qt.AlignCenter)

        timeEdit = QLineEdit('0')
        timeEdit.setReadOnly(True)
        timeEdit.setMaximumWidth(40)
        timeEdit.setAlignment(Qt.AlignCenter)

        scoreLayout.addWidget(player1NameLabel, 0, 0)
        scoreLayout.addWidget(player1ScoreEdit, 1, 0)

        scoreLayout.addWidget(timeEdit, 1, 1)

        scoreLayout.addWidget(player2NameLabel, 0, 2)
        scoreLayout.addWidget(player2ScoreEdit, 1, 2)

        mainLayout = QGridLayout()

        mainLayout.addLayout(scoreLayout, 0, 0)

        self.setLayout(mainLayout)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
