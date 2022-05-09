# 클래스를 사용하면 재사용성이 증가하고
# 객체지향적 사고는 프로그램의 설계를 이해하기 쉽게 도와준다.

# 클래스를 사용하지 않았을 때
champ1_name = "이즈리얼"
champ1_health = 300
champ1_attack = 60

champ2_name = "리신"
champ2_health = 400
champ2_attack = 70

champ3_name = "티모"
champ3_health = 230
champ3_attack = 55

print(f"{champ1_name}님 소환사의 협곡에 오신것을 환영합니다.")
print(f"{champ2_name}님 소환사의 협곡에 오신것을 환영합니다.")
print(f"{champ3_name}님 소환사의 협곡에 오신것을 환영합니다.")

def basic_attack(name, attack):
    print(f"{name} 기본공격 {attack}")

basic_attack(champ1_name, champ1_attack)
basic_attack(champ2_name, champ2_attack)
basic_attack(champ3_name, champ3_attack)

# 클래스를 사용 했을 때
class Champion:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name}님 소환사의 협곡에 오신것을 환영합니다.")
    def basic_attack(self):
        print(f"{self.name} 기본공격 {self.attack}")


champ1 = Champion("이즈리얼", 300, 60)
champ2 = Champion("리신", 400, 70)
champ3 = Champion("티모", 230, 55)

champ1.basic_attack()
champ2.basic_attack()
champ3.basic_attack()


# 파이썬에서는 자료형도 클래스다
a = 10
b = "문자열"
c = True

print(type(a))
print(type(b))
print(type(c))

print(b.__dir__())  # 문자열 객체의 메서드를 출력
