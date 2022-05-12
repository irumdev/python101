# 1. replace
# 문자열 치환
a = "오늘 날씨는 흐림입니다."
a = a.replace('흐림', '맑음')
print(a)

# 2. find
# 문자열 시작위치 찾기
b = "Hello World"
idx = b.find('World')
print(idx)

# 3. split
# 문자열 구분자로 분리
str = '신발,265,X2221,99000'
c = str.split(',')
print(c)

# 4. 문자열 공백 제거
d = "          Hello!         "
print(d.lstrip())  # 왼쪽 공백제거
print(d.rstrip())  # 오른쪽 공백제거
print(d.strip())  # 양쪽 공백제거
