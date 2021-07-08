# DemoStr.py 
u = "<<<  spam and ham  >>>"
print( u )
result = u.strip("<> ")
print( result )
#치환 
result = result.replace("spam", "spam egg")
print( result )
#공백문자를 기준으로 리스트로 변환해서 리턴 
lst = result.split() 
print( lst )
#다시 하나의 문자열 변수로 합치기 
print( " ".join(lst) )

#정규 표현식
import re 
#검색을 했을 때 리턴형식이 매칭 오브젝트 
print( re.search("[0-9]*th", "35th") )
print( re.match("[0-9]*th", "35th") )
result = re.search("[0-9]*th", "35th")
print( result.group() )

#함정을 추가
print("---함정---")
print( re.search("[0-9]*th", "  35th") )
print( re.match("[0-9]*th", "  35th") )
print( re.search("apple", "this is apple") )
print( re.match("apple", "this is apple") )

#우편번호 패턴 
print("---우편번호---")
result = re.search("\d{5}", "우리동네는 52300")
print( result.group() )
result = re.search("\d{4}", "올해는 2021년")
print( result.group() )
