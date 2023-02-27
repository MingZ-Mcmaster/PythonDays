import socket

client = socket.socket()

client.connect(("localhost", 9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue  # 不能为空，所以要继续输入

    client.send(cmd.encode("utf-8"))

    cmd_res_size = client.recv(1024)    # 先接收命令结果的长度
    print(cmd_res_size)
    client.send( ("准备好接收了,server可以发了").encode("utf-8") )

    received_size= 0        # 初始化
    received_data = b''     # 初始化
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)  # 每次收到的有可能小于1024，所以必须用len来判断
        # print(data.decode())
        received_data += data

    else:
        print("cmd res receive is done...\n", received_size)
        print(received_data.decode())

    

client.close()