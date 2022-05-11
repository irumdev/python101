version = 2.0

def printAuthor():
    print("이루밍이루밍이루밍이루밍")

class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time

    def get_pay_info(self):
        return f"{self.time} {self.id} {self.price}"


# 해당 파일을 직접 실행했을 때만 실행되는 부분
if __name__ == "__main__":
    print("pay module 실행")
    print(__name__)