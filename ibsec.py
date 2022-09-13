# cliente

import socket

ip = "192.168.15.10"
porta = 8082

c = socket.socket()
print("Se conectando ao servidor")
c.connect((ip, porta))

x = input("Digite algo")
c.close()