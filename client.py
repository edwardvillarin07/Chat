import socket

def main():
    host = "127.0.0.1"  # IP address of the server
    port = 1234  # Port to connect to

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        message = input("Enter message: ")  # prompts user for message
        s.send(message.encode())  # sends message to server
        data = s.recv(1024).decode()  # receives message from other client
        print("Received from other client: " + data)

if __name__ == "__main__":
    main()
