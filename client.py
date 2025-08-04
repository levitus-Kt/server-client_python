import socket
import sys
import os

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # создаем сокет клиента
client_sock.connect((socket.gethostname(), 53210))                  # получаем хост локальной машины и подключаемся к серверу
print("Connected")
if sys.argv[1]: file_from_server = sys.argv[1]                      # получаем файл для запроса с сервера
file_from_server = os.path.basename(file_from_server)               # получаем название файла, если был указан путь
print("receiving data from server")

while True:
    data = client_sock.recv(1024)    # получаем данные от сервера
    print(bytes.decode(data))
    if not data: break

# client_sock.send(message.encode())       # отправляем данные серверу
client_sock.close()                     # закрываем подключение
print('Received', data.decode())