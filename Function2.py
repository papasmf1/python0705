# Function2.py 
#기본값이 있는 경우
def times(a=10, b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드 인자(파라메터명을 기술)
def connectURI(server, port):
    str = "http://" + server + ":" + port 
    return str 

#호출
print( connectURI("kpc.net", "80") )
print( connectURI(port="8080", server="kpc.net") )

#가변인자(입력되는 파라메터의 숫자가 가변적이다.)
def union(*ar):
    #지역변수로 리스트형식을 초기화
    result = []
    #HAM(0) | EGG(1)
    for item in ar:
        # H(0) | A(1) | M(2)
        for x in item:
            #result에 include되어 있지 않으면
            if x not in result:
                result.append(x)
    return result

#호출
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )


#정의되지 않은 인자 처리(딕셔너리로 처리)
def userURIBuilder(server, port, **user):
    str = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str 

#호출
print( userURIBuilder("kpc.net", "80", id="kim", passwd="1234"))
print( userURIBuilder("kpc.net", "80", id="kim", 
    passwd="1234", name="mike"))

#람다 표현식(간단하게 함수를 정의)
g = lambda x,y:x*y 
print( g(3,4) )
print( g(5,6) )
print( (lambda x:x*x)(3) )
print( globals() )

#도움말 추가
def times(a,b):
    """이 함수는 2개의 숫자를 
       입력받아서 곱해서 리턴합니다.
    """
    return a*b 

#호출
print( help(times) )

#순회가능한 형식(시퀀스형식): 리스트, 튜플, 문자열
for item in [1,2,3]:
    print(item)

for char in "abc":
    print(char)

#저수준으로 처리
s = "abc"
it = iter(s)
print( next(it) )    
print( next(it) )    

