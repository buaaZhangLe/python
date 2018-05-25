#coding:utf-8
'''
作者：张乐
日期：2018.5.25 11.10
用途：udp通信服务端
'''

import socket

host = ""
port = 1024
buf_size = 128

addr = (host,port)

udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_server.bind(addr)

while(True):
	print("Wating message...")
	data,addr = udp_server.recvfrom(buf_size)
	print('...received from and return to:%s : %s'%(str(addr),data))
udp_server.close()
