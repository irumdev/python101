str = input("시간을 입력해주세요. >>>")


if '시간' in str and '분' in str:
    str = str.split()
    hour = int(str[0].replace('시간', ''))
    minute = int(str[1].replace('분', ''))
    print(hour * 60 + minute)
elif '시간' in str:
    hour = int(str.replace('시간', ''))
    print(hour * 60)
elif '분' in str:
    minute = int(str.replace('분', ''))
    print(minute)
