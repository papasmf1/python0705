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

