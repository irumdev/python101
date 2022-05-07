# 1. 대입 연산
# 변수이름 = 값


# 2. 산술 연산
x = 5
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)  # 몫
print(x % y)  # 나머지
print(x ** y)  # x의 y제곱

# 3. 문자열 연산
tag1 = "#핫플"
tag2 = "#맛집"
tag3 = "#파스타"
tag = tag1 + tag2 + tag3
print(tag)

message = "우린 모두 파이썬을 사랑합니다.\n" * 3
print(message)

# 4. 복합 할당 연산자
level = 10
level = level + 1
level += 1  # 레벨 1 증가

health = 2000
health -= 500  # 체력 500 감소

attack = 300
attack *= 1.5  # 공격력 50% 증가

speed = 420
speed /= 2  # 이동속도 50% 감소

print(level, health, attack, speed)
