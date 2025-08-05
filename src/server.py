import socket
import sys
import os
import _io

# Создаем объект сокета сервера
serv_sock: socket.socket = socket.socket(
    socket.AF_INET, 
    socket.SOCK_DGRAM)
# Получаем имя хоста локальной машины
hostname: str = socket.gethostname()
# Устанавливаем порт сервера
port: int = 53210
# Привязываем сокет сервера к хосту и порту
serv_sock.bind((hostname, port))
# Получаем файл для отправки клиенту
if sys.argv[1]: file_to_client = sys.argv[1]

# Получаем данные от клиента
client_sock, client_addr = serv_sock.recvfrom(1024)

print("serving", os.path.abspath(file_to_client))
print('request from', client_addr[0] + ":" + str(client_addr[1]))

# Открываем файл для отправки
file: _io.BufferedReader = open(file_to_client, "rb")     
print("sending data to client...")

# Считываем данные из файла блоками по 1024 байт и отправляем клиенту
line: bytes = file.read(1024)
while line:
    serv_sock.sendto(line, client_addr) # отправляем строку клиенту
    line = file.read(1024)

print(f"finished sending to", client_addr[0] + ":" + str(client_addr[1]))

file.close()         # закрываем файл
serv_sock.close()    # закрываем сервер