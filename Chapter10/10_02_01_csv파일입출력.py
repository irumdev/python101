import pickle

# 1. 파이썬 객체를 pickle로 저장하기
data = {
    "목표1" : "파이썬 기초, 심화 강의 모두 듣기",
    "목표2" : "자기소개 준비하기"
}
file = open("./Chapter10/data.pk", "wb")
pickle.dump(data, file)
file.close()


# 2. pickle 파일 파이썬으로 가져오기
file = open("./Chapter10/data.pk", "rb")
data = pickle.load(file)
print(data)
file.close()
