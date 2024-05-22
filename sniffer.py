from scapy.all import sniff, TCP, IP

def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_layer = packet.getlayer(IP)
        tcp_layer = packet.getlayer(TCP)
        
        print(f"New Packet: {packet.summary()}")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Source Port: {tcp_layer.sport}")
        print(f"Destination Port: {tcp_layer.dport}")
        print(f"Payload: {bytes(packet[TCP].payload)}")
        print("-" * 50)

# Sniff packets on the specified network interface (wlp2s0)
sniff(iface="wlp2s0", prn=packet_callback, filter="tcp", store=0)


