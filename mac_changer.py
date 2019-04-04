
import subprocess

new_mac = "00:11:22:33:44:66"

print("<------Select interface below----------->")
subprocess.call("ifconfig -s", shell=True)
print("----------------------------------------")
interface = input("interface >")







print(f"Changing MAC address for {interface} to {new_mac}")

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)
