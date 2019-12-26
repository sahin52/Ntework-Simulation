from socket import *
from threading import Thread
from time import time


def d_server(ip,portNo,files): ## Sanki dogru
	s = socket(AF_INET, SOCK_DGRAM)
	s.bind((ip,portNo))
	
	end2end_val = []

	for i in range(100):
		try:
			s = socket(AF_INET, SOCK_DGRAM)
			s.bind((ip,portNo))
			msg,peer = s.recvfrom(1024)
			rcv = time()
			if msg == "":
				s.sendto("NACK".encode(),peer)
				break
			#print("received")
			s.sendto("ACK".encode(),peer)
			end2end_val.append(rcv-float(msg))
		finally:
			s.close()
	s.close()
	sum = 0
	for i in end2end_val:
		sum += i
	avg = sum/float(len(end2end_val))

	with open(files,'a') as out:
		out.write(str(portNo)+": "+str(avg)+"\n")



server_r3 = Thread(target= d_server,args=("10.10.7.1",10001,"measure.txt"))

#thread starts
server_r3.start()