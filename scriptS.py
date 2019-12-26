from socket import *
from threading import Thread



def s_server(ip,portNo): ## Sanki dogru
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



server_r1 = Thread(target= s_server,args=("10.10.1.1",10000,))
server_r2 = Thread(target= s_server,args=("10.10.2.2",10006,))
server_r3= Thread(target= s_server,args=("10.10.3.1",10003,))   

#thread starts

server_r1.start()
server_r2.start()
server_r3.start()