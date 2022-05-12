# 이룸님 수강기간이 7일 남았습니다.
name = '이룸'
duration = 7


# 문자열 포매팅이 없다면?
message = name + '님 수강기간이 ' + str(duration) + '일 남았습니다.'
print(message)

# 문자열 포매팅 사용시
message2 = f"{name}님 수강기간이 {duration}일 남았습니다."
print(message2)


# format 메서드 사용
# 인덱스로 대입
message3 = "Hello {0} {1} {2}".format('apple', 'pineapple', 'pen')
print(message3)
message3 = "Hello {2} {0} {1}".format('apple', 'pineapple', 'pen')
print(message3)
# 이름으로 대입
message3 = "Hellp {a} {c} {b}".format(a='apple', b='pineapple', c='pen')
print(message3)

# f-string 사용
name1 = 'apple'
name2 = 'pineapple'
name3 = 'pen'

message4 = f"Hello {name1} {name2} {name3}"
print(message4)
