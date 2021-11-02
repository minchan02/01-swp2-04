import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()

        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.initUI()
        self.showScoreDB()

    def initUI(self):
        name = QLabel('Name: ')
        age = QLabel('Age: ')
        score = QLabel('Score: ')
        amount = QLabel('Amount: ')
        key = QLabel('Key: ')
        resulting = QLabel('Result: ')

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()

        self.keyCombo = QComboBox()
        self.keyCombo.addItem('Name')
        self.keyCombo.addItem('Age')
        self.keyCombo.addItem('Score')

        AddButton = QPushButton("Add")
        DelButton = QPushButton("Del")
        FindButton = QPushButton("Find")
        IncButton = QPushButton("Inc")
        ShowButton = QPushButton("Show")

        AddButton.clicked.connect(self.buttonClicked)
        DelButton.clicked.connect(self.buttonClicked)
        FindButton.clicked.connect(self.buttonClicked)
        IncButton.clicked.connect(self.buttonClicked)
        ShowButton.clicked.connect(self.buttonClicked)



        Uhbox = QHBoxLayout() # 맨 위 레이아웃
        Uhbox.addWidget(name)
        Uhbox.addWidget(self.nameEdit)
        Uhbox.addWidget(age)
        Uhbox.addWidget(self.ageEdit)
        Uhbox.addWidget(score)
        Uhbox.addWidget(self.scoreEdit)
        Uhbox.addWidget(amount)
        Uhbox.addWidget(self.amountEdit)
        Uhbox.addWidget(key)
        Uhbox.addWidget(self.keyCombo)



        D1hbox = QHBoxLayout() # 아래 레이아웃 1 => 버튼
        D1hbox.addWidget(AddButton)
        D1hbox.addWidget(DelButton)
        D1hbox.addWidget(FindButton)
        D1hbox.addWidget(IncButton)
        D1hbox.addWidget(ShowButton)


        self.result = QTextEdit()


        D2hbox = QHBoxLayout()
        D2hbox.addWidget(resulting)

        D3hbox = QHBoxLayout()
        D3hbox.addWidget(self.result)



        vbox = QVBoxLayout()
        vbox.addLayout(Uhbox)
        vbox.addLayout(D1hbox)
        vbox.addLayout(D2hbox)
        vbox.addLayout(D3hbox)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
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
            self.scoredb =  pickle.load(fH)
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
        cp_scoredb = []

        keyname = self.keyCombo.currentText()

        cp_scoredb = sorted(self.scoredb, key = lambda x:x[keyname])

        for info in cp_scoredb:
            self.result.append('Age=' + str(info['Age'] )+ "    " + 'Name=' + str(info['Name']) + "    " + 'Score=' + str(info['Score']) + "    ")

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == 'Add':
            dict = {}

            name = self.nameEdit.text()
            age = self.ageEdit.text()
            score = self.scoreEdit.text()

            dict['Name'] = name
            dict['Age'] = age
            dict['Score'] = score
            self.scoredb.append(dict)

            self.result.clear()
            self.showScoreDB()

        if sender.text() == 'Del':
            num = 0
            for i in self.scoredb:
                if i['Name'] == self.nameEdit.text():
                    del self.scoredb[num]
                    num -= 1
                num += 1

            self.result.clear()
            self.showScoreDB()

        if sender.text() == 'Find':
            self.result.clear()

            for i in self.scoredb:
                if i['Name'] == self.nameEdit.text():
                    self.result.append('Age=' + str(i['Age'] )+ "    " + 'Name=' + str(i['Name']) + "    " + 'Score=' + str(i['Score']) + "    ")

            self.showScoreDB()

        if sender.text() == 'Inc':
            for i in self.scoredb:
                if i['Name'] == self.nameEdit.text():
                    i['Score'] += int(self.amountEdit.text())

            self.result.clear()
            self.showScoreDB()

        if sender.text() == 'Show':
            if self.keyCombo.currentText() == 'Name':
                self.scoredb.sort(key = lambda x:x['Name'])

            elif self.keyCombo.currentText() == 'Age':
                self.scoredb.sort(key = lambda x:x['Age'])

            elif self.keyCombo.currentText() == 'Score':
                self.scoredb.sort(key = lambda x:x['Score'])

            self.result.clear()
            self.showScoreDB()

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
