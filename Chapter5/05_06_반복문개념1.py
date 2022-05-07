# 반복문
# 반복해서 명령을 실행하고 싶을 때

# 시퀀스 자료형
# 순서가 있는 자료형
# 1. 리스트
# 2. 문자열
# 3. range 객체
# 4. 튜플
# 5. 딕셔너리

# for 문
champions = ["티모", "이즈리얼", "리신"]

for champion in champions:
    print("선택한 챔피언 :", champion)

# 문자열
message = "소환사의 협곡에 오신 여러분을 환영합니다."

for word in message:
    print(word, end='')

# range 객체
# range(10) -> 0 ~ 9 까지 숫자를 포함하는 range 객체가 생성된다.
# range(시작, 끝 + 1, 단계)
for i in range(1, 10, 2):
    print(i)