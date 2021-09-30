'''
Entrada de dados

* A função "input" sempre retorna uma String
'''

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

ano_nascimento = 2021 - int(idade)

print()
print(f'{nome} tem {idade} anos. ' f'{nome} nasceu em {ano_nascimento}. ')


# Exemplo da calculadora com input:

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

print(numero1 ** numero2)