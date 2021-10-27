from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("test1.ui", self)
        self.voiceb.clicked.connect(self.GoLunchWindow)

    def GoLunchWindow(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

class LunchWindow(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("test2.ui", self)
        self.backb.clicked.connect(self.backbuttonfunction)
        self.lunchb.clicked.connect(self.lunchloadfunction)

    def lunchloadfunction(self):
        req = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=남주고등학교 10월 26일 급식')

        html = req.text

        soup = BeautifulSoup(html, 'html.parser')

        Nj_MealData = soup.find_all('li', attrs={'class':'menu_info'})
        Nj_MealData = re.sub('<[^>]+>', '', str(Nj_MealData), 0)
        Nj_MealData = re.sub('[a-z]+', '', str(Nj_MealData), 0)
        Nj_MealData = Nj_MealData.replace('  ', '')

        nj_Lunch = Nj_MealData.split('10월 26일 [점심]')[1].split(',')[0]
        nj_Dinner = Nj_MealData.split('10월 26일 [저녁]')[1].split(',')[0]

        print('점심:' + nj_Lunch + '\n저녁: ' + nj_Dinner)
        self.luncht.append('점심:' + nj_Lunch + '\n저녁: ' + nj_Dinner)
    def backbuttonfunction(self):
        widget.setCurrentIndex(widget.currentIndex()-1)


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #화면 전환용 Widget 설정
    widget = QtWidgets.QStackedWidget()

    #레이아웃 인스턴스 생성
    mainWindow = MainWindow()
    lunchwindow = LunchWindow()

    #Widget 추가
    widget.addWidget(mainWindow)
    widget.addWidget(lunchwindow)

    #프로그램 화면을 보여주는 코드
    widget.setFixedHeight(480)
    widget.setFixedWidth(640)
    widget.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()