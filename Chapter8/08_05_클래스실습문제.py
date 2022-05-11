# 실습문제 8.1.1

class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    def sale(self):
        print(f"{self.name}을 {self.price}원에 판매했습니다.")
    def discard(self):
        if self.isdropable:
            print(f"{self.name}을 버렸습니다.")
        else:
            print(f"{self.name}은 버릴 수 없습니다.")

class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def wear(self):
        print(f"{self.name}를 착용해서 {self.effect} 효과를 얻었습니다!")

class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def use(self):
        print(f"{self.name}를 사용해서 {self.effect} 효과를 얻었습니다!")

# 인스턴스 생성
sword = WearableItem("소드테일의 꼬리", 30000, 100, True, "허기짐 500 증가")
sword.wear()  # WearableItem 클래스 wear 메소드 호출
sword.sale()  # 상속받은 Item 클래스 sale 메소드 호출
sword.discard()  # 상속받은 Item 클래스 discard 메소드 호출

potion = UsableItem("비타민 주스", 500, 10, False, "2년 수명연장")
potion.use()
potion.discard()  # 상속받은 메소드
potion.sale()  # 상속받은 메소드
