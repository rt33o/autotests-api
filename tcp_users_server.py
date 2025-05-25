import socket
import threading

# Храним историю сообщений
messages = []

# Обработка клиента
def handle_client(client_socket, client_address):
    print(f"Пользователь с адресом: {client_address} подключился к серверу")

    try:
        data = client_socket.recv(1024).decode().strip()
        if data:
            print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
            messages.append(data)
            history = '\n'.join(messages)
            client_socket.send(history.encode())
    except Exception as e:
        print(f"Ошибка при обработке клиента {client_address}: {e}")
    finally:
        client_socket.close()

# Настройка сервера
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(10)
    print("Сервер запущен на 127.0.0.1:12345")

    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    start_server()
