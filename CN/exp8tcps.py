import socket

# create a TCP socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
tcp_server_socket.bind(('localhost', 8000))

# listen for incoming connections (accept up to 5)
tcp_server_socket.listen(5)

print('TCP server is listening...')

while True:
    # accept a new connection
    client_socket, address = tcp_server_socket.accept()
    print(f'TCP connection established with {address}')

    # receive data from the client
    data = client_socket.recv(1024)
    print(f'Client sent: {data.decode()}')

    # print user input from the client
    print(f'Client sent: {client_socket.recv(1024).decode()}')

    # send a response back to the client
    client_socket.send(b'Thank you for connecting!')

    # close the connection
    client_socket.close()
