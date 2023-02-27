import socket

client = socket.socket() # 声明socket类型，同时生成socket连接对象；default is enough
client.connect(('localhost', 6969))

# client.send(b"Hello World!")
client.send("如果是中文的话，需要转码 abc".encode("utf-8"))

data = client.recv(1024)    # 收的长度为X字节
# print(f"Recv: {data}")
# 同样的，如果接收的是中文的话，需要解码
print(f"Recv: {data.decode()}")

client.close()