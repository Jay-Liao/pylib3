import socket


server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind((socket.gethostbyname("localhost"), 8080))
server.listen(5)

while True:
    try:
        print("Waiting client...")
        client_socket, address_info = server.accept()
        msg = client_socket.recv(1024)
        print(f"accessed by: {address_info} msg: {msg}")
        msg_to_client = "hello world".encode()
        client_socket.send(msg_to_client)
        client_socket.close()
    except KeyboardInterrupt:
        server.close()
        break
