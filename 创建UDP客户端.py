import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data=input("请输入数字")
s.sendto(data.encode(),('127.0.0.1',8080))
print(s.recv(1024).decode())
s.close()