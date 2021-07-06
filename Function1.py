# Function1.py 
#함수를 정의
def times(a,b):
    return a*b 

#호출 
result = times(5,6)
print(result)

#값을 리턴하지 않는 함수
def setValue(newValue):
    x = newValue

#호출
retValue = setValue(5)
print(retValue)

#다중의 값을 리턴 
def swap(x,y):
    return y,x 

#호출
print( swap(3,4) )

#불변형식(정수, 실수, 불린, 튜플, 문자열)
a = 1.2 
print( id(a) )
a = 2.3 
print( id(a) )

print("---가변형식---")
#가변형식
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )

#스코핑룰(이름을 해석하는 규칙):LGB 
x = 5 
def func1(a):
    return a+x 

#호출
print( func1(1) )

def func2(a):
    x = 1 
    return a+x

#호출
print( func2(1) )

#Pass By Reference(참조가 복사된다)
def change(x):
    #복사본을 수정(깊은복사)
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:", x1)

#초기화
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:", wordlist)

#디버깅을 연습(논리적인 오류 찾기)
def intersect(prelist, postlist):
    #리스트로 교집합 문자를 저장할 지역변수
    retList = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList

#호출(교집합 문자를 리턴)
print( intersect("HAM", "SPAM") )

