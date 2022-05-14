from multiprocessing import Process
import time

class Sub_Process(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name
    
    def run(self):
        print(f"[sub] {self.name} start")
        time.sleep(5)
        print(f"[sub] {self.name} end")

print("[main] start")
p = Sub_Process(name='irumdev')
p.start()
time.sleep(1)

# 프로세스가 살아 있는지 검사
print(p.is_alive())

# 프로세스 강제 종료
p.terminate()


print("[main] end")


# 추가학습하면 좋은 것들
# 1. 스레드간 데이터 처리 (lock)
# 2. 프로세스간 데이터 전송 (Queue, Pipe)
# 3. 속도 비교 (멀티스레딩, 멀티프로세싱 사용유무에 따른)
# 4. 운영체제와 메모리 (자원사용량)
