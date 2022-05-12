# 1. 위치 매개변수
# 가장 기본적인 매개변수
def my_func(a, b):
    print(a, b)

my_func("asd", "fgh")



# 2. 기본 매개변수
# 매개변수의 기본값을 지정 할 수 있다.
def post_info(title, content='내용없음'):
    print(f"제목 : {title}")
    print(f"내용 : {content}")

post_info("안녕하세요!")



# 3. 키워드 매개변수
# 함수 호출시에 키워드를 붙여서 호출
# 매개변수의 순서를 지키지 않아도 됩니다.
def post_info(title, content):
    print(f"제목 : {title}")
    print(f"내용 : {content}")

post_info(content="없어용!", title="내용이 있었는데")
