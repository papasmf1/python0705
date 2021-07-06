# DemoLoop.py 
value = 5 
while value > 0:
    print(value)
    value -= 1 

#갯수가 정해진 경우
for i in [1,2,3]:
    print(i)

d = ["문자열", 100, 3.14]
for item in d:
    print(item, type(item))

#구구단 출력
for x in [2,3,4,5,6]:
    print("---{0}단---".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x, y, x*y))

#break구문
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    # ctrl + / 
    if i > 5:
        break
    print("Item:{0}".format(i))

#contine구문은 나머지를 스킵하고 지속
print("---continue구문---")
for i in lst:
    # ctrl + / 
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

for i in lst:
    # ctrl + / 
    if i % 2 == 1:
        continue
    print("Item:{0}".format(i))

#수열함수
print( list(range(10)) )
print( list(range(1,11)) )
print( list(range(10,0,-1)) )

#수동으로 for구문을 돌리는 경우
for i in range(5):
    print(i)

#리스트 내장(리스트 컴프리헨션):약식 표현식
#파이썬스럽다.
lst = [1,2,3,4,5,6,7,8,9,10]
result = [i**2 for i in lst if i > 5]
print(result)

d = {100:"apple", 200:"kiwi", 300:"orange"}
print( [v.upper() for v in d.values()] )
