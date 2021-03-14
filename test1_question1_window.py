import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
from test1_question2_window import Test1_Question2_Window

# mysql ##################################
cnx = mysql.connector.connect(
    user = "root",
    password = "1001tnqls",
    host = "127.0.0.1",
    port = 3306,
    database = "test_zip"
)

cursor = cnx.cursor()

class Test1_Question1_Window(QtWidgets.QMainWindow, QPushButton):
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
        self.q1 = QLabel("조별 과제에서 당신의 역할은?", self)
        self.q1.setFont(QtGui.QFont("맑은 고딕", 26))
        self.q1.resize(800, 60)
        self.q1.move(40, 140)

        #답 버튼
        self.a1 = QPushButton("자료조사 및 정리", self)
        self.a1.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a1.resize(800, 100)
        self.a1.move(40, 210)
        self.a1.clicked.connect(self.a_click)

        self.a2 = QPushButton("정리된 자료로 ppt 만들기", self)
        self.a2.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a2.resize(800, 100)
        self.a2.move(40, 320)
        self.a2.clicked.connect(self.b_click)

        self.test1_question2_window = Test1_Question2_Window(self)

    def a_click(self):
        self.test1_question2_window.show()
        user_name = self.name_label.text()
        self.test1_question2_window.name_label.setText(user_name)

        print(user_name, ">>>점수 추가 완료")
        #print(self.name_label.text() + " : a 선택")
        if self.label.text() == "Are you the frontend? Is it the backend?":
            self.test1_question2_window.label.setText("Are you the frontend? Is it the backend?")
            self.test1_question2_window.q1.setText("What if you could make one of the two?")
            self.test1_question2_window.a1.setText("Dressing up Steve Jobs")
            self.test1_question2_window.a2.setText("Talking with Siri")
        elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
            self.test1_question2_window.label.setText("あなたはフロントエンドであるかバックエンドのか？")
            self.test1_question2_window.q1.setText("2つのうちの1つを作れたらどうする？")
            self.test1_question2_window.a1.setText("Steve Jobs のドレスアップ")
            self.test1_question2_window.a2.setText("Siri との会話")
        self.hide()

    def b_click(self):
        self.test1_question2_window.show()
        user_name = self.name_label.text()
        self.test1_question2_window.name_label.setText(user_name)

        sql = "UPDATE programmer_Test SET calculate = 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print(user_name, ">>>점수 추가 완료")
        #print(self.name_label.text() + " : b 선택")
        if self.label.text() == "Are you the frontend? Is it the backend?":
            self.test1_question2_window.label.setText("Are you the frontend? Is it the backend?")
            self.test1_question2_window.q1.setText("What if you could make one of the two?")
            self.test1_question2_window.a1.setText("Dressing up Steve Jobs")
            self.test1_question2_window.a2.setText("Talking with Siri")
        elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
            self.test1_question2_window.label.setText("あなたはフロントエンドであるかバックエンドのか？")
            self.test1_question2_window.q1.setText("2つのうちの1つを作れたらどうする？")
            self.test1_question2_window.a1.setText("Steve Jobs のドレスアップ")
            self.test1_question2_window.a2.setText("Siri との会話")
        self.hide()


