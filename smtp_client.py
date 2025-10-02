import socket

def smtp_client(host= 127.0.0.1, port=2525):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(client_socket.recv(1024).decode())  
    
    commands = [
        "EHLO localhost\r\n",
        "MAIL FROM:<mewawamohit14@gmail.com>\r\n",
        "RCPT TO:<mewawamohit6@gmail.com>\r\n",
        "DATA\r\n",
        "Subject: Test Mail\r\nHello Bob, this is a test mail.\r\n.\r\n",
        "QUIT\r\n"
    ]
    
    for cmd in commands:
        client_socket.send(cmd.encode())
        print(">>", cmd.strip())
        print(client_socket.recv(1024).decode())

    client_socket.close()

if __name__ == "__main__":
    smtp_client()

