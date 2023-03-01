import threading
import time

def run(n):
    print("Task ", n)
    time.sleep(2)
    print("Done")

#====================================
## 一个线程一个线程的生成
# t1 = threading.Thread(target=run, args=("t1",)) # target的任务不需要（）, args里就算只有一个参数，也需要用逗号隔开
# t2 = threading.Thread(target=run, args=("t2",))
# t1.start()
# t2.start()

#====================================
## 循环启动线程, 如果没有特殊机制的话，不能统计时间
# start_time = time.time()

# for i in range(50):     # 这段循环程序因为主线程启动的多线程，所以后面的主程序不会等多线程完成
#     t = threading.Thread(target=run, args=(f"t-{i}",))
#     t.start()

# end_time = time.time()  # 也就是这段计时不会考虑多线程的时间
# print("cost: ", end_time-start_time)

#====================================
## 循环启动线程
start_time = time.time()
task = []       # 创建了一个多线程的任务列表

for i in range(50):    
    t = threading.Thread(target=run, args=(f"t-{i}",))
    t.start()
    task.append(t)      # 每次启动一个线程后，就将此线程的task放入列表

for i in task:     # 在这个循环里面，等待线程任务列表里的每一个任务
    i.join()

end_time = time.time()  # 等待所有线程并行走完后，统计时间
print("cost: ", end_time-start_time)