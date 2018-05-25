#coding:UTF-8
import socket
import sys,getopt

'''
作者：张乐
时间：2018.5.25 9:42
用处：用来扫描计算机开放的端口
'''

def usage():
	print('USAGE:')
	print('    [-h] help')
	print('    [-i] IP')
	print('    [-s] Begin the scan from this port')
	print('    [-e] End the scan from this port')	

#扫描一个端口
def scanOnePort(url,port):
	print("[+]Connecting %s : %d " % ( url, port ))
	
	#establish a socket connection and send a message
	s = socket.socket()
	try:
		s.connect( ( url, port ) )
		s.send(b'hello \n')

		msg = s.recv(1024)
		if( len(msg) ):
			print(msg)
			return(msg)
	#由于在大多数端口都是不开放的，所以对于异常情况，我们忽略
	except Exception as e:
		#print(e)
		return False
	return False


def scanAllPort(argv):
	IP = '127.0.0.1'
	beginPort = 0
	endPort = 0
	
	result = {}
	try:
		opts,args = getopt.getopt(argv,"hi:s:e:",["IP=","beginPort=","endPort="])
	except getopt.GetoptError:
		print('unknown parameter')
		usage()
		sys.exit(2)

	for opt,arg in opts:
		if (opt == "-h" ):
			usage()
			sys.exit()

		elif (opt == "-i" ):
			IP = arg
			
		elif (opt == "-s" ):
			beginPort = arg
		
		elif (opt == "-e" ):
			endPort = arg
	
	for port in range(int(beginPort),int(endPort)):
		oneResult = scanOnePort(IP,port)
		if (oneResult):
			k = "%s:%d"%(IP,port)
			result[k] = str(oneResult)
			#result.join( "%s:%d"%(IP,port) = oneResult )
	
	print("本次扫描结果：")
	print("    扫描IP：%s"%(IP))
	print("    扫描端口：%d个"%(abs(int(endPort)-int(beginPort))))
	print("    其中开放的端口共有：%d个，分别是："%(len(result)))
	
	i = 0
	for k,v in result.items():
		i = i + 1
		print("        [%d] %s:%s"%(i,k,v))    
	
if __name__ == "__main__":
	scanAllPort(sys.argv[1:])
