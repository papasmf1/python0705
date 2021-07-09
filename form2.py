# form2.py 
# form2.ui(화면만 저장) + form2.py(로직을 저장)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#웹서버와 통신할 때 사용
import urllib.request
#크롤링에 사용
from bs4 import BeautifulSoup
#웹페이지를 실행해서 문자열로 리턴 


#미리 디자인한 파일을 로딩
form_class = uic.loadUiType("form2.ui")[0]

#폼 클래스를 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
    #슬롯 메서드를 정의(시그널 처리)
    def firstClick(self):
        #파일에 저장(읽기+쓰기, 첨부)
        f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
        for i in range(1,6):
            strURL = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
            print(strURL)    
            data = urllib.request.urlopen(strURL)
            #검색이 용이한 객체 
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")
            for item in cartoons:
                title = item.find("a").text 
                print( title.strip() )
                f.write(title.strip() + "\n")
        f.close() 
        self.label.setText("네이버 웹툰 리스트 저장~~")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭~~")

#진입점을 체크 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show() 
    app.exec_() 


