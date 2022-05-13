# Unit 클래스
class Unit:
    """
    인스턴스 속성 : 이름, 체력, 방어막, 공격력
    -> 객체마다 각각 가지고 있는 속성
    """

    count = 0

    # 생성자(Constructor)
    # 객체를 생성할 때 호출되는 메서드
    def __init__(self, name, hp, guard, demage):
        self.name = name
        self.hp = hp
        self.guard = guard
        self.demage = demage
        Unit.count += 1
        print(f"{name}이(가) 생성 되었습니다.")

    # 객체를 문자열로 표현할 때 호출되는 메서드
    def __str__(self):
        return f"[{self.name}] 체력 : {self.hp}, 방어막 : {self.guard}, 공격력 : {self.demage}"

    # 1. 인스턴스 메서드
    # 인스턴스 속성에 접근할 수 있는 메서드
    def hit(self, demage):
        if self.guard >= demage:
            self.guard -= demage
        elif (self.guard + self.hp) >= demage:
            self.hp -= demage - self.guard
            self.guard = 0
        else:
            self.guard = 0
            self.hp = 0

    # 2. 클래스 메서드
    # 클래스 속성에 접근하는 메서드
    @classmethod
    def print_count(cls):
        print(f"생성된 유닛 갯수 : [{cls.count}]")

# 객체를 생성
probe = Unit('프로브', 20, 20, 5)
zealot = Unit('질럿', 100, 60, 16)
dragoon = Unit('드라군', 100, 80, 20)


# 인스턴스 메서드 호출
probe.hit(16)
print(probe)  # [프로브] 체력 : 20, 방어막 : 4, 공격력 : 5
probe.hit(16)
print(probe)  # [프로브] 체력 : 8, 방어막 : 0, 공격력 : 5
probe.hit(16)
print(probe)  # [프로브] 체력 : 0, 방어막 : 0, 공격력 : 5

# 클래스 메서드 호출
Unit.print_count()
