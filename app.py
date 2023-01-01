from server import Server
from os import system
from time import sleep
from datetime import datetime


app = Server()


@app.register_action
def ola_mundo(ola, mundo='terra'):
    print(f'{ola} {mundo}!')
    
@app.register_action
def cumprimento(nome):
    if 5 <= datetime.now().hour < 12:
        cumpr = 'Bom dia'
    elif 12 <= datetime.now().hour < 18:
        cumpr = 'Boa tarde'
    else:
        cumpr = 'Boa Noite'
    print(f'{cumpr}, {nome}!')
    
@app.register_action
def enviar_email():
    print('enviando o email...')
    sleep(2)
    print('enviei o email!')
    
@app.register_action
def clear():
    system('clear')
    
@app.register_action
def backup():
    print('fazendo o backup...')
    sleep(2)
    print('fiz o backup!')

if __name__ == "__main__":
    port = input('Qual porta?\n> ')
    app.listen(port)
