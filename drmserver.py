
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
establishedlics=["44559999"]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"DRM Client:{addr}...............................................................................................")
        while True:
            data = conn.recv(1024)
            if not data:
             break
            for i in establishedlics:
                if str(i).strip("[]") == data.decode():
                 conn.sendall(b'CX53G63')
                else:
                     conn.sendall(b'fuck')
                      
