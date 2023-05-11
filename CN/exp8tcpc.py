import socket

# create a TCP socket
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
tcp_client_socket.connect(('localhost', 8000))

# send user input to the server
tcp_client_socket.send(input('Enter your msg: ').encode())

# receive a response from the server
response = tcp_client_socket.recv(1024)
print(response.decode())

# close the connection
tcp_client_socket.close()
