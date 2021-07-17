import socket

SERVER_HOST_PORT = ("127.0.0.1", 1234)

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.connect(SERVER_HOST_PORT)
data = socket_obj.recv(1024)
print(f"got data from server: {data}")
