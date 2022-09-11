#MODULO 6 - TRABALHANDO COM REDES E SOCKETS

#AULA 1 - SOCKET E CLIENT TCP

#cliente tcp
#se conecta ao servidor tcp

import socket

#FAMÍLIA IPV4 = socket.AF_INET
#TIPO TCP = socket.SOCK_STRAM // TIPO UDP = socket.SOCK_DGRAM
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

try:
    #conexão
    client.connect(('google.com', 80))

    #enviar dados para a conexão
    # client.send(b"olá tudo bem?")
    client.send("GET / HTTP/1.1\nHost: www.google.com\n\n\n".encode())
    pacotes_recebidos = client.recv(1024).decode()
    print(pacotes_recebidos)
except:
    print("Um erro ocorreu!!!")
###########----------##########

#AULA 2 - CLIENT UDP

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        msg = input("Mensagem: ") + "\n"
        client.sendto(msg.encode(), ("127.0.0.1", 4433))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ": " + data.decode())
        if data.decode() == "sair\n" or msg == "sair\n":
            break
    client.close()
except Exception as error:
    print("Erro de conexao")
    print(error)
    client.close()
###########----------##########