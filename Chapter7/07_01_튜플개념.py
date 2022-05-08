# 튜플
# 시퀀스 자료형
# 수정, 추가, 삭제가 불가능한 리스트 = 읽기 전용 리스트
# 메모리 사용이 효율적
# 읽기만 가능하기 때문에 데이터 손실 염려가 없다.
x = (1, 2, 3)
y = "자료형이 달라도 된다", 2, False
z = tuple([5,])
print(x, y, z)
print(type(x), type(y), type(z))

numbers = 3, 4, 5  # 패킹
x, y, z = numbers  # 언패킹
print(numbers)
print(x, y, z)


a = 10, 20, 30, 40, 30
print(a.index(20))  # 특정값의 인덱스 구하기
print(a.count(30))  # 특정값의 갯수
print(max(a), min(a))  # 최대값, 최소값
print(sum(a))  # 합계
