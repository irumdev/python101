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
p.join()
print("[main] end")
