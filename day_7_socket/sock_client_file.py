import socket
import hashlib

client = socket.socket()
client.connect( ("localhost", 999) )

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue

    if cmd.startswith("get"):
        client.send(cmd. encode())
        server_response = client.recv(1024)
        print("Server response: ", server_response.decode())    # file size

        client.send(b"Ready to recv file")

        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + ".new", 'wb')   # 打开模式为byte，后面接收和写入也都是按照byte
        m = hashlib.md5()

        while received_size < file_total_size:
            if file_total_size - received_size > 1024:  # 拆包，要收不止一次
                size = 1024
            else:   # 拆包，最后一次，剩下多少
                size = file_total_size-received_size
                print("Last receive size:", size)

            data = client.recv(size)    # 根据拆包来调整
            received_size += len(data)

            m.update(data)
            f.write(data)

        new_file_md5 = m.hexdigest()
        print("Received file is done. ", received_size, file_total_size)
        f.close()

        server_file_md5 = client.recv(1024)
        print("Server file MD5:", server_file_md5)
        print("Client file MD5:", new_file_md5)