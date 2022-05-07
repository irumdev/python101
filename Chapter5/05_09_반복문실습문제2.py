# 실습문제 Learning Korean
words = ["김치", "불고기", "비빔밥", "삼계탕"]

correct = 0
print("Let's learning Korean")
for word in words:
    print(word)
    x = input(">>>")
    if x != word:
        break
    else:
        correct += 1

print("전체 문제 개수 : ", len(words))
print("맞힌 문제 개수 : ", correct)
print("틀린 문제 개수 : ", len(words) - correct)

