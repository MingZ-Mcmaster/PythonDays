__author__ = "Ming"
# import os
# print(os.getcwd)

# 方法1：内容已经放到内存里了
# data_1 = open(r"day_2_Variance_function\lyric.txt", 'r', encoding='utf-8').read()

# 方法2：文件句柄：指向内存里的内容
f = open(r"day_2_Variance_function\lyric.txt", 'r', encoding='utf-8')   # read only
#   读文件内容
print(f.readline()) # 读了第一行
data_2 = f.read()   # 读了剩下的所有，因为指针指到了第二行
f.close()
print(data_2)

#   写文件会创建文件，如果不改名会被覆盖
f = open(r"day_2_Variance_function\lyric_2.txt", 'w', encoding='utf-8')   # create a file and write only
f.write("我爱北京天安门,\n")
f.close()
#   追加写文件
f = open(r"day_2_Variance_function\lyric_2.txt", 'a', encoding='utf-8') 
f.write("天安门上太阳升")
f.close()

# 读成列表： readlines读小文件还可以，内存空间还够，大文件会溢出
print("--------------")
with open(r"day_2_Variance_function\lyric.txt", "r", encoding='utf-8') as f:        
    data = f.readlines()
    print(data)

with open(r"day_2_Variance_function\lyric.txt", "r", encoding='utf-8') as f:
    for i in f.readlines():
        print(i.strip())    # 去掉回车

# 读文件，跳过某一行
with open(r"day_2_Variance_function\lyric.txt", "r", encoding='utf-8') as f:
    for index, line in enumerate(f.readlines()):
        if index == 9:
            print("----跳过----")
            continue
        print(line.strip())

# 读文件，每次只保存一行,效率最高，可行性最强
with open(r"day_2_Variance_function\lyric.txt", "r", encoding='utf-8') as f:
    for line in f:
        print(line.strip())
# 读文件，每次只保存一行，跳过某一行
with open(r"day_2_Variance_function\lyric.txt", "r", encoding='utf-8') as f:
    count = 0
    for line in f:
        if count == 9:
            print("----跳过----")
            count += 1
            continue
        print(line.strip())
        count += 1

# 读文件，查找指针，指定指针位置
with open(r"day_2_Variance_function\lyric.txt", "r", encoding='utf-8') as f:
    print("当前位置: ", f.tell())
    print("读一行：",f.readline())
    print("现在的位置", f.tell())
    # 读取5个字符，每个字符3个Bytes
    print("再读5个", f.read(5))
    print("现在的位置", f.tell())
    # 重新复位
    f.seek(0)
    print("复位后：",f.readline())

# 其它指令
with open(r"day_2_Variance_function\lyric.txt", "r", encoding='utf-8') as f:
    # 打印字符编码
    print(f.encoding)
    # 返回文件在内存中的编号，并不是内存的地址
    print(f.fileno())   # OS内部的操作接口

with open(r"day_2_Variance_function\lyric_2.txt", "a", encoding='utf-8') as f:
    # 截断：指定位置，后面的都清空
    f.truncate(27)

# 读写文件: r+(读写)， w+(写读)， a+(追加读写)， rb(二进制文件，不能加encoding，一般用于网络传输中)
with open(r"day_2_Variance_function\lyric_2.txt", "r+", encoding='utf-8') as f:
    f.readline().strip()
    f.write("----------")

    # rb 读二进制
with open(r"day_2_Variance_function\lyric_2.txt", "rb") as f:
    print("读一行二进制", f.readline() )
    # ab 追加二进制
with open(r"day_2_Variance_function\lyric_2.txt", "ab") as f:
    f.write("hello binary\n".encode())
    # wb 同理，写二进制，但是会清空之前的内容
with open(r"day_2_Variance_function\lyric_2.txt", "wb") as f:
    f.write("hello binary\n".encode())