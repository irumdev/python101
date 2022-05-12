# raise 구문을 사용해서 에러를 강제로 발생시켜 봅시다.

try:
    num = int(input("음수를 입력해주세요. >>>"))
    if num >= 0:
        raise ValueError("양수는 입력할 수 없습니다.")
except ValueError as e:
    print("밸류 에러 발생!", e)
except Exception as e:
    print("에러 발생!", e)



# 에러 만들기

class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수는 입력할 수 없습니다잉~")

try:
    num = int(input("음수를 입력해주세요. >>>"))
    if num >= 0:
        raise PositiveNumberError
except PositiveNumberError as e:
    print("에러 발생!", e)
