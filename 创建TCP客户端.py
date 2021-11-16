import socket
host='127.0.0.1'
port=8080
#创建socket对象
client=socket.socket()
#初始化TCP服务器连接
client.connect((host,port))
send_data=input("请输入要发送的内容：")
#发送TCP数据
client.send(send_data.encode())
#接收数据
recv_data=client.recv(1024).decode()
print('接收到的数据：',recv_data)
client.close()



