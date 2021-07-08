# web1.py 
from bs4 import BeautifulSoup

#파일을 문자열 변수에 로딩
page = open("c:\\work\\test01.html", "rt", 
    encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )
#<p>태그 몽땅 검색 ===> 리스트 형식
#print( soup.find_all("p") )
#첫번째 <p>태그만 검색
#print( soup.find("p") )
#조건이 있는 경우: <p class='outer-text'>
#print( soup.find_all("p", class_="outer-text") )

#내부의 문자열만 가져오기 
for tag in soup.find_all("p"):
    print( tag.text.replace("\n", "").strip() )

    
    