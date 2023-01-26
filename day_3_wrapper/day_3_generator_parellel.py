# 用生成器的yield来实现单线程下的并行效果
# 也称其为协程

import time

def consumer(name):
    print(f"{name}准备吃包子啦！")
    while True:
        baozi = yield
        print(f"包子{baozi}来了，被{name}吃了！")

# 验证consumer
c = consumer("Ming")    # 实例化
c.__next__()            # 唤醒yield
xian_1 = "韭菜馅"       # 准备一种馅料
c.send(xian_1)          # 回传包子馅，执行后面的代码。然后继续中断到yield处


def producer(name):
    c_1 = consumer("A")
    c_2 = consumer("B")
    c_1.__next__()
    c_2.__next__()
    print(f"{name}开始准备做包子啦！")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子！")
        c_1.send(i)
        c_2.send(i)

producer("Ming")