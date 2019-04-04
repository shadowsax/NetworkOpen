import scapy.all as scapy
import sys
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    #arp_request_broadcast.show()
    answered_list = scapy.srp(arp_request_broadcast,
                              timeout=1, verbose=False)[0]
    #print(answered.summary())
    client_list = []
    for element in answered_list:
        target_ip = element[1].psrc
        target_mac = element[1].hwsrc
        client_list.append({"ip": target_ip, "mac": target_mac})
    #print_result(client_list)
    return client_list


def print_result(result_list):
    print("IP\t\t\t\tMAC\n----------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)

#scan("192.168.2.173/24")
