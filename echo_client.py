import socket


HOST = '127.0.0.1'
PORT = 65432
SIZE_LIMIT = 1024
DECODE_FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

print(
    '\nКлиент подключен.\n'
    '\n[Для остановки клиента введите пустую строку]'
)

while True:
    string = str(input(
        '\n'
        'Введите строку, которую хотите преобразовать в верхний регистр (EN): '
    ))

    # Останавливает клиент, если введена пустая строка
    if not string:
        break

    server.sendall(string.encode())
    print('Отправлено ', string)

    response = server.recv(SIZE_LIMIT)
    if not response:
        break
    print('Получено   ', response.decode(DECODE_FORMAT))
