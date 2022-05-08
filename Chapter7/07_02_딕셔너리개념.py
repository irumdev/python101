# 시퀀스 자료형
# KeyValue 사전형 자료형

# 딕셔너리 만들기
stock_a = {"삼성전자": 85000, "LG전자": 150000}

stock_b = {
    "삼성전자": [81000, 81500, 79000, 77500, 77000],
    "LG전자": (150000, 149000, 145000, 151000, 152000)
}

stock_c = {
    "삼성전자": {
        "현재가": 66000,
        "보유수량": 5,
        "매수단가": 81000
    }
}



# 접근
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

# 할당
stock_a["삼성전자"] = 84000
print(stock_a["삼성전자"]) 

# 삭제
del stock_a["LG전자"]
print(stock_a)


# 딕셔너리 함수
stock_d = {
    "삼성전자": 85000,
    "SK하이닉스": 123000,
    "NAVER": 367000,
    "카카오": 88000
}

# items() : 키와 데이터의 쌍
print(stock_d)
print(stock_d.items())
for item in stock_d.items():
    print(item)

# keys() : 키
for key in stock_d.keys():
    print(key)

# values() : 데이터
for value in stock_d.values():
    print(value)
    