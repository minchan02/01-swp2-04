import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from ad_inGame import PWGame

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        start_button = QPushButton('Start')  # 시작버튼
        start_button.resize(100, 500)
        start_button.clicked.connect(self.start_button_clicked)
        self.show()
        
        title_label = QLabel('카이사르 암호 게임')  # 제목 라벨
        font = title_label.font()
        font.setBold(True)
        title_label.setFont(QtGui.QFont('Noto Sans KR',20))
        title_label.setAlignment(Qt.AlignHCenter)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(title_label)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(start_button)
        hbox2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(2)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle("카이사르 암호 게임")
        self.setGeometry(600,200,400,400)
        self.show()
        
    def start_button_clicked(self):
        self.close()
        self.start = PWGame()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())
