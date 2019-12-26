from socket import *
from time import time
from threading import Thread
import random


'''This script connects to the s,r2,and 
d measures the avg. Rtt of the links between them
saves as measure.txt'''
'''
ipS-R1 =  "10.10.1.1"
ipR1-S = "10.10.1.2"
ipS-R2 = "10.10.2.2"
ipR2-S = "10.10.2.1"
ipS-R3 = "10.10.3.1"
ipR3-S = "10.10.3.2"
ipR1-R2 = "10.10.8.1"
ipR2-R1 = "10.10.8.2"
ipD-R1 = "10.10.4.2"
ipR1-D = "10.10.4.1"
ipR2-D = "10.10.5.1"
ipD-R2 = "10.10.5.2"
ipR2-R3 =  "10.10.6.1"
ipR3-R2 = "10.10.6.2"
ipR3-D = "10.10.7.2"
ipD-R3 = "10.10.7.1"
'''



def s_client(ip,portNo,files):
	
	mess = ['hello', 'bye', 'why', 'yes', 'no', 'maybe', 'are you sure', 'why not?']
	
	c = socket(AF_INET, SOCK_DGRAM)
	server = (ip,portNo)

	for i in range(100):
		time_before = time()
		c.sendto((str(time_before)).encode(),server)
		reply = c.recv(1024)
	c.close()

	


s_r3 = Thread(target=s_client,args=("10.10.3.2",10000,"measure1.txt"))


#thread starts
s_r3.start()


#out.close()