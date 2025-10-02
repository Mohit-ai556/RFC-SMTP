import socket

def smtp_server(host='127.0.0.1', port=2525):  
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"SMTP Server listening on {host}:{port}...")
    
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")
    
    conn.send(b"220 SimpleSMTPServer Ready\r\n")
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Client:", data.strip())
        
        if data.startswith("EHLO") or data.startswith("HELO"):
            conn.send(b"250 Hello\r\n")
        elif data.startswith("MAIL FROM"):
            conn.send(b"250 OK\r\n")
        elif data.startswith("RCPT TO"):
            conn.send(b"250 OK\r\n")
        elif data.startswith("DATA"):
            conn.send(b"354 End data with <CR><LF>.<CR><LF>\r\n")
        elif data == ".\r\n":
            conn.send(b"250 Message accepted\r\n")
        elif data.startswith("QUIT"):
            conn.send(b"221 Bye\r\n")
            break
        else:
            conn.send(b"500 Command not recognized\r\n")
    
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    smtp_server()
