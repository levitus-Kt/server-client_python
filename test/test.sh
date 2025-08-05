fallocate -l 10M ./file
python3 src/server.py ./file &
python3 src/client.py ./file
cmp -s file newfile && echo "Файлы совпадают"