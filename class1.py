# class1.py 
#클래스(새로운 형식을 정의): 내부에 변수 + 함수 
class Person:
    #초기화를 담당하는 특별한 메서드 
    def __init__(self):
        self.name = "default name"
    #인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성(복사본)
p1 = Person()
p1.print()
