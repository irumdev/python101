# 원화와 환율을 입력하면 달러로 변환

won = input("원화 금액을 입력하세요. >>>")
dollar = input("환율을 입력하세요. >>>")

try:  # 예외를 발생 할 수도 있는 코드
    print(int(won) / int(dollar))
except ValueError as e:  # 예외가 발생했을 때 실행되는 코드
    print("예외가 발생했습니다!", e)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.", e)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally:
    print("항상 실행되는 코드")

# 예외처리를 하면 에러가 발생해도 실행을 중단하지 않고 계속 실행한다.
print("프로그램 종료")
