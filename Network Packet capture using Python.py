import socket
import struct

# create a raw socket
raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# receive a packet
packet = raw_socket.recvfrom(65535)[0]

# extract the IP header fields
ip_header = packet[0:20]
ip_version, ip_protocol, ip_total_length, ip_source_address, ip_destination_address = struct.unpack('!BBHHH', ip_header[0:8] + ip_header[9:20])

# extract the TCP header fields
tcp_header = packet[20:40]
tcp_source_port, tcp_destination_port, tcp_sequence_number, tcp_acknowledgement_number, tcp_data_offset_reserved_flags, tcp_window_size, tcp_checksum, tcp_urgent_pointer = struct.unpack('!HHLLBBHH', tcp_header)

# extract the data payload
data = packet[40:]

# print the packet contents
print("IP Version: {}".format(ip_version))
print("IP Protocol: {}".format(ip_protocol))
print("IP Total Length: {}".format(ip_total_length))
print("IP Source Address: {}".format(socket.inet_ntoa(struct.pack('!I', ip_source_address))))
print("IP Destination Address: {}".format(socket.inet_ntoa(struct.pack('!I', ip_destination_address))))
print("TCP Source Port: {}".format(tcp_source_port))
print("TCP Destination Port: {}".format(tcp_destination_port))
print("TCP Sequence Number: {}".format(tcp_sequence_number))
print("TCP Acknowledgement Number: {}".format(tcp_acknowledgement_number))
print("TCP Data Offset/Reserved/Flags: {}".format(tcp_data_offset_reserved_flags))
print("TCP Window Size: {}".format(tcp_window_size))
print("TCP Checksum: {}".format(tcp_checksum))
print("TCP Urgent Pointer: {}".format(tcp_urgent_pointer))
print("Data Payload: {}".format(data))
