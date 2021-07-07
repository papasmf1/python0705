#다중 상속에서 이름 충돌 
class Tiger:
    def jump(self):
        print("호랑이 점프")
    def cryOne(self):
        print("호랑이 어흥~~")

class Lion:
    def bite(self):
        print("사자 물어뜯기")
    def cryTwo(self):
        print("사자 으르릉~~")

#한번에 여러개의 부모 클래스를 상속받기 
class Liger(Lion, Tiger):
    def play(self):
        print("라이거와 놀기")

l = Liger()
l.cryOne()
l.cryTwo() 
print("클래스 상속 순서(MRO):", Liger.__mro__)


        
