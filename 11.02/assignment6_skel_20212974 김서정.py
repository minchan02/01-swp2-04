import pickle #모든 기능이 동작하지 않습니다. 확인 부탁드립니다.
import sys
import copy
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        # label setting
        self.name = QLabel('Name:', self)
        self.age = QLabel('Age:', self)
        self.score = QLabel('Score:', self)
        self.amount = QLabel('Amount:', self)
        self.key = QLabel('Key:', self)
        self.result = QLabel("Result:", self)

        # 값 입력창
        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()

        # 명령
        self.addButton = QPushButton('Add')
        self.delButton = QPushButton('Del')
        self.findButton = QPushButton('Find')
        self.incButton = QPushButton('Inc')
        self.showButton = QPushButton('show')

        self.addButton.clicked.connect(self.buttonClicked)
        self.delButton.clicked.connect(self.buttonClicked)
        self.findButton.clicked.connect(self.buttonClicked)
        self.incButton.clicked.connect(self.buttonClicked)
        self.showButton.clicked.connect(self.buttonClicked)

        # 정렬 키
        self.keyset = QComboBox()
        self.keyset.addItem("Name")
        self.keyset.addItem("Age")
        self.keyset.addItem("Score")

        # 결과 창
        self.textresult = QTextEdit()

        # 첫번째 행 설정
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.name)
        hbox1.addWidget(self.nameEdit)
        hbox1.addWidget(self.age)
        hbox1.addWidget(self.ageEdit)
        hbox1.addWidget(self.score)
        hbox1.addWidget(self.scoreEdit)

        # 두번째 행 설정
        hbox2 = QHBoxLayout()
        hbox2.stretch(1)
        hbox2.addWidget(self.amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(self.key)
        hbox2.addWidget(self.keyset)

        # 세번째 행 설정
        hbox3 = QHBoxLayout()
        hbox3.stretch(1)
        hbox3.addWidget(self.addButton)
        hbox3.addWidget(self.delButton)
        hbox3.addWidget(self.findButton)
        hbox3.addWidget(self.incButton)
        hbox3.addWidget(self.showButton)

        # 네번째 행 설정
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.result)

        # 다섯번째 행 설정
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.textresult)

        # 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        self.setLayout(vbox)

        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        keyw = self.keyset.currentText()
        a = sorted(self.scoredb, key=lambda x: x[keyw])
        r = ''
        for i in a:
            for j in i.items():
                r += j[0] + '=' + str(j[1]) + '\t'
            r += '\n'
        self.textresult.setText(r)

    def buttonClicked(self):
        sender = self.sender()
        button = sender.text()
        r = ''

        if button == 'Add':
            record = {'Name': self.nameEdit.text(), 'Age': self.ageEdit.text(), 'Score': self.scoreEdit.text()}
            self.scoredb.append(record)
            self.showScoreDB()

        if button == 'Del':
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    self.scoredb.remove(p)
            self.showScoreDB()

        if button == 'Find':
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    for attr in p:
                        r += attr + "=" + p[attr] + '\t'
                    r += '\n'
            self.textresult.setText(r)

        if button == 'Inc':
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    p['Score'] = str(int(p['Score']) + int(self.amountEdit.text()))
            self.showScoreDB()

        if button == 'show': #show할 경우 출력되는 record의 format이 동일하지 않습니다. 확인 부탁드립니다.
            self.showScoreDB()


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

