
import scapy.all as scapy


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    print("a",packet)

    #print("decoded", packet.decode())


sniff("wlp3s0")
#sudo /home/jb/anaconda3/bin/python packet_sniffer.py


