import socket
from time import sleep
from os import system

def get_data(client_socket: socket.socket) -> str:
    return client_socket.recv(1024).decode()

def client_program(port):
    host = socket.gethostname()
    SOCKET = (host, port)

    loop = True
    while loop:
        
        client_socket = socket.socket()
        client_socket.connect(SOCKET)
        
        data = get_data(client_socket) # Get Menu
        print(data)

        message = input("-> ")
        if message == 'exit':
            system('clear')
            loop = False
        
        client_socket.send(message.encode())
        print('comando enviado!')
        sleep(2)
        system('clear')

        client_socket.close()

    exit()

if __name__ == '__main__':
    loop = True
    while loop:
        try:
            port = input('Qual porta?\n> ')
            system('clear')
            port = int(''.join([c for c in port if c.isnumeric()]))
            client_program(port=port)
            print(f'Conectado em {port}\n')
            loop = False
        except ConnectionRefusedError as cfe:
            print(f'Conexão mal sucedida em {port}')
            print(str(cfe))
        except KeyboardInterrupt:
            print('\nDesligando...')
            exit()