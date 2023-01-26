# 列表生成式: 一行
a = [i*2 for i in range(10)]

print(a)

# 常规列表生成方式：需要三行
a = []
for i in range(10):
    a.append(i*2)

print(a)

# 生成器：边循环调用，边生成序列，省内存

b = ( i*2 for i in range(10) )  # 就是个算法的地址
print(b)
for i in b: # 只有调用的时候，才能执行，否则就不会执行
    print(i)

# 生成器的__next__()唯一方法
#   只保存当前位置，也只能用__next__()方法去往后继续
b = ( i*2 for i in range(10) )
print(b.__next__()) # 0
print(b.__next__()) # 2
print(b.__next__()) # 4


# Fibonacci (斐波那契数列)
#   1. 用函数生成
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # 2. 若想用生成器替代，仅需将print(b)替换成yield b
        # print(b)
        yield b # 中断一下出去，等调用的时候再次回来
        a, b = b , a+b
        n = n + 1
    return "Done"

# 1. 用函数生成时的调用，会比较占用内存
fib(10)
# 2. 用生成器的方式调用，会省内存
f = fib(10)        # 运行函数
print(f.__next__()) # 1；跳出，被打印，再进去继续运行函数
print(f.__next__()) # 1；跳出，被打印，再进去继续
print(f.__next__()) # 2
print(f.__next__()) # 3
print(f.__next__()) # 5

print("----start loop----")
for i in f:         # 6 用loop把剩余的都打印出来
    print(i)

# 3. 此时如果函数已经运行完了，继续运行f.__next__()会报错
#   所以来抓取异常
g = fib(6)
while True:
    try:
        x = next(g)
        print("g: ", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break