# while
# 보통 반복 횟수가 정해지지 않았을 때 사용한다.

i = 5  # 초기화
while i < 9:  # 조건식
    print(i, "번째 다짐, 나는 할 수 있다!")  # 반복할 명령
    i += 2  # 증감식


# 무한루프
# 조건식에 True를 넣어서 항상 반복되게 함
while True:
    x = input("종료하려면 \"exit\"를 입력하세요. >>>")
    if x == "exit":
        break