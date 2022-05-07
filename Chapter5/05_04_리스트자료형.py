# 1. 리스트 만들기
# 데이터가 있는 리스트
animals = ["파스타", "피자", "치킨", "마카롱", "아아"]

# 데이터가 없는 리스트
empty = []



# 2. 데이터 조작하기
# 데이터 접근하기
# 인덱스는 0 부터 시작
print(animals[3])
print(animals[-1])  # 마지막 원소

# 데이터 추가하기
animals.append("멘보샤")
print(animals)

# 데이터 할당하기
animals[1] = "리조또"
print(animals)

# 데이터 삭제하기
del animals[0]
print(animals)

# 리스트 슬라이스
print(animals[1:3])
print(animals[:])
print(animals[:3])
print(animals[1:])
print(animals[1:-1])

# 리스트 길이
print(len(animals))
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)
