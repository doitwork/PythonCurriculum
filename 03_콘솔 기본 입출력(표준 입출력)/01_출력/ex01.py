"""

콘솔 기본 입출력
- 기본 입력 장치 : 키보드
- 기본 출력 장치 : 모니터



출력함수
- print(*object, sep='', end='', file=sys.stdout, flush=False)



"""
#숫자 출력
print(100)

#문자열 출력
print("문자열")

#연산 결과 출력
print(100 + 200)

#연산 결과 출력
print(100 > 0)

#다수의 인자값 출력
print("Hong" + "Gil" + "Dong") #문자열 합치기
print("Hong" "Gil" "Dong") #문자열 합치기
print("Hong", "Gil", "Dong") #문자열 띄어쓰기

#개행 문자 대신 원하는 문자로 출력하기
print("Hong", end="@")
print("Gil", end="@")
print("Dong", end="@")
print()

for i in range(5):
    print(i, end=' ')
print()

#구분자로 원하는 문자를 출력하기
print("Hong", "Gil", sep=" ")






