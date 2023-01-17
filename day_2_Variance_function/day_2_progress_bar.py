import sys, time

for i in range(20):
    sys.stdout.write("#")   # stdout 是标准输出，write 也就是输出到屏幕上
    sys.stdout.flush()      # 不用缓存满了再写上去，直接flush上去
    time.sleep(0.1)