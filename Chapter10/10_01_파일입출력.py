# 1. 파일 쓰기 (덮어쓰기)
contents = open("./Chapter10/data.txt", "w", encoding="utf8")
contents.write("안녕하세요. 반갑습니다. 사랑해요.")
contents.close()

# 2. 파일 쓰기 (이어쓰기)
contents2 = open("./Chapter10/data2.txt", "a", encoding="utf8")
contents2.write("\n안녕하세요. 반갑습니다. 사랑해요.")
contents2.close()

# 3. 파일 읽기
file = open("./Chapter10/data2.txt", "r", encoding="utf8")

# 3.1 파일 전체 읽기
contents = file.read()
print(contents)

# 3.2 파일 한줄씩 읽기
while True:
    line = file.readline()
    print(line, end="")
    if line == "":
        break


file.close()
