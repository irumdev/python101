class Math:
    # 3. 정적 메서드
    # 인스턴스를 만들 필요가 없는 메서드
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    # 4. 매직 메서드 (던더 메서드) __ -> 던더
    # __init__, __str__ 등


print(Math.add(3, 4))
print(Math.sub(3, 4))
