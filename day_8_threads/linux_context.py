# pwd           所在位置
# more /etc/passwd

# passwd user   改user密码
# su - user     换成user账户
        # 只要登录过一个账户，就会自动生成.ssh

# 权限
# r(4读)    w(2写)  x(1执行)
# rwx(属主)  rwx（属组） rwx（others）
# chmod 777 file_name       改变file_name的权限为777，所有人都可以读写执行
# chmod 600 file_name       只能用户自己读写

# ssh-keygen        生成密钥 RSA, DSA, ECC
        # 生成 id_rsa（私钥） & id_rsa.pub(公钥)
        # 私钥自己，公钥给别人，这样便可以登录有公钥的机器了。这是单向的。
    # 可以拷到.ssh/下
    # 也可以 ssh-copy-id "-pXXX user_name@ip_address"

    # ssh user_name@ip_address -pXXX    SSH免密登录，如果需要调试，增加 -v

# vim
    # dd 删除

# 查找端口号
    # netstat -tulnp
    # netstat -tulnp|grep 22                ssh默认端口22
    # netstat -tulnp|grep ssh

# 虚拟机传文件
    # rz        通过 ZMODEM 协议, 将本地文件批量上传到远程 Linux/Unix 服务器，注意不能上传文件夹。
    # sz path/file        通过 ZMODEM 协议，可将多个文件从远程服务器下载到本地。