import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
from test1_question4_window import Test1_Question4_Window

# mysql ##################################
cnx = mysql.connector.connect(
    user = "root",
    password = "1001tnqls",
    host = "127.0.0.1",
    port = 3306,
    database = "test_zip"
)

cursor = cnx.cursor()

class Test1_Question3_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('당신은 프론트엔드인가? 백엔드인가?')
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

        self.label = QLabel("         은(는) 프론트엔드인가? 백엔드인가?", self)
        self.label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.label.resize(800, 60)
        self.label.move(40, 100)

        #질문
        self.q1 = QLabel("1 더하기 1은?", self)
        self.q1.setFont(QtGui.QFont("맑은 고딕", 26))
        self.q1.resize(800, 60)
        self.q1.move(30, 140)

        #답 버튼
        self.a1 = QPushButton("2", self)
        self.a1.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a1.resize(800, 100)
        self.a1.move(30, 210)
        self.a1.clicked.connect(self.a_click)

        self.a2 = QPushButton("귀요미", self)
        self.a2.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a2.resize(800, 100)
        self.a2.move(30, 320)
        self.a2.clicked.connect(self.b_click)

        self.test1_question4_window = Test1_Question4_Window(self)
    def a_click(self):
        self.test1_question4_window.show()
        user_name = self.name_label.text()
        self.test1_question4_window.name_label.setText(user_name)

        print(user_name, ">>>점수 추가 완료")
        if self.label.text() == "Are you the frontend? Is it the backend?":
            self.test1_question4_window.label.setText("Are you the frontend? Is it the backend?")
            self.test1_question4_window.q1.setText("People often tell me that I have an aesthetic sense.")
        elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
            self.test1_question4_window.label.setText("あなたはフロントエンドであるかバックエンドのか？")
            self.test1_question4_window.q1.setText("私は芸術のセンスがあるとよく言われます。")
        self.hide()

    def b_click(self):
        self.test1_question4_window.show()
        user_name = self.name_label.text()
        self.test1_question4_window.name_label.setText(user_name)

        sql = "UPDATE programmer_Test SET calculate = calculate + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print(user_name, ">>>점수 추가 완료")
        if self.label.text() == "Are you the frontend? Is it the backend?":
            self.test1_question4_window.label.setText("Are you the frontend? Is it the backend?")
            self.test1_question4_window.q1.setText("People often tell me that I have an aesthetic sense.")
        elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
            self.test1_question4_window.label.setText("あなたはフロントエンドであるかバックエンドのか？")
            self.test1_question4_window.q1.setText("私は芸術のセンスがあるとよく言われます。")
        self.hide()
