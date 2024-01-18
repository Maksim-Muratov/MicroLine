import socket
import threading


HOST = '127.0.0.1'
PORT = 65432
SIZE_LIMIT = 1024
CONNECTIONS_LIMIT = 10

main_socket: socket.socket = None
stop_main_thread = False


def on_client_connected(client_socket: socket.socket, addres):
    """Принимает от клиента строку, переводит её в
    верхний регистр и отправляет обратно клиенту"""

    print('Клиент подключен: ', addres)
    while True:
        string = client_socket.recv(SIZE_LIMIT)
        if not string:
            break
        client_socket.sendall(string.upper())
    client_socket.close()
    print('Клиент отключен: ', addres)


def start_server():
    """Отвечает за работу сервера"""

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(CONNECTIONS_LIMIT)
    global main_socket
    main_socket = server
    print(
        f'\nСервер запущен по проту {PORT}'
        '\nОжидание подключений...\n'
        '\n[Для остановки сервера нажмите клавишу Enter]\n'
    )
    global stop_main_thread
    while True and not stop_main_thread:
        client_socket, addres = server.accept()
        threading.Thread(
            target=on_client_connected,
            args=(client_socket, addres)
        ).start()
    print('Сервер остановлен.')


def stop_server():
    """Отвечает за остановку сервера"""

    global stop_main_thread
    stop_main_thread = True
    # Фиктивное соединение, выполняемое для разблокировки
    # метода accept и более изящной остановки.
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((HOST, PORT))


main_thread = threading.Thread(target=start_server)
main_thread.start()

# Останавливает сервер при нажатии клавиши Enter
while True:
    input_data = input()
    if not input_data:
        break
print('Остановка сервера... ')
stop_server()
main_thread.join()
main_socket.close()
