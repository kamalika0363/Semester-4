import socket

# create a UDP socket
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to a specific address and port
udp_server_socket.bind(('localhost', 8000))

print('UDP server is listening...')

while True:
    # receive data from the client
    data, address = udp_server_socket.recvfrom(1024)
    print(f'UDP message received from {address}: {data.decode()}')

    # send a response back to the client
    udp_server_socket.sendto(b'Thank you for the message!', address)
