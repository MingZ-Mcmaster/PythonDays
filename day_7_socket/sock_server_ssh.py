import socket
import time
import os

server = socket.socket()
server.bind( ("localhost", 9999) )

server.listen()

while True:
    conn, addr = server.accept()
    print("New ", conn, addr)

    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令：", data)
        cmd_res = os.popen(data.decode()).read()    # 接收的是字符串，所以要执行，就需要decode
        print("Before send back:", len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output..."    # 字符串不能用byte，否则后面的encode就不能了

        conn.send(  str(len(cmd_res.encode())).encode("utf-8")  )    # 先发文件大小
        
        # time.sleep(0.5)     # 防止粘包，但是会拖慢速度
        client_ack = conn.recv(1024)    # 等待用户确认，防止粘包
        print("Ack from client:", client_ack.decode())
        
        conn.send(cmd_res.encode("utf-8"))   # 发送的也必须是字符串，所以要encode
        print("Send Done.")

server.close()