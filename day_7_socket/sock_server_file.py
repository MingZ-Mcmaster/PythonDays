import socket
import hashlib
import os

server = socket.socket()
server.bind(("localhost", 999))
server.listen()

conn, addr = server.accept()

while True:
    print("等待文件")
    data = conn.recv(1024)
    if not data:
        print("客户端已断开")
        break
    cmd, filename = data.decode().split()
    print(filename)

    if os.path.isfile(filename):
        f = open(filename, 'rb')    # 因为打开模式为byte,所以发送就不要encode了
        m = hashlib.md5()
        file_size = os.stat(filename).st_size

        conn.send( str(file_size).encode() )    # send the file size
        conn.recv(1024) # wait for ack
        for line in f:
            m.update(line)  # 
            conn.send(line) # 打开模式为byte,所以没有encode

        print("File MD5: ", m.hexdigest())
        f.close()

        conn.send(m.hexdigest().encode())
    
    print("Send is done.")

server.close()