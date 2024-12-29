import socket

HOST = '127.0.0.1'  # localhost
PORT = 65432

def run_server():
    # Створюємо сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))       # Прив'язуємося до хоста і порту
        s.listen(1)               # Сервер слухає (1 - максимальна кількість клієнтів в черзі)
        print(f"Сервер запущено на {HOST}:{PORT}")

        # Чекаємо клієнта
        conn, addr = s.accept()
        with conn:
            print(f"Підключився клієнт: {addr}")

            # Отримуємо дані від клієнта
            data = conn.recv(1024)
            if data:
                print("Отримано від клієнта:", data.decode('utf-8'))

            # Відправляємо відповідь
            message = "Привіт із сервера!"
            conn.sendall(message.encode('utf-8'))

if __name__ == "__main__":
    run_server()
