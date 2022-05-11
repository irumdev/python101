import pay_module

# 변수 사용
print(pay_module.version)

# 함수 사용
pay_module.printAuthor()

# 클래스 사용
payment = pay_module.Pay("9591-5691-3392-1922", 5000, "2022-05-11")
print(payment.get_pay_info())


print(pay_module.__name__)
