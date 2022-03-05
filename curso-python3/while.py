"""
While em Python - Aula 07 => https://youtu.be/bkSePLdPiDk

While é utilizado para realizar(repetir) ações enquanto uma condição for verdadeira.

Requisitos: entender condições e operadores.

"""

from traceback import print_tb

"""
while True: # loop infinito
    nome = input("Qual é o seu nome? ")
    print(f'Olá {nome}! ')

print("Não será executada")

"""

"""
# imprime na tela a sequência de 0 - 99
x = 0
while x < 100:
    print(x)
    x = x + 1

"""

# criando uma calculadora
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número!')
        continue

        num_1 = int(num_1)
        num_2 = int(num_2)

    # Operadores: + - / * 
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido')