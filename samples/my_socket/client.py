import socket


client = socket.socket()
client.connect((socket.gethostbyname("localhost"), 8080))
msg_to_server = "123".encode()
client.send(msg_to_server)
msg = client.recv(1024)
print(f"receive msg from server: {msg}")
client.close()
