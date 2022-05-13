# 1. map 함수
# 기존 리스트에서 각 원소마다 특정 로직을 실행한 결과를 다시 리스트로 만들 때
# map(함수, 컬렉션)
print(list(map(int, ['3', '4', '5', '6'])))

# 1) for 사용
items = ['  로지텍마우스 ', ' 키보드  ']
for index, item in enumerate(items):
    items[index] = item.strip()
print(items)

# 2) map 사용
def strip_all(a):
    return a.strip()
items = ['  로지텍마우스 ', ' 키보드  ']
items = list(map(strip_all, items))
print(items)

# 3) map, lambda 사용
items = ['  로지텍마우스 ', ' 키보드  ']
items = list(map(lambda x:x.strip(), items))
print(items)






# 2. filter 함수
# 기존 리스트에서 조건을 만족하는 원소만 남기고 싶을 때
# filter(함수, 컬렉션)
def func(x):
    return x < 0
print(list(filter(func, [-3, 1, 0, -7, 5])))

# 예제
# 리스트에서 길이가 3이하인 문자들만 필터링
animals = ['cat', 'dog', 'bird', 'pig', 'cow', 'tiger', 'lion']
animals = list(filter(lambda x:len(x)<=3, animals))
print(animals)
