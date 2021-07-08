# form.py 
# form.ui(화면만 저장) + form.py(로직을 저장)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#미리 디자인한 파일을 로딩
form_class = uic.loadUiType("form.ui")[0]

#폼 클래스를 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
        self.label.setText("첫번째 Qt데모")

#진입점을 체크 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show() 
    app.exec_() 


