import sys
import urllib.request
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
import home_window

# mysql ##################################
cnx = mysql.connector.connect(
    user = "root",
    password = "1001tnqls",
    host = "127.0.0.1",
    port = 3306,
    database = "test_zip"
)

cursor = cnx.cursor()

class Result2_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('나와 어울리는 영화는?')
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resize(1100, 800)

        # 테스트 이름
        self.name_label = QLabel("봉봉", self)
        self.name_label.resize(0, 0)
        self.name_label.move(0, 0)

        # 로고
        logo = QPushButton("", self)
        logo.resize(100, 50)
        logo.move(30, 30)
        logo.toggle()
        logo.setToolTip("Home")
        logo.setStyleSheet('image:url(./image/logo.png); border:0px;')
        logo.clicked.connect(self.btn_Start)

        # 테스트 결과
        self.result_name = QLabel("", self)
        self.result_name.setFont(QtGui.QFont("맑은 고딕", 26))
        self.result_name.resize(800, 60)
        self.result_name.move(60, 100)


        # 테스트 결과 이미지
        self.result_img = QLabel("", self)
        self.result_img.resize(400, 500)
        self.result_img.move(70, 180)
        #self.result_img.setStyleSheet('image:url(./image/FullStack.png); border:0px;')

        # 테스트 결과 내용
        self.result_text = QLabel("", self)
        self.result_text.setFont(QtGui.QFont("맑은 고딕", 13))
        self.result_text.setStyleSheet("color: black;"
                                 "border-style: solid;"
                                 "border-width: 1px;"
                                 "border-color: #000000;"
                                 "border-radius: 1px;"
                                 "line-height: 160%;")
        self.result_text.resize(530, 500)
        self.result_text.move(500, 180)

        #url 경로
        self.url_label = QLabel("", self)
        self.url_label.resize(0, 0)
        self.url_label.move(0, 0)

        #저장하기 버튼 ( 결과 공유 대체 )
        save = QPushButton("result save", self)
        save.resize(150, 50)
        save.move(900, 100)
        save.toggle()
        save.clicked.connect(self.save_result)

        self.deleteData()

    def btn_Start(self):
        self.start = home_window.Home_Window(self)
        self.start.show()
        self.hide()

    def save_result(self):
        url = self.url_label.text()
        urllib.request.urlretrieve(url,'./image_result/' + self.name_label.text() + '_result.png')
        print(self.name_label.text() + "_result.png" + " : 저장")

    def deleteData(self):
        sql = "TRUNCATE TABLE my_movie_Test;"
        cursor.execute(sql)

        cnx.commit()