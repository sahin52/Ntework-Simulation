from socket import *
from time import time
from threading import Thread
import random


def r2_client(ip,portNo,files):
	
	mess = ['hello', 'bye', 'why', 'yes', 'no', 'maybe', 'are you sure', 'why not?']
	
	c = socket(AF_INET, SOCK_DGRAM)
	server = (ip,portNo)
	rtt_val = []

	for i in range(1000):
		print(i)
		time_before = time()
		c.sendto(random.choice(mess).encode(),server)
		reply = c.recv(1024)
		time_after = time()
		rtt_val.append(time_after-time_before)
	c.close()

	sum = 0
	for i in rtt_val:
		sum += i
	avg = sum/float(len(rtt_val))

	with open(files,"w") as out:
		out.write(str(portNo)+": "+str(avg))


def r2_server(ip,portNo): ## Sanki dogru
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

r2_s = Thread(target= r2_client, args=("10.10.2.2",10006,"measure1.txt"))
r2_d = Thread(target= r2_client, args=("10.10.5.2",10007,"measure2.txt"))

server_r1 = Thread(target= r2_server,args=("10.10.8.2",10001,)) 
server_r3 = Thread(target= r2_server,args=("10.10.6.1",10004,))

## threads starts
r2_s.start()
r2_d.start()
server_r1.start()
server_r3.start()

#r2_server("10.10.6.1",10000,)
