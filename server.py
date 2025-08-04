import socket
import sys
import os

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)  # создаем объект сокета сервера
hostname = socket.gethostname()         # получаем имя хоста локальной машины
serv_sock.bind((hostname, 53210))       # привязываем сокет сервера к хосту и порту
serv_sock.listen(10)                    # начинаем прослушиваение входящих подключений
if sys.argv[1]: file_to_client = sys.argv[1]    # получаем файл для отправки клиенту

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()   # принимаем клиента
    print("serving", os.path.abspath(file_to_client))
    print('request from', client_addr)

    file = open(file_to_client, "rb")     # открываем файл для отправки
    print("sending data to client...")

    # считываем данные из файла блоками по 1024 байт и отправляем клиенту
    line = file.read(1024)
    while line:
        client_sock.send(line)      # отправляем строку клиенту 
        line = file.read(1024)
    
    print(f"finished sending to {client_addr}")

    file.close()            # закрываем файл
    client_sock.close()     # закрываем клиента