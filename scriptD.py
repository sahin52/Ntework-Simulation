from socket import *
from threading import Thread



def d_server(ip,portNo): ## Sanki dogru
	s = socket(AF_INET, SOCK_DGRAM)
	s.bind((ip,portNo))
	
	while True:
		try:
			s = socket(AF_INET, SOCK_DGRAM)
			s.bind((ip,portNo))
			msg,peer = s.recvfrom(1024)
			if msg == "":
				break
			print("received")
			s.sendto(msg,peer)
		finally:
			s.close()



server_r1 = Thread(target= d_server,args=("10.10.4.2",10002,))
server_r2 = Thread(target= d_server,args=("10.10.5.2",10007,))
server_r3= Thread(target= d_server,args=("10.10.7.1",10005,))   

#thread starts

server_r1.start()
server_r2.start()
server_r3.start()