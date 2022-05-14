# 데코레이터
# 함수의 앞, 뒤로 부가적인 기능을 넣어주고 싶을 때 사용
# 로깅, 권한 등에 자주 사용


# 데코레이터 생성하기
def logger(func):
    def wrapper(arg):
        print("함수시작")
        func(arg)
        print("함수 끝")
    return wrapper


# 데코레이터 적용
@logger
def print_hello(name):
    print(f"Hello {name}")

@logger
def print_bye(name):
    print(f"Bye {name}")

print_hello('irumdev')
print_bye('gildong')
