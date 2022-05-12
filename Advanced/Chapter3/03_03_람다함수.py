# 기존 함수
def minus_one(a):
    return a-1

# 람다 함수 - 이름이 필요 없는 함수
lambda a : a-1


# 람다 함수 호출 방법
# 1. 함수 자체를 호출
print((lambda a : a-1)(10))

# 2. 변수에 람다함수를 담아서 호출
minus_one_2 = lambda a : a-1
print(minus_one_2(100))


# 람다 함수에서 if문 사용
# 기존 함수
def is_positive_number(a):
    if a > 0:
        return True
    else:
        return False

# 람다 함수
lambda a : True if a > 0 else False

# 1. 함수 자체를 호출
print((lambda a : True if a > 0 else False)(5))

# 2. 변수에 람다함수를 담아서 호출
is_positive_number_2 = (lambda a : True if a > 0 else False)
print(is_positive_number_2(-1))
