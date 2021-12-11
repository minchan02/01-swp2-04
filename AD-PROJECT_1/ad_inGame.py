import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from function import LockString
from word import Word
import random
from guess import Guess


class PWGame(QWidget):
    def __init__(self):
        super(PWGame, self).__init__()
        # 클래스 설정
        self.lock = LockString()
        self.word = Word('Words.txt')
        self.guess = Guess(self.word.randWord())

        # 변수 설정
        self.Finished = False
        self.life = 3
        self.score = 0

        # 타이머 생성
        self.timer = QTimer(self)
        self.sec = 20

        self.inGame()

    def inGame(self):
        hbox = QHBoxLayout()

        # word setting


        # label setting
        life = QFrame()
        life.setFrameShape(QFrame.StyledPanel)

        layout1 = QVBoxLayout()
        self.life_label = QLabel('♥ ♥ ♥')
        self.life_label.setFont(QtGui.QFont('Noto Sans KR', 20))
        self.life_label.setAlignment(Qt.AlignCenter)
        layout1.addWidget(self.life_label)
        life.setLayout(layout1)

        score_label = QLabel('Score:')
        score = QFrame()
        score.setFrameShape(QFrame.StyledPanel)

        layout2 = QVBoxLayout()
        self.score_value = QLabel()
        self.score_value.setNum(self.score)
        self.score_value.setFont(QtGui.QFont('Noto Sans KR', 20))
        self.score_value.setAlignment(Qt.AlignCenter)
        layout2.addWidget(self.score_value)
        score.setLayout(layout2)

        # time
        layout3 = QVBoxLayout()
        self.timer.start(1000)  # 타이머 시작
        self.timer.timeout.connect(self.setTimer)
        self.time_label = QLabel('Time:')
        self.time_value = QLabel()
        self.time_value.setNum(15)
        self.time_value.setFont(QtGui.QFont('Noto Sans KR', 20))
        self.time_value.setAlignment(Qt.AlignCenter)
        time = QFrame()
        time.setFrameShape(QFrame.StyledPanel)
        layout3.addWidget(self.time_value)
        time.setLayout(layout3)

        # 랜덤 n 생성
        self.random_n = random.randrange(1, 6)

        # n
        layout4 = QHBoxLayout()
        self.n_value = QLabel(str(self.random_n), self)
        self.n_value.setFont(QtGui.QFont('Noto Sans KR', 20))
        self.n_value.setAlignment(Qt.AlignCenter)  # 가운데 정렬
        n = QFrame()
        n.setFrameShape(QFrame.StyledPanel)
        layout4.addWidget(self.n_value)
        n.setLayout(layout4)

        # 암호화된 문자열
        layout5 = QHBoxLayout()
        e_str = QFrame()

        # 카이사르 암호화로 나온 암호
        self.pwd = QLabel(self.lock.encryption(self.guess.getWord(), self.random_n))
        self.pwd.setFont(QtGui.QFont('Noto Sans KR', 20))
        self.pwd.setAlignment(Qt.AlignCenter)  # 가운데 정렬
        e_str.setFrameShape(QFrame.StyledPanel)
        layout5.addWidget(self.pwd)
        e_str.setLayout(layout5)

        # 상태창
        self.message = QLineEdit()
        self.message.setReadOnly(True)

        # 답
        answer_label = QLabel('답:')
        self.answer = QLineEdit()
        self.answer.returnPressed.connect(self.PressEnter)

        # spliter 설정

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(life)
        splitter1.addWidget(score_label)
        splitter1.addWidget(score)
        splitter1.addWidget(self.time_label)
        splitter1.addWidget(time)

        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(answer_label)
        splitter2.addWidget(self.answer)

        splitter3 = QSplitter(Qt.Vertical)
        splitter3.addWidget(splitter1)
        splitter3.addWidget(n)
        splitter3.addWidget(e_str)
        splitter3.addWidget(self.message)
        splitter3.addWidget(splitter2)

        hbox.addWidget(splitter3)
        self.setLayout(hbox)

        self.setWindowTitle("Caesar Cipher Game")
        self.setGeometry(600, 200, 400, 400)
        self.show()

    # 정답 확인 버튼이 눌리면 실행할 함수
    def PressEnter(self):
        if self.guess.isAnswer(self.answer.text()):
            # 사용자의 복호화 성공 여부에 따라 상태창 업데이트
            self.message.setText("Successfully decrypted!")
            self.score += self.guess.getLength()
            self.startGame()
            return

        else:
            self.message.setText("Failed to unlock.")
            self.life -= 1

        self.answer.clear()

        # 목숨확인
        if self.life <= 0:
            self.Finished = True

        self.life_label.setText('♥ '* self.life) # 목숨만큼 업데이트

        if self.Finished:
            self.gameOver()

    def setTimer(self):
        if self.sec == 0:  # or 정답 버튼이 눌리면:
            self.sec = 20
            self.life -= 1

            if self.life <= 0:
                self.gameOver()

            else:
                self.startGame()

        self.time_value.setNum(self.sec)
        self.sec -= 1

    def gameOver(self):  # 혹시 몰라서 게임 오버됐을 때 창 뜨게 만들어본 함수

        result = QMessageBox.information(self, 'Game Over', 'Game Over\nRetry?', QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            self.startGame()
        else:
            self.close()


    def startGame(self):
        self.Finished = False
        self.guess = Guess(self.word.randWord())
        self.score_value.setNum(self.score)
        self.sec = 20
        
        if self.life <= 0:
            self.life = 3
    
        self.life_label.setText('♥ ' * self.life)
        self.random_n = random.randrange(1, 6)
        self.n_value.setText(str(self.random_n))
        self.pwd.setText(self.lock.encryption(self.guess.getWord(), self.random_n))
        self.message.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PWGame()
    sys.exit(app.exec_())

