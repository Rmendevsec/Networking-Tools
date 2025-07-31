import socket

target = input("Target IP: ")
for port in range(20,1025):
    s = socket.socket()
    s.settimeout(0.5)
    if s.connect_ex((target, port)) == 0:
        print(f"Port {port} is Open")
    s.close()

