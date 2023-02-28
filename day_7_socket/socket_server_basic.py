import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                # self.request is the TCP socket connected to the client
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)

                # if not self.data:   # 如果收到的数据为空，即为断开了
                #     print(self.client_address, "断开了")
                #     break     # 手动断开会抛出异常，所以就用抓异常的方法，不用手动方法。
                
                # just send back the same data, but upper-cased
                self.request.send(self.data.upper())        #
                # self.request.sendall(self.data.upper())   # 

            except ConnectionResetError as e:
                print("Err", e)
                break

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # create the server, binding to localhost on port 9999
    # server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)   # 单线程
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)     # 多线程,并发，每次来一个连接，就实例化一个线程

    server.handle_request() # 处理单个请求，一般不会用
    # server.serve_forever(poll_interval=0.5) # 处理多个请求，每0.5s poll一次是否要shutdown,如果是，就杀死所有的线程