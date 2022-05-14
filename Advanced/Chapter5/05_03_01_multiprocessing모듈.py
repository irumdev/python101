import multiprocessing as mp

# 프로세스에서 실행할 함수
def sub_process(name):
    print("[sub] start")
    print(name)
    cp = mp.current_process()
    print(f"[sub] pid : {cp.pid}")
    print("[sub] end")

# 메인 프로세스
# if __name__ == "__main__":
print("[main] start")
p = mp.Process(target=sub_process, args=('irumdev',))
p.start()
cp = mp.current_process()
print(f"[main] pid : {cp.pid}")
print("[main] end")
