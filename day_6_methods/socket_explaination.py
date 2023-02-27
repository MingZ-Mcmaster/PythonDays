
# OSI
# Pysical: 01010101
# link: Mac addr
# network: ip addr; icmp是个arp，就是ping
# transportation: 大部分的数据在传输层
    # TCP/IP: 三次握手，四次断开
    # UDP：
# Session
# presentation
# application

# 各种传输协议
    # 网站协议：http
    # 邮件协议：smtp
    # 域名协议：dns
    # 传输协议：ftp, ssh
    # 简单网络监控的协议：snmp
    # ping协议：icmp
    # ip地址分配协议：dhcp
    # ...
# 都包含收发，为了方便、简化和统一，使用了同一个接口就是socket

# A(Receiver)                   B(Transimitter)
# nginx 80                      qq
# mysql 3306                    ssh
# Ming 6969                     weixin
#
# import socket                 import socket
# socket.TCP/IP                 socket.TCP/IP
# listen(0.0.0.0, 6969)         connect(a.ip, a.port)
# waiting()                     socket.send(hello)
# socket.recv()                 
# socket.send()                 
#                               socket.recv()
#                               socket.close()    