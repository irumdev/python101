import csv

# 1. csv 파일 쓰기
data = [
    ["이름", "반", "번호"],
    ["재석", 2, 20],
    ["이유", 3, 21],
    ["병훈", 3, 22],
    ["동규", 3, 23]
]

file = open("./Chapter10/student.csv", "w")
writer = csv.writer(file)
for d in data:
    writer.writerow(d)
file.close()


# 2. csv 파일 읽기
file = open("./Chapter10/student.csv", "r")
reader = csv.reader(file)
for data in reader:
    print(data)

file.close()
