import string, secrets, os, socket
def serial_KeyGEN():
   m=''.join(secrets.choice(string.digits) for i in range(8))
   if '12340000' == m:
    m=''.join(secrets.choice(string.digits) for i in range(8))
    return m
   else:
        return m
def serialkey():
   l=input("serialkey: ")
   HOST = "127.0.0.1"  # The server's hostname or IP address
   PORT = 65432  # The port used by the server
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s.connect((HOST, PORT))
       s.sendall(l.encode())
       data = s.recv(1024)
       if data == b'fuck':
        print("PIRACY IS NO PARTY")
        os.system("/usr/local/bin/python3 hack")
       else:
            return True
