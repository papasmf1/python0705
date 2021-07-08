# db1.py 
import sqlite3

#연결객체를 생성(임시로 메모리만 저장)
con = sqlite3.connect(":memory:")
#구문을 실행할 커서 객체를 생성
cur = con.cursor()
#테이블 구조를 만들기
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('derick', '010');")
#입력파라메터 처리
name = "gildong"
phoneNumber = "222"
cur.execute("insert into PhoneBook values (?, ?);", 
    (name, phoneNumber) )
#다중 데이터 입력 
datalist = (("tom","222"), ("dsp","123"))
cur.executemany("insert into PhoneBook values (?, ?);", 
    datalist )

#검색하기
cur.execute("select * from PhoneBook;")
#패치 메서드로 읽기 
print("---fetchone()---")
print( cur.fetchone() )
print("---fetchmany(2)---")
print( cur.fetchmany(2) )
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print( cur.fetchall() )

