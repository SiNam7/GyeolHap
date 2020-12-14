from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.Qt import QSize
from System.gyeolhap import Gyeolhap
from GUI.UI import Tile


class LogLayout(QGridLayout):
    def __init__(self):
        super().__init__()
        self.row = 0
        self.column = 2

        #TODO 코드 반복 줄이기
        self.roundLayout = QHBoxLayout()

        self.roundLabel = QLabel("1 round")
        self.roundLabel.setFont(QFont("Arial", 15))
        self.roundLayout.addStretch()
        self.roundLayout.addWidget(self.roundLabel)
        self.roundLayout.addStretch()

        self.createTable()

        self.addLayout(self.roundLayout, 0, 0)

    def createTable(self):
        self.table = QTableWidget()
        self.table.setRowCount(self.row)
        self.table.setColumnCount(self.column)
        self.table.setHorizontalHeaderLabels(("Player", "Hap"))
        self.table.resizeRowsToContents()
        self.addWidget(self.table, 1, 0)

    def addTable(self, player, hap):
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        self.table.setItem(rowPosition, 0, QTableWidgetItem(player))
        self.table.setItem(rowPosition, 1, QTableWidgetItem(str(hap)))


    def setRound(self, i):
        """
        set RoundLabel
        :param i:  round number
        :return: none
        """
        i = str(i) + "round"
        self.roundLabel.setText(i)

    def setItem(self, r, c, s):
        """
        set tableItem text
        :param r: row
        :param c: column
        :param s: string
        :return: none
        """
        s = str(s)
        self.table.setItem(r, c, QTableWidgetItem(s))


class TileLayout(QGridLayout):
    def __init__(self, widget, gl):
        super().__init__()

        # self.figureList = Gyeolhap.currentfigure  #TODO To Receives the current round image

        t = Tile()

        figureList = list(gl.currentfigure.tileDict.values())

        r, c = 0, 0
        cnt = 0
        for figure in figureList:
            path = t.tileDict[figure][3]
            tilebutton = TileButton(path, widget.slot_toggle, cnt)
            self.addWidget(tilebutton, r, c)
            c += 1
            cnt += 1
            if c >= 3:
                r += 1
                c = 0


class PlayerLayout(QGridLayout):
    def __init__(self, widget):
        super().__init__()
        self._userLabel = QLabel(widget)
        self._userLabel.setFont(QFont("Arial", 15))  #TODO 글씨체 선정

        self._userScoreEdit = QTextEdit(widget)
        self._userScoreEdit.setFixedSize(70, 40)
        self.setUserScoreLabel("0")

        self.addWidget(self._userLabel, 0, 0)
        self.addWidget(self._userScoreEdit, 1, 0)

    def setUserLabel(self, username):
        """
        유저 이름을 받아서 이름Label을 변경
        :param username: 유저이름
        :return: none
        """
        self._userLabel.setText(username)

    def setUserScoreLabel(self, userscore):
        """
        유저 점수를 받아서 스코어에딧을 변경
        :param userscore: 유저 점수
        :return: none
        """
        self._userScoreEdit.setText(userscore)
        self._userScoreEdit.setReadOnly(True)
        self._userScoreEdit.setFont(QFont("Arial", 15))
        self._userScoreEdit.setAlignment(Qt.AlignCenter)


class AnswerLayout(QGridLayout):
    def __init__(self, widget):
        super().__init__()
        self.answerEdit = QLineEdit(widget)
        self.answerEdit.setReadOnly(True)
        self.answerSet = set()
        hapButton = Button("Hap", widget.buttonClicked)
        gyeolButton = Button("Gyeol", widget.buttonClicked)

        self.addWidget(self.answerEdit, 0, 0, 1, 2)
        self.addWidget(hapButton, 1, 0)
        self.addWidget(gyeolButton, 1, 1)

    def setAnwerEdit(self, set):
        """
        AnswerEdit에 선택한 Tile 집합 표시
        :param set: 선택한 Tile set
        :return: none
        """
        if set:
            self.answerEdit.setText(str(set))
            self.answerEdit.setReadOnly(True)
        else:
            self.answerEdit.setText("")
            self.answerEdit.setReadOnly(True)


    def addAnswerSet(self, i):
        """
        AnswerSet에 i를 추가하고 answerSet을 반환하는 함수
        :param i: integer
        :return: self.answerSet
        """
        self.answerSet.add(i)
        return self.answerSet

    def removeAnswerSet(self, i):
        """
        AnswerSet에 i를 제거하고 answerSet을 반환하는 함수
        :param i: integer
        :return: none
        """
        self.answerSet.remove(i)
        return self.answerSet


class TileButton(QPushButton):
    def __init__(self, path, callback, cnt):
        super().__init__()
        self.setCheckable(True)
        Qicon = QIcon(path)
        self.setIcon(Qicon)
        self.setIconSize(QSize(50, 50))
        self.setToolTip(str(cnt))
        self.clicked[bool].connect(callback)


class Button(QPushButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)  #TODO 적어 놓을지 아니면 제거할 지 판단
        self.setText(text)
        self.clicked.connect(callback)
