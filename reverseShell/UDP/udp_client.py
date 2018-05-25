#coding:utf-8
'''
作者：张乐
日期：2018.5.25 11.17
作用：udp通信客户端
'''

import socket

host = '127.0.0.1'
port = 1024
buf_size = 128

addr = (host,port)

udp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while(True):
	data = raw_input('>')
	if not data:
		break
	udp_client.sendto(data,addr)
udp_client.close()
