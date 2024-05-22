# cybersecurity
Basic Network sniffer

The network sniffer can be a hardware either a software which is used to monitor network traffic.
It is also called as packet sniffer because the data in a network is transmitted in the form of packets.
packet analyzer,protocol analyzer and network analyzer are its other names.
Sniffers work by examining streams of data that flow on a network i.e between computer or network devices.
The network sniffers opens upto all data traffic of the network by opening the system's NIC(Network Interface Card) to listen to that traffic.The software reads the data and 
performs data analysis or data extraction on it.
Basic Sniffers works with only TCP/IP packets but the well developed and sophisticated sniffers works with ethernet frames and low level networking protocols.
I am building a basic network sniffer in linux environment as a part of this project.
STEPS TO BUILD THE BASIC NETWORK SNIFFER:
1)Open the terminal and enter the command "ifconfig" to get the available network interfaces on your system and use a network interface in the sniffer script at inf='network name')
2)install scapy using pip3(python package installer). Scapy is a python library which is used for network manipulation.
3)Now write the required sniffer script in the editor(let's say it was named as 'sniffer.py').
4)execute the sniffer script in the terminal( 'sudo python3 sniffer.py').
5)The output shows the detailed captured the TCP/IP packets,including IP addresses,port numbers and payload.
