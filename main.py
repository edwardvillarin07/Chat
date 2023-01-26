import socket


def main():
    host = "127.0.0.1"  # IP address of the server
    port = 1234  # Port to listen on

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(2)  # allows for two clients to connect
    print("[+] Listening for incoming connections...")
    conn1, addr1 = s.accept()
    print("[+] Connection from: " + str(addr1))
    conn2, addr2 = s.accept()
    print("[+] Connection from: " + str(addr2))

    while True:
        message1 = conn1.recv(1024).decode()  # receives message from client 1
        conn2.send(message1.encode())  # sends message to client 2
        message2 = conn2.recv(1024).decode()  # receives message from client 2
        conn1.send(message2.encode())  # sends message to client 1


if __name__ == "__main__":
    main()