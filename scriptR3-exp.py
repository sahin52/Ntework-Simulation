from socket import *
from time import time
from threading import Thread
import random


def r3_client():
	
	mess = ['hello', 'bye', 'why', 'yes', 'no', 'maybe', 'are you sure', 'why not?']
	
	c = socket(AF_INET, SOCK_DGRAM)
	server = (("10.10.7.1",10001))
	s = socket(AF_INET, SOCK_DGRAM)
	s.bind(("10.10.3.2",10000))
	

	for i in range(100):
		
		try:
			s = socket(AF_INET, SOCK_DGRAM)
			s.bind(("10.10.3.2",10000))
			
			msg,peer = s.recvfrom(1024)
			if msg == "":
				break
			c.sendto(msg,server)
			reply = c.recv(1024)

			if c!="":
				s.sendto(msg,peer)
		finally:
			s.close()
	c.close()


def r3_server(ip,portNo): ## Sanki dogru
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

r3_d = Thread(target= r3_client, args=())


## threads starts
r3_d.start()
#server_s.start()

#r2_server("10.10.6.1",10000,)
