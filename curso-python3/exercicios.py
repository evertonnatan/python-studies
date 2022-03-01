"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro. 

"""


numero_inteiro = input('Digite um número inteiro: ')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print(f"{numero_inteiro} é par!")
    else:
        print(f"{numero_inteiro} é ímpar!")
else:
    print("Isso não é um número inteiro!")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.: Bom dia, Boa tarde, Boa noite!

"""
horario = input('Digite um horário (0-23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('O horário deve estar entre 0 e 23 horas')
    else:
        if horario < 11:
            print("Bom dia😄!")
        elif horario <= 17:
            print("Boa tarde😅!")
        else:
            print("Boa noite😴!")
else:
    print("Por favor, digite um horário entre 0 e 23 horas.")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 letras, escreva "Seu nome é muito grande".

"""

nome = input("Digite seu nome: ")
tamanho = len(nome)

if tamanho <= 4:
    print("Seu nome é curto!")
elif tamanho <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande!")