# web2.py 
#웹서버와 통신할 때 사용
import urllib.request
#크롤링에 사용
from bs4 import BeautifulSoup
#웹페이지를 실행해서 문자열로 리턴 

#파일에 저장(읽기+쓰기, 첨부)
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
for i in range(1,6):
    strURL = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    print(strURL)    
    data = urllib.request.urlopen(strURL)
    #검색이 용이한 객체 
    soup = BeautifulSoup(data, "html.parser")

    cartoons = soup.find_all("td", class_="title")

    for item in cartoons:
        title = item.find("a").text 
        print( title.strip() )
        f.write(title.strip() + "\n")

f.close() 

