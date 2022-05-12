# 실습문제 2.4.1
word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']

# 리스트 내포 사용 전
answer = []
for word in word_list:
    if word[0] == 'a':
        answer.append(word)
print(answer)

# 리스트 내포 사용 후
answer2 = [i for i in word_list if i[0] == 'a']
print(answer2)





# 실습문제 2.4.2
word_list = ['오메가3', None, '비타민C500', None, '홍삼절편']

# 리스트 내포 사용 전
answer3 = []
for word in word_list:
    if word is not None:
        answer3.append(word)
    else:
        answer3.append('')
print(answer3)

# 리스트 내포 사용 후 (내포를 남용하면 오히려 가독성이 떨어진다.)
answer4 = ['' if word is None else word for word in word_list]
print(answer4)
