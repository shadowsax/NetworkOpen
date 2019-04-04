import scapy.all as scapy 

packet = scapy.ARP(op=2, pdst="192.168.2.173", hwdst="80:d6:05:1d:3f:6d", psrc="192.168.2.1")
