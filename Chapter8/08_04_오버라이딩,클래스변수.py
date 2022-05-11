import random

# 상속
# 클래스들의 중복된 코드를 제거 및 통합하여 유지보수를 편리하게 함

# 클래스 변수
# 인스턴스들이 모두 공유하는 변수

# 부모 클래스
class Monster:
    max_num = 1000  # 클래스 변수
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1  # 클래스 변수는 self 키워드를 쓰지 않고 클래스명으로 접근한다.
    def move(self):
        print("지상에서 이동하기")

# 자식클래스
class Wolf(Monster):
    # 속성과 메서드를 상속받는다
    pass

class Shark(Monster):
    # 메소드 오버라이딩
    def move(self):
        print("헤엄치기")

class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)  # 부모클래스의 생성자 호출
        self.skills = ("불뿜기", "몸통박치기", "도망가기")
    def move(self):
        print("날기")
    def skill(self):
        print(f"[{self.name}] 스킬 사용 - {self.skills[random.randint(0,2)]}")


wolf = Wolf("울프", 1500, 200)
wolf.move()
print(wolf.max_num)

shark = Shark("상어", 3000, 400)
shark.move()
print(shark.max_num)

dragon = Dragon("용용이", 8000, 800)
dragon.move()
dragon.skill()
dragon.skill()
dragon.skill()
print(Monster.max_num)
