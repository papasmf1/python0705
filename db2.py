# db2.py 
import sqlite3

#연결객체를 생성(영구적으로 파일에 저장)
con = sqlite3.connect("c:\\work\\sample.db")
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
print( cur.fetchall() )

#정상적으로 완료(Log에 기록 ---> DB에 복사)
con.commit() 