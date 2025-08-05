import socket
import sys
import os
import _io

# Создаем сокет клиента
client_sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Получаем хост локальной машины
hostname: str = socket.gethostname()
# Устанавливаем порт сервера                                  
port: int = 53210     
# Подключаемся к серверу                                                   
serv_addr: tuple = (hostname, port)

# Получаем файл для запроса с сервера
if sys.argv[1]: file_from_server: str = os.path.basename(sys.argv[1])
# Отправляем данные серверу
data: bytes = file_from_server.encode()
client_sock.sendto(data, serv_addr)

print(f"requesting from {hostname}:{port}")
print("downloading...")

# Создаем файл для записи
newfile: _io.TextIOWrapper = open("newfile", "w")

while True:
    # получаем данные от сервера
    data, addr = client_sock.recvfrom(1024)
    # декодируем данные и записываем в файл
    newfile.write(bytes.decode(data))
    # файл закончился
    message = input('Please type a word ')
    if message == 'stop' or message == '':
        newfile.close()  # Закрываем файл
        client_sock.close()
        break


client_sock.close()  # Закрываем подключение
print('downloaded as', os.path.abspath("newfile"))