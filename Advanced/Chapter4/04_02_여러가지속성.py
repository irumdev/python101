# Unit 클래스
class Unit:
    """
    인스턴스 속성 : 이름, 체력, 방어막, 공격력
    -> 객체마다 각각 가지고 있는 속성

    클래스 속성 : 전체 유닛 갯수
    -> 모든 클래스가 공유하는 하나의 속성

    비공개 속성
    -> 클래스 안에서만 사용 가능한 속성
    """

    count = 0

    # 생성자(Constructor)
    # 객체를 생성할 때 호출되는 메서드
    def __init__(self, name, hp, guard, demage):
        self.name = name
        self.__hp = hp
        self.guard = guard
        self.demage = demage
        Unit.count += 1
        print(f"{name}이(가) 생성 되었습니다.")

    # 객체를 문자열로 표현할 때 호출되는 메서드
    def __str__(self):
        return f"[{self.name}] 체력 : {self.__hp}, 방어막 : {self.guard}, 공격력 : {self.demage}"


# 객체를 생성
probe = Unit('프로브', 20, 20, 5)
print(f"전체 유닛 갯수 : {Unit.count}")
zealot = Unit('질럿', 100, 60, 16)
print(f"전체 유닛 갯수 : {Unit.count}")
dragoon = Unit('드라군', 100, 80, 20)
print(f"전체 유닛 갯수 : {Unit.count}")

print(probe, zealot, dragoon, sep='\n')


# 비공개 속성 접근 시도
# 속성이름이 name mangling 되어서 __hp라는 이름으로 찾을 수 없다.
print(probe.__hp)
probe.__hp = 100
print(probe)

# 비공개 속성에 강제로 접근
# 접근 자체를 막는 것이 아니고 속성의 이름을 바꿔서 쉽게 접근하지 못하도록 하는 것임
print(probe._Unit__hp)
probe._Unit__hp = 100
print(probe)
