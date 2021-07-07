# class2.py 
#클래스(새로운 형식을 정의): 내부에 변수 + 함수 
class Person:
    #클래스 멤버변수(데이터 공유가 목적)
    num_person = 0 
    #초기화를 담당하는 특별한 메서드 
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1 
    #인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성(복사본)
p1 = Person()
p2 = Person()
p3 = Person()
print("인스턴스 갯수:{0}".format(Person.num_person))
p1.name = "전우치"
p2.name = "이순신"
p1.print()
p2.print()

#런타임(실행시간)에 변수 추가
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

#인스턴스에 추가
p1.age = 30 
print(p1.age)
#print(Person.age)
