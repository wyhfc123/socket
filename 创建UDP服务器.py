import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8080))
data,addr=s.recvfrom(1024)
data=float(data)*2
send_data="计算后的data:"+str(data)
print('从客户端接收:',addr)
s.sendto(send_data.encode(),addr)
s.close()