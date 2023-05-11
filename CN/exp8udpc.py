import socket

# create a UDP socket
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send user input to the server
udp_client_socket.sendto(input('Enter your msg: ').encode(), ('localhost', 8000))

# receive a response from the server
response, server_address = udp_client_socket.recvfrom(1024)
print(response.decode())

# close the connection
udp_client_socket.close()
