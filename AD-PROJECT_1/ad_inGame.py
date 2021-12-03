import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

class PWGame(QWidget):
    def __init__(self):
        super(PWGame, self).__init__()
        self.inGame()

    def inGame(self):
        hbox = QHBoxLayout()

        life = QFrame()
        life.setFrameShape(QFrame.StyledPanel)

        layout1 = QVBoxLayout()
        life_label = QLabel('♥ ♥ ♥') #life를 라벨로 해도 되는지 모르겠네요 .. 
        life_label.setFont(QtGui.QFont('Noto Sans KR', 20))
        layout1.addWidget(life_label)
        life.setLayout(layout1)

        score_label = QLabel('Score:')
        score = QFrame()
        score.setFrameShape(QFrame.StyledPanel)

        layout2 = QVBoxLayout()
        score_value = QLabel('0')
        score_value.setFont(QtGui.QFont('Noto Sans KR', 20))
        layout2.addWidget(score_value)
        score.setLayout(layout2)

        time_label = QLabel('Time:')
        time = QFrame()
        time.setFrameShape(QFrame.StyledPanel)

        n = QFrame()
        n.setFrameShape(QFrame.StyledPanel)

        str = QFrame()
        str.setFrameShape(QFrame.StyledPanel)

        answer_label = QLabel('답:')
        answer = QLineEdit()

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(life)
        splitter1.addWidget(score_label)
        splitter1.addWidget(score)
        splitter1.addWidget(time_label)
        splitter1.addWidget(time)

        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(answer_label)
        splitter2.addWidget(answer)

        splitter3 = QSplitter(Qt.Vertical)
        splitter3.addWidget(splitter1)
        splitter3.addWidget(n)
        splitter3.addWidget(str)
        splitter3.addWidget(splitter2)

        hbox.addWidget(splitter3)
        self.setLayout(hbox)

        self.setWindowTitle("Caesar Cipher Game")
        self.setGeometry(600, 200, 400, 400)
        self.show()

    def gameOver(self): #혹시 몰라서 게임 오버됐을 때 창 뜨게 만들어본 함수
        result = QMessageBox.information(self, 'Game Over', 'Game Over\nRetry?', QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            self.inGame
        else:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PWGame()
    sys.exit(app.exec_())
