"""
Formatando valores com modificadores - Aula 05: https://youtu.be/L4jNzQYD-zQ



:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (Número) f - Quantidade de casas decimais (float)
:(Caracteres) (> ou < ^)(Quantidade (Tipo - s, d ou f)

> - Esquerda
< - Direita 
^ - Centro

"""

num_1 = 10
num_2 = 3
num_3 = 1155
divisao = num_1 / num_2

print(f'{divisao:.2f}')

print(f'{num_3:0<10}') # < - Direita
print(f'{num_3:0>10}') # > - Esquerda
print(f'{num_3:0^10}') # ^ - Centro

nome = "Everton"
sobrenome = "Natã"

nome_formatado = '{0:$^10} {1:#^10}'.format(nome, sobrenome)
print(nome_formatado)