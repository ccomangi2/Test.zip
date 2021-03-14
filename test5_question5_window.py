import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
from test5_question6_window import Test5_Question6_Window

# mysql ##################################
cnx = mysql.connector.connect(
    user = "root",
    password = "1001tnqls",
    host = "127.0.0.1",
    port = 3306,
    database = "test_zip"
)

cursor = cnx.cursor()

class Test5_Question5_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('연애세포 생존 테스트')
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.resize(880, 500)

        back = QLabel("", self)
        back.resize(880, 500)
        back.move(0, 0)
        back.setStyleSheet('image:url(./image/background.png); border:0px;')

        # 로고
        logo = QLabel("", self)
        logo.resize(100, 50)
        logo.move(30, 30)
        logo.setStyleSheet('image:url(./image/logo.png); border:0px;')

        # 테스트 이름
        self.name_label = QLabel("이수빈", self)
        self.name_label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.name_label.resize(80, 60)
        self.name_label.move(40, 100)

        self.label = QLabel("         의 연애세포는 살아있는가?", self)
        self.label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.label.resize(800, 60)
        self.label.move(40, 100)

        #질문
        self.q1 = QLabel("새로운 사람을 만나는 것은 스트레스다. ", self)
        self.q1.setFont(QtGui.QFont("맑은 고딕", 22))
        self.q1.resize(800, 60)
        self.q1.move(30, 140)

        #답 버튼
        self.a1 = QPushButton("O", self)
        self.a1.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a1.resize(800, 100)
        self.a1.move(40, 210)
        self.a1.clicked.connect(self.a_click)

        self.a2 = QPushButton("X", self)
        self.a2.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a2.resize(800, 100)
        self.a2.move(40, 320)
        self.a2.clicked.connect(self.b_click)

        self.test5_question6_window = Test5_Question6_Window(self)
    def a_click(self):
        self.test5_question6_window.show()
        user_name = self.name_label.text()
        self.test5_question6_window.name_label.setText(user_name)

        print(user_name, ">>>점수 추가 완료")
        if self.label.text() == "         's Love Cell Survival Test":
            self.test5_question6_window.label.setText("         's Love Cell Survival Test")
            self.test5_question6_window.q1.setText("When you see a couple passing by, you get annoyed rather than envious.")
        elif self.label.text() == "         恋愛細胞生存テスト":
            self.test5_question6_window.label.setText("         恋愛細胞生存テスト")
            self.test5_question6_window.q1.setText("カップルが通り過ぎるのを見ると, うらやましいというよりむしろいらいらするものだ。")
        self.hide()

    def b_click(self):
        self.test5_question6_window.show()
        user_name = self.name_label.text()
        self.test5_question6_window.name_label.setText(user_name)

        sql = "UPDATE lovesurvival_test SET calculate = calculate + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print(user_name, ">>>점수 추가 완료")
        if self.label.text() == "         's Love Cell Survival Test":
            self.test5_question6_window.label.setText("         's Love Cell Survival Test")
            self.test5_question6_window.q1.setText("When you see a couple passing by, you get annoyed rather than envious.")
        elif self.label.text() == "         恋愛細胞生存テスト":
            self.test5_question6_window.label.setText("         恋愛細胞生存テスト")
            self.test5_question6_window.q1.setText("カップルが通り過ぎるのを見ると, うらやましいというよりむしろいらいらするものだ。")
        self.hide()


