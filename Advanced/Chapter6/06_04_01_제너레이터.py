# 제너레이터

# 1. 이터레이터를 만드는 함수
def season_generator(*args):
    for arg in args:
        yield arg

g = season_generator('spring', 'summer', 'fall', 'winter')

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())


def func():
    print("첫번째 작업 중...")
    yield 1

    print("두번째 작업 중...")
    yield 2

    print("세번째 작업 중...")
    yield 3

    print("네번째 작업 중...")
    yield 4

ge = func()
print(ge.__next__())
print(ge.__next__())
print(ge.__next__())
print(ge.__next__())
print(ge.__next__())
