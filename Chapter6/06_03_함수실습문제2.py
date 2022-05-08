# 실습문제 6.1.3
# 로또 번호 생성기
import random

def get_random_number():
    number = random.randint(1, 45)
    return number


numbers = []
while len(numbers) < 6:
    x = get_random_number()
    if x not in numbers:
        numbers.append(x)

print(numbers) 
