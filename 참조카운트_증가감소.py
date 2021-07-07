import sys 

class MyClass:
    #초기화 메서드(생성자)
    def __init__(self, value):
        self.Value = value 
        print("Instance is created! Value = ", value)
    #소멸자 메서드 
    def __del__(self):
        print("Instance is deleted!")
        
#인스턴스 생성
c = MyClass(10)
#참고 카운트를 출력
#print("참조 카운트:", sys.getrefcount(c) )
#del c 

print("전체 코드 실행 종료")
