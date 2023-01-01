from time import sleep
from os import system
from typing import Optional
from socket import socket, gethostname
import inspect

class Server:
    def __init__(self):
        self.host = gethostname()
        self.actions = []
        
    def listen(self, port: str):
        port = int(''.join([c for c in port if c.isnumeric()]))
        self.SOCKET = (self.host, port)
        
        server_socket = socket()
        server_socket.bind(self.SOCKET)
        
        while True:
            try:
                server_socket.listen(2)
                print(f'\nEscutando em: {self.SOCKET}...')
                
                connection, address = server_socket.accept()
                
                if (connection, address):
                    self.main(connection, address)
                
            except KeyboardInterrupt:
                try:
                    connection.close()
                except UnboundLocalError:
                    exit()
                
            except IndexError:
                connection.close()
                exit()
                
            except UnboundLocalError:
                exit()
                
    def register_action(self, action: callable):
        arg_spec = inspect.getargspec(action)
        context = {'action': action, 'name': action.__name__, 'args': arg_spec[0]}
        self.actions.append(context)

    def get_action(self, name: str) -> callable:
        for context in self.actions:
            if context['name'] == name:
                return context['action']

    def execute_action(self, action: Optional[callable], args: list, kwargs: dict):
        print('Executando...\n\n')
        if action:
            try:
                action(*args, **kwargs)
            except TypeError as e:
                print('Ação utilizada incorretamente!')
                print(str(e))
        else:
            print('Nenhum comando encontrado')
        
    def main(self, connection: socket, address: tuple):
        print(f"Conexão de: {address[0]}/{address[1]}")
        
        menu = self.get_menu()
        connection.send(menu.encode())
        
        data_received = self.get_data(connection)
        
        action_name = self.get_action_name(data_received)
        args = self.get_args(data_received)
        kwargs = self.get_kwargs(data_received)
        
        if action_name == 'exit':
            connection.close()
            system('clear')
            exit()
            
        action = self.get_action(action_name)
        
        self.execute_action(action, args, kwargs)
        sleep(0.01)
        
    def get_menu(self) -> str:
        string = 'Menu:\n'
        for context in self.actions:
            
            args = ''
            for arg in context['args']:
                args += f'{arg}, '
            args = args[:-2]
            
            string += f'> action: {context["name"]}'
            if args:
                string += f' | args: {args}'
            string += '\n'
        
        return string

    def get_data(self, connection) -> str:
        data_received = connection.recv(1024).decode()
        print("\nDo usuario conectado: " + str(data_received))
        return data_received
    
    def get_action_name(self, data_received: str) -> str:
        return data_received.split()[0]
    
    def get_args(self, data_received: str) -> list:
        parts = data_received.split()
        items = [
            part for part in parts
            if part.startswith('-') and not part.startswith('--')
        ]
        args = [item[1:] for item in items]
        return args
        
    def get_kwargs(self, data_received: str) -> dict:
        kw = {}
        parts = data_received.split()
        kw_list = [
            part for part in parts
            if part.startswith('--')
        ]
        for item in kw_list:
            item = item.replace('--', '')
            key, value = item.split('=')
            kw[key] = value
            
        return kw
