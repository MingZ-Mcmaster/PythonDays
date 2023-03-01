import threading
import time

class MyThread(threading.Thread):
    def __init__(self, n, sleep_time) -> None:
        super(MyThread, self).__init__()
        self.n = n
        self.sleep_time = sleep_time

    def run(self):  # 类的方式必须是run
        print("running task ", self.n)
        time.sleep(self.sleep_time)
        print("Done", self.n)

start_time = time.time()

t1 = MyThread("t1", 2)
t2 = MyThread("t2", 4)

t1.start()
t2.start()

t1.join()   # 相当于其它语言中的wait(), 在等t1的结果
t2.join()   # 如果线程中的时间不同，就需要再加上等待t2的结果

print("Main Threading")
end_time = time.time()
print("Cost time: ", end_time-start_time)