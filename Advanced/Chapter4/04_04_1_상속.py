class Item:
    """
    속성 : 이름
    메서드 : 줍기, 버리기
    """

    def __init__(self, name):
        self.name = name

    def pick(self):
        print(f"[{self.name}]을 주웠습니다.")

    def discard(self):
        print(f"[{self.name}]을 버렸습니다.")


class Weapon(Item):
    """
    속성 : 공격력
    메서드 : 공격하기
    """
    def __init__(self, name, demage):
        super().__init__(name)
        self.demage = demage

    def attack(self):
        print(f"[{self.name}]을(를) 사용하여 {self.demage}의 피해를 입혔습니다.")

class HealingItem(Item):
    """
    속성 : 회복량
    메서드 : 사용하기
    """
    def __init__(self, name, heal):
        super().__init__(name)
        self.heal = heal
    
    def use(self):
        print(f"[{self.name}]을(를) 사용하여 {self.heal}의 체력을 회복했습니다.")


m16 = Weapon('m16', 110)
bandage = HealingItem('붕대', 20)

m16.attack()
bandage.use()
