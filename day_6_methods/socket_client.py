import socket

client = socket.socket() # 声明socket类型，同时生成socket连接对象；default is enough
client.connect(('localhost', 6969))

client.send(b"Hello World!")

data = client.recv(1024)    # 收的长度为X字节
print(f"Recv: {data}")

client.close()