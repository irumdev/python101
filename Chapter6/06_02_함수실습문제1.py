# 실습문제 6.1.1
def multiply(a, b):
    """
    DocString
    함수에 대한 설명
    두 수의 곱샘 결과를 반환하는 함수
    """
    return a * b

print(multiply(2, 6))


# 실습문제 6.1.2
def print_sum_avg(x, y, z):
    print(f"합계 : {sum([x, y, z])}")
    print(f"평균 : {sum([x, y, z])/3}")

print_sum_avg(10, 20, 30)
