# 조건문
# 조건에 따라 명령의 실행여부를 결정

origin_pw = "1234"
input_pw = input("비밀번호를 입력하세요. >>>")

if input_pw == origin_pw:
    print("로그인 성공")
elif input_pw == "":
    print("비밀번호를 입력하지 않았습니다.")
else:
    print("로그인 실패")
