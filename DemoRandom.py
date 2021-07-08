# DemoRandom.py 
import random

print( random.random() )
print( random.random() )
#구간을 지정
print( random.uniform(2.0, 5.0) )
print( random.uniform(2.0, 5.0) )
#임의의 정수를 생성
print( [random.randrange(20) for i in range(10)] )
print( [random.randrange(20) for i in range(10)] )
print( [random.randrange(20) for i in range(10)] )
#유일한 숫자를 샘플링
print( random.sample(range(20), 10) )
print( random.sample(range(20), 10) )

print("---로또번호생성---")
lotto = list(range(1,46))
random.shuffle(lotto)
print( lotto )
print("---번호 5개 추출---")
for item in range(5):
    print( lotto.pop() )

#파일 다루기 
from os.path import * 
print( abspath("python.exe") )
print( basename("c:\\work\\demo.txt") )
print( getsize("c:\\python38\\python.exe") )

#경로를 이동해서 c:\work폴더에 파일리스트 받기 
from os import * 
import glob 

print("운영체제이름:", name)
print("현재작업폴더:", getcwd() )
chdir("..")
print("현재작업폴더:", getcwd() )
chdir("c:\\work")
print("현재작업폴더:", getcwd() )
result = glob.glob("*.py")
print( result )
for item in glob.iglob("*.*"):
    print(item)
