import socket
host='127.0.0.1'
port=8080
#创建socket对象
web=socket.socket()
#绑定主机和端口号
web.bind((host,port))
#设置最多连接数
web.listen(5)
print('服务器等待客户端连接')
while True:
    #建立客户端连接
    conn,addr=web.accept()
    #获取客户端请求数据
    data=conn.recv(1024)
    print(data)
    conn.sendall(b'HTTP/1.1 200 OK\r\n\r\nhello world')
    conn.close()


