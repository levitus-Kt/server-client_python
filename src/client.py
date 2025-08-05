import socket
import sys
import os
import _io

# Создаем сокет клиента
client_sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Получаем хост локальной машины
hostname: str = socket.gethostname()
# Устанавливаем порт сервера                                  
port: int = 53210     
# Подключаемся к серверу                                                   
client_sock.connect((hostname, port))
print("Connected")

# Получаем файл для запроса с сервера
if sys.argv[1]: file_from_server: str = os.path.basename(sys.argv[1])
# Отправляем данные серверу
client_sock.send(file_from_server.encode())

print(f"requesting from {hostname}:{port}")
print("downloading...")

# Создаем файл для записи
newfile: _io.TextIOWrapper = open("newfile", "w")

while True:
    # получаем данные от сервера
    data: bytes = client_sock.recv(1024)
    # декодируем данные и записываем в файл
    newfile.write(bytes.decode(data))
    # файл закончился
    if not data: break

newfile.close()  # Закрываем файл
client_sock.close()  # Закрываем подключение
print('downloaded as', os.path.abspath("newfile"))