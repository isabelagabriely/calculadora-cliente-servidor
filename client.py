import socket
import json
import os

from colorama import Fore, Style

HOST = 'localhost'
PORT = 5000

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((HOST, PORT))


try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('\n CALCULADORA')
        print('creator: Isabela')
        print('\n [1] Adição')
        print('\n [2] Subtração')
        print('\n [3] Multiplicação')
        print('\n [4] Divisão')
        print('\n [5] Sair')

        operator = -1
        while operator not in range(1, 6):
            operator = int(input('\n Digite o número de referência do operador escolhido [1][2][3][4] ou [5] para sair: '))

        if operator == 5:
            break
        
        value1 = float(input(' Digite o primeiro valor: '))
        value2 = float(input(' Digite o segundo valor: '))

        request = {
            'operator': operator,
            'value1': value1,
            'value2': value2
        }
        request = json.dumps(request).encode()

        connection.send(request)
        print(f'\n [{Fore.GREEN}✓{Style.RESET_ALL}] Request enviada para o servidor')

        reply = connection.recv(1024).decode()
        print(f'\n [{Fore.GREEN}✓{Style.RESET_ALL}] Reply recebida do servidor')
        print(f'{Fore.GREEN}{Style.BRIGHT}{reply}{Style.RESET_ALL}')

        input('\n Pressione enter ')

    connection.close()
    input('\n Pressione enter para fechar')

except:
    connection.close()
