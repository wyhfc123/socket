import socket
host=socket.gethostname()
port=12345
#创建TCP/IP套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
sock,addr=s.accept()
print("连接已建立")
info=sock.recv(1024).decode()
while info !='byebye':
    if info:
        print('接收到的内容:',info)
    send_data=input("请输入要发送的内容")
    sock.send(send_data.encode())
    if send_data=='byebye':
        break
    info=sock.recv(1024).decode()
#关闭客户端套接字
sock.close()
#关闭服务器端套接字
s.close()