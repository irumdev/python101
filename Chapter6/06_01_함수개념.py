# 함수를 쓰지 않았을 때
print("안녕하세요. 길동님")
print("프리미엄 서비스 사용기간이 1일 남았습니다.")

print("안녕하세요. 병훈님")
print("프리미엄 서비스 사용기간이 30일 남았습니다.")

print("안녕하세요. 동규님")
print("프리미엄 서비스 사용기간이 15일 남았습니다.")


# 함수를 사용했을 때
def printMessage(name, remain):
    print(f"안녕하세요. {name}님")
    print(f"프리미엄 서비스 사용기간이 {remain}일 남았습니다.")

printMessage("길동", 1)
printMessage("병훈", 30)
printMessage("동규", 15)
