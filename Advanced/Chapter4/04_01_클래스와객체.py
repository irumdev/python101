# Unit 클래스
class Unit:
    """
    속성 : 이름, 체력, 방어막, 공격력
    """

    # 생성자(Constructor)
    # 객체를 생성할 때 호출되는 메서드
    def __init__(self, name, hp, guard, demage):
        self.name = name
        self.hp = hp
        self.guard = guard
        self.demage = demage
        print(f"{name}이(가) 생성 되었습니다.")

    # 객체를 문자열로 표현할 때 호출되는 메서드
    def __str__(self):
        return f"[{self.name}] 체력 : {self.hp}, 방어막 : {self.guard}, 공격력 : {self.demage}"


# 객체를 생성
probe = Unit('프로브', 20, 20, 5)
zealot = Unit('질럿', 100, 60, 16)
dragoon = Unit('드라군', 100, 80, 20)

print(probe, zealot, dragoon, sep='\n')
