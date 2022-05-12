# 리스트 할당 방식
# Call by Reference
x = [1, 2, 3, 4, 5]
y = x
y[2] = 0

print(x, y)
print(id(x), id(y))


# 리스트 복사
x = [1, 2, 3, 4, 5]
y = x.copy()
y[2] = 0

print(x, y)
print(id(x), id(y))


# 다차원 리스트 깊은 복사
import copy
x = [[1, 2], [3, 4, 5]]
y = copy.deepcopy(x)
y[1][0] = 999

print(x, y)
print(id(x), id(y))
