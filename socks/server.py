import socket

HOST_PORT = ("127.0.0.1", 1234)

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.bind(HOST_PORT)
socket_obj.listen(3)
print(f"server running at {HOST_PORT}")

while True:
    client_soc, addr = socket_obj.accept()
    print(f"client: {addr}")
    client_soc.send(b"hell0 from server")
