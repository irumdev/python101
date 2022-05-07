cnt = []

for i in range(1, 8):
    x = int(input(f"{i}일차 턱걸이 횟수 >>>"))
    cnt.append(x)

print(sum(cnt) / len(cnt))
