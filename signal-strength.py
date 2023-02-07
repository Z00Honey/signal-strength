from scapy.all import *

# How to use
def usage():
    print("syntax : signal-strength <interface> <mac>")
    print("sample : signal-strength mon0 00:11:22:33:44:55")

# Handle packet
def get_signal_strength(packet):
    dbm_signal = packet.dBm_AntSignal
    ssid = packet[Dot11Elt].info.decode()
    print(ssid,dbm_signal)

# Check Parameter
if len(sys.argv) != 3:
    usage()
    sys.exit()

target ="ether src " + sys.argv[2] # Make filter target mac address
sniff(iface=sys.argv[1],filter=target, prn=get_signal_strength,count=0)
