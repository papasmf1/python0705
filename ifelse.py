# ifelse.py
#input()은 입력을 받는 함수
#int()는 정수형식으로 변환
score = int(input("Input score:"))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
else:
    grade = "D"

print("Grade is ", grade)

