import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from function import LockString
from word import Word

class PWGame(QWidget):
    def __init__(self):
        super(PWGame, self).__init__()
        self.lock = LockString()
        self.word = Word('Words.txt')
        self.inGame()


    def inGame(self):
        hbox = QHBoxLayout()

        # word setting
        GuessWord = self.word.randWord()
        # label setting

        life = QFrame()
        life.setFrameShape(QFrame.StyledPanel)

        layout1 = QVBoxLayout()
        life_label = QLabel('♥ ♥ ♥')
        life_label.setFont(QtGui.QFont('Noto Sans KR', 20))
        life_label.setAlignment(Qt.AlignCenter)
        layout1.addWidget(life_label)
        life.setLayout(layout1)

        score_label = QLabel('Score:')
        score = QFrame()
        score.setFrameShape(QFrame.StyledPanel)

        layout2 = QVBoxLayout()
        score_value = QLabel('0')
        score_value.setFont(QtGui.QFont('Noto Sans KR', 20))
        score_value.setAlignment(Qt.AlignCenter)
        layout2.addWidget(score_value)
        score.setLayout(layout2)

        # time
        layout3 = QVBoxLayout()
        time_label = QLabel('Time:')
        time_value = QLabel('0:15') # 나중에 시간 설정
        time_value.setFont(QtGui.QFont('Noto Sans KR', 20))
        time_value.setAlignment(Qt.AlignCenter)
        time = QFrame()
        time.setFrameShape(QFrame.StyledPanel)
        layout3.addWidget(time_value)
        time.setLayout(layout3)

        # n
        layout4 = QHBoxLayout()
        n_value = QLabel('4', self) # n 값은 나중에 random으로 조절
        n_value.setFont(QtGui.QFont('Noto Sans KR', 20))
        n_value.setAlignment(Qt.AlignCenter) # 가운데 정렬
        n = QFrame()
        n.setFrameShape(QFrame.StyledPanel)
        layout4.addWidget(n_value)
        n.setLayout(layout4)


        # 암호화된 문자열
        layout5 = QHBoxLayout()
        str = QFrame()
        
        # 카이사르 암호화로 나온 암호
        self.pwd = QLabel(self.lock.encryption(GuessWord, 3)) # 3은 나중에 n으로 바꿈
        self.pwd.setFont(QtGui.QFont('Noto Sans KR', 20))
        self.pwd.setAlignment(Qt.AlignCenter) # 가운데 정렬
        str.setFrameShape(QFrame.StyledPanel)
        layout5.addWidget(self.pwd)
        str.setLayout(layout5)

        # 답
        answer_label = QLabel('답:')
        answer = QLineEdit()
        
        # 상태창
        self.message = QLineEdit()
        self.message.setReadOnly(True)

        # spliter 설정

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
        splitter3.addWidget(self.message)
        splitter3.addWidget(splitter2)

        hbox.addWidget(splitter3)
        self.setLayout(hbox)

        self.setWindowTitle("Caesar Cipher Game")
        self.setGeometry(600, 200, 400, 400)
        self.show()
        
    # 정답 확인 버튼이 눌리면 실행할 함수
    def answerButtonClicked(self):
        GuessWord = self.word.randWord()
        self.pwd.setText(self.lock.encryption(GuessWord, 3))  # 3은 이후에 n으로 대체
        if self.lock.encryption(GuessWord, 3) == self.answer.text():
            # 사용자의 복호화 성공 여부에 따라 상태창 업데이트
            self.message.setText("Successfully decrypted!")
        else:
            self.message.setText("Failed to unlock.")

    def gameOver(self): #혹시 몰라서 게임 오버됐을 때 창 뜨게 만들어본 함수
        result = QMessageBox.information(self, 'Game Over', 'Game Over\nRetry?', QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            self.inGame()
        else:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PWGame()
    sys.exit(app.exec_())

