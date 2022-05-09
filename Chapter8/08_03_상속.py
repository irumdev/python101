# 상속
# 클래스들의 중복된 코드를 제거 및 통합하여 유지보수를 편리하게 함

# 부모 클래스
class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
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
    def move(self):
        print("날기")


wolf = Wolf("울프", 1500, 200)
wolf.move()

shark = Shark("상어", 3000, 400)
shark.move()

dragon = Dragon("용용이", 8000, 800)
dragon.move()
