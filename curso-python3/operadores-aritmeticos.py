numero_1 = 5
numero_2 = 2

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(soma) # 7
print(subtracao) # 3
print(multiplicacao)  # 10
print(divisao) # 2.5
print(divisao_inteira) # 2
print(modulo)  # 1
print(exponenciacao) # 25

# Operador de repetição:
print(100 * '#')

'''
Você olha para um relógio e são exatamente 2 da tarde. Você coloca um alarme para tocar daqui a 51 horas. A que horas o alarme ira tocar?
'''

# Resolução:
hora_inicial = 14
hora_final = hora_inicial + 51
print(f'O alarme tocará às {hora_final % 24} horas')

'''
Escreva um programa em Python que resolve a versão geral do problema acima. Peça ao usuário que entre com a hora atual (em horas) e que entre com o número de horas que deverá esperar antes do alarme tocar. Seu programa deve imprimir a hora que o alarme irá tocar.

'''

# Resolução:
hora_atual = int
horas_de_espera = int
input(f'Digite a hora atual ({hora_atual})')
input(f'Digite a quantidade de horas que deseja esperar até o alarme tocar ({hora_final})')
print(f'Seu alarme irá tocar às {hora_atual % hora_final} horas')
