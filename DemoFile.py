# DemoFile.py 

#쓰기 작업
f = open("c:\\work\\demo.txt", "wt")
f.write("첫줄\n두번째줄\n세번째\n")
f.close()
print( f.closed )

#읽기
f = open("c:/work/demo.txt", "rt")
#전체를 하나의 문자열 변수로 읽기(파일 크기가 작다)
result = f.read() 
print(result)
#한번에 한줄씩 읽기 
print( f.tell() )
f.seek(0)
#파일 크기가 100MB(로그파일) 
print( f.readline(), end="" )
print( f.readline(), end="" )

#파일 내용을 리스트로 출력 
print("---리스트로 리턴---")
f.seek(0)
lst = f.readlines()
print( lst )
for item in lst:
    #문자열을 치환
    print( item.replace("\n", "") )


f.close()
