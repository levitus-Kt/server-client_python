import socket
import sys
import os

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # создаем сокет клиента
hostname = socket.gethostname()                                     # получаем хост локальной машины
port = 53210                                                        # устанавливаем порт сервера
client_sock.connect((hostname, port))                   # подключаемся к серверу
print("Connected")
if sys.argv[1]: file_from_server = sys.argv[1]                      # получаем файл для запроса с сервера
file_from_server = os.path.basename(file_from_server)               # получаем название файла, если был указан путь
client_sock.send(file_from_server.encode())       # отправляем данные серверу
print(f"requesting from {hostname}:{port}")
print("downloading...")
newfile = open("newfile", "w")

while True:
    data = client_sock.recv(1024)    # получаем данные от сервера
    newfile.write(bytes.decode(data))   # декодируем данные и записываем в файл
    if not data: break              # файл закончился

newfile.close()
client_sock.close()                     # закрываем подключение
print('downloaded as', os.path.abspath("newfile"))