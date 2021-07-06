# DemoDict.py 
colors = {"apple":"red", "banana":"yellow"}
print( colors )
print( len(colors) )
#검색
print( colors["apple"] )
#입력
colors["cherry"] = "red"
print( colors )
#삭제 
del colors["apple"]

for item in colors.items():
    print(item)

for k,v in colors.items():
    print(k, v)

print("----장비---")
device = {"아이폰":5, "아이패드":10}
print( device["아이폰"] )
#입력
device["맥프레"] = 15 
#수정
device["아이폰"] = 6 
#삭제
del device["아이패드"]
print( device )

#전화번호 저장
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print( phone.keys() )
print( phone.values() )
print( "park" in phone )
print( "moon" not in phone )

#디버깅할 때 중단점(Break Point)
for item in phone.items():
    print(item)


#phone의참조만 복사해서 p변수 대입 
p = phone
p["kang"] = "1234"
print(phone)
print(p)
#아이덴티티를 출력
print( id(phone) )
print( id(p) )




