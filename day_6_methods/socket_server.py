import socket

server = socket.socket()

server.bind(("localhost", 6969))    # 绑定要监听的端口
server.listen() # 监听

print("我要开始等待数据了")
conn, addr = server.accept() # 等待连接的数据, conn就是那个连接, addr就是地址
# conn就是客户端连接时，再服务端为其生成的一个连接实例
print(f"Conn: {conn}\n Addr: {addr}")

print("The link is connected.")
data = conn.recv(1024)    # 接收发送端的数据
print(f"Recv: {data}")

conn.send(data.upper())   # 发送数据给发送端

server.close()