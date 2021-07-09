# form2.py 
# form2.ui(화면만 저장) + form2.py(로직을 저장)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#미리 디자인한 파일을 로딩
form_class = uic.loadUiType("form2.ui")[0]

#폼 클래스를 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
    #슬롯 메서드를 정의(시그널 처리)
    def firstClick(self):
        self.label.setText("첫번째~~")
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


