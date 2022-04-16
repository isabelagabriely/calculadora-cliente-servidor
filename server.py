import socket
import json
import os

from colorama import Fore, Style

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

os.system('cls' if os.name == 'nt' else 'clear')
print(f'\n [{Fore.GREEN}✓{Style.RESET_ALL}] Servidor funcionando')

connection, (ip, port) = s.accept()
print(f'\n [{Fore.GREEN}✓{Style.RESET_ALL}] {Fore.GREEN}Conexão estabelecida{Style.RESET_ALL} | Endereço IP: [{ip}] : Porta [{port}]')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    return x / y


try:
    while True:
        request = connection.recv(1024)

        if len(request) < 1:
            break

        print(f'\n [{Fore.GREEN}✓{Style.RESET_ALL}] Request recebida do cliente')

        request = json.loads(request)
        operator = request['operator']
        value1 = request['value1']
        value2 = request['value2']

        if operator == 1:
            result = add(value1, value2)
            reply = f' → {value1} + {value2} = {result}'
            connection.send(reply.encode())
            
        elif operator == 2:
            result = subtract(value1, value2)
            reply = f' → {value1} - {value2} = {result}'
            connection.send(reply.encode())
        
        elif operator == 3:
            result = multiply(value1, value2)
            reply = f' → {value1} * {value2} = {result}'
            connection.send(reply.encode())

        elif operator == 4:
            result = devide(value1, value2)
            reply = f' → {value1} / {value2} = {result}'
            connection.send(reply.encode())

        print(f'\n [{Fore.GREEN}✓{Style.RESET_ALL}] Reply enviada para o cliente')
    
    connection.close()
    print(f'\n [{Fore.GREEN}✓{Style.RESET_ALL}] {Fore.RED}Conexão encerrada{Style.RESET_ALL}')
    input('\n Pressione enter para fechar')

except:
    s.close()
