import os, socket
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
            open("coolos","w").write(socket.gethostname()+l)
def UACheck():
   l=input("Serialkey??")
   # If the programs execs for its first time use serial key check.
   if os.path.exists("coolos"):
    print(":)")
    if socket.gethostname()+l == open(coolos).readline():
     return True
    else:
         os.system("/usr/local/bin/python3 hack")
   else:
         os.system("/usr/local/bin/python3 hack")



