# 일급객체 (First Class Object)
# 데이터처럼 사용이 가능하다.
# 매개변수에 넘겨줄 수 있다.
# 리턴값이 될 수 있다.


# 1. 데이터 처럼 사용이 가능하다.

# 1) 변수에 할당
def func(x, y):
    return x + y

add = func
print(add(1, 2))


# 2) 컬렉션에 할당
def multiply(x, y):
    return x * y

def division(x, y):
    return x / y

calculator = [multiply, division]
print(calculator[0](3, 4))
print(calculator[1](4, 2))

# 2. 매개변수에 넘겨 줄 수 있다.
def input_data():
    data = input("데이터 입력 >>>")
    return data

def start(func):
    print("입력한 데이터는", func())

start(input_data)


# 3. 리턴값이 될 수 있다.
def plus10(a):
    return a + 10

def func():
    return plus10

tmp = func()
print(tmp(5))
