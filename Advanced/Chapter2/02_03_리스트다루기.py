# 리스트 원소 삭제
fruits = ['apple', 'orange', 'carrot']
del fruits[1]  # 1
fruits.remove('carrot')  # 2
fruits.pop(0)  # 3
print(fruits)

# 리스트 정렬
nums = [6,1,3,5,1,2,6,7]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# enumerate
days = ['일', '월', '화', '수', '목', '금', '토']
for index, day in enumerate(days, 1):  # index 1 부터 시작
    print(index, day)
