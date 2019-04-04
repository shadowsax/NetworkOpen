import subprocess

print("Installing required packages...\n")
subprocess.call("aptitude -r install network-manager-openvpn-gnome network-manager-pptp network-manager-pptp-gnome network-manager-strongswan network-manager-vpnc network-manager-vpnc-gnome -y", shell=True)

print("Installing network-manager-openvpn...\n")
subprocess.call("apt-get install network-manager-openvpn", shell=True)

print("networking is restarting...\n")
subprocess.call("service networking restart")

print("Network manager is restarting again...\n")
subprocess.call("service network-manager restart")

print("Downloading openvpn certificates...\n")
subprocess.call("wget https://www.privateinternetaccess.com/openvpn/openvpn.zip")

print("Extracting certificates to '/etc/openvpn'\n")
subprocess.call("unzip -q openvpn.zip -d /etc/openvpn")


print("""
    Go to Network Manager > Edit Connections\n
    Change to VPN Tab. VPN> Add\n
    Click [ADD +] click the drop down menu, and set the type as OpenVPN.\n
    \n\n\n
    Go to “VPN” and fill up the following details”.\n
    \n
    Connection name: PrivateInternetAccess VPN\n
    Gateway:  us-east.privateinternetaccess.com [**choose Gateway's from the list below]\n
    Username: PIA Username\n
    Password: PIA Password\n
    CA Certificate: Browse to /etc/openvpn and select ca.crt\n
    \n
    Click [Advanced]: Check the box next to “Use LZO data compression“\n
    Click [OK], [Save] and then [Close].\n
    \n\n\n
    As for Gateways, choose on the following depending on your location:
    \n\n
    --------------------------------------\n
    PIA Regional Gateways\n\n
    United States (US VPN)\n
    us-midwest.privateinternetaccess.com\n
    us-east.privateinternetaccess.com\n
    us-west.privateinternetaccess.com\n
    us-texas.privateinternetaccess.com\n
    us-california.privateinternetaccess.com\n
    us-florida.privateinternetaccess.com\n\n
    Canada (CA VPN)\n
    ca.privateinternetaccess.com\n
    ca-toronto.privateinternetaccess.com\n\n
    United Kingdom (UK VPN)\n
    uk-london.privateinternetaccess.com\n
    uk-southampton.privateinternetaccess.com\n\n
    Switzerland (Swiss VPN)\n
    swiss.privateinternetaccess.com\n\n
    Netherlands (NL VPN)\n
    nl.privateinternetaccess.com\n\n
    Sweden (SE VPN)\n
    sweden.privateinternetaccess.com\n\n
    France (FR VPN)\n
    france.privateinternetaccess.com\n\n
    Germany (DE VPN)\n
    germany.privateinternetaccess.com\n\n
    Romania (RO VPN)\n
    ro.privateinternetaccess.com\n\n
    Hong Kong (HK VPN)\n
    hk.privateinternetaccess.com\n\n
    Israel (Israel VPN)\n
    israel.privateinternetaccess.com\n\n
    Australia (Australia VPN)\n
    aus.privateinternetaccess.com\n\n
    Japan (Japan VPN)\n
    japan.privateinternetaccess.com\n\n
""")
