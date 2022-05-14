# 2. 제너레이터 표현식
# 리스트 내포와 유사하다. []를 사용하느냐 ()를 사용하느냐의 차이
double_generator = (i * 2 for i in range(1, 10))
print(double_generator)

for i in double_generator:
    print(i)


# 3. 메모리 사용을 효율적으로 사용하기 위해서 사용
# ex) 숫자 1 - 10000 3배로 만든 결과 리스트 vs 제너레이터 차이
import sys

# 리스트 : 데이터 저장에 필요한 메모리를 모두 사용함
# 제너레이터 : 나중에 필요할 때 값을 만들어서 사용 (expression만 가지고 있음)
list_data = [i * 3 for i in range(1, 10000 + 1)]
generator_data = (i * 3 for i in range(1, 10000 + 1))

print(sys.getsizeof(list_data))  # 87616
print(sys.getsizeof(generator_data))  # 112
