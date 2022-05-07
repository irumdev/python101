# 구구단 출력하기

step = int(input("몇 단을 출력할까요? >>>"))

for i in range(1,10):
    print(step, "*", i, "=", step * i)


# 게임 메뉴 만들기
while True:
    menu = int(input("메뉴를 선택해주세요. >>>"))
    if menu == 1:
        print("게임을 시작합니다!")
    elif menu == 2:
        print("실시간 랭킹")
    elif menu == 3:
        print("게임을 종료합니다.")
        break
    else:
        print("다시 입력해주세요.")
