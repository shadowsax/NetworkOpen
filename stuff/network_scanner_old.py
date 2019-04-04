import scapy.all as scapy
import sys

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    #arp_request_broadcast.show()
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    #print(answered.summary())
    client_list = []
    for element in answered_list:
        target_ip = element[1].psrc
        target_mac = element[1].hwsrc
        client_list.append({"ip":target_ip, "mac": target_mac})
    print_result(client_list)


def print_result(result_list):
    print("IP\t\t\t\tMAC\n----------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

#scan("192.168.2.173") ipad
#scan("192.168.2.48") mypc
#scan("192.168.2.1") router
if __name__ == "__main__":
    try:
        ip = sys.argv[1]
        print("arg ip: ", ip)
        scan(ip)
    except:
        scan("192.168.2.173/24")
        

"""
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    #arp_request_broadcast.show()
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    #print(answered.summary())
    for element in answered_list:
        #element[0] send
        print("---------------------------------")
        print(element[0].show())
        my_ip = element[0].psrc
        my_mac = element[0].hwsrc
        print("my ip and mac: ", my_ip, my_mac)
        #element[1] receive
        print("---------------------------------")
        print(element[1].show())
        target_ip = element[1].psrc
        target_mac = element[1].hwsrc
        print("target ip and mac: ", target_ip, target_mac)




def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()
    #scapy.ls(scapy.ARP())
    #scapy.ls(scapy.Ether())


(scapy.ls(scapy.ARP()))
hwtype     : XShortField                         = 1               (1)
ptype      : XShortEnumField                     = 2048            (2048)
hwlen      : FieldLenField                       = None            (None)
plen       : FieldLenField                       = None            (None)
op         : ShortEnumField                      = 1               (1)
hwsrc      : MultipleTypeField                   = '94:e9:79:aa:21:97' (None)   MAC ADRESS
psrc       : MultipleTypeField                   = '192.168.2.48'  (None)       
hwdst      : MultipleTypeField                   = None            (None)
pdst       : MultipleTypeField                   = None            (None)


(scapy.ls(scapy.Ether()))
dst        : DestMACField                        = 'ff:ff:ff:ff:ff:ff' (None)
src        : SourceMACField                      = '94:e9:79:aa:21:97' (None)
type       : XShortEnumField                     = 36864           (36864)

"""




#will print
#request summary:  ARP who has Net('192.168.2.48/24') says 192.168.2.48
