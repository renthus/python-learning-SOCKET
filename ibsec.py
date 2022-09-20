
#############
#***CLIENT***
#############

#versão inicial
import socket

ip="192.168.15.6"
port=8081
c = socket.socket()
print("conectando no servidor")
#conectar no IP e porta destino
c.connect((ip,port))
c.close()

#versão final
import socket
import time

# IP e porta destino
ip="192.168.15.6"
port=8081
c = socket.socket()
print("conectando no servidor")
#abrindo conexao
c.connect((ip,port))
#recebendo resposta
resposta = c.recv(2048).decode()
print(resposta)
c.close()


#############
#***SERVER***
#############

#versão inicial
import socket

c = socket.socket()
#escutar na porta 8081
c.bind(('0.0.0.0',8081))
c.listen(50)
print("Servidor iniciado aguardando conexao")
c, addr = c.accept()
print('[+] Recebeu conexao de:', addr)

#versão final
import socket
import random

#abre conexao
c = socket.socket()
c.bind(('0.0.0.0',8081))
c.listen(50)
print("Servidor iniciado aguardando conexao")
c, addr = c.accept()
print('[+] Recebeu conexao de:', addr)

#escolhe a fruta
lines=open("lista.txt").read().splitlines()
fruta = random.choice(lines)
informacao=fruta

#envia resposta
c.send(str(informacao).encode())
print("mensagem enviada, fechando conexao")
c.close()