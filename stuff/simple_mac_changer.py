
import subprocess

interface = "wlan0"
new_mac = "3a:7e:12:19:aa:98"

print(f"Changing MAC address for {interface} to {new_mac}")

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)
