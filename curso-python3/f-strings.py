'''
DESAFIO DA AULA DE F-STRINGS:

Criar variável com o ano atual (int)
Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibir um texto com todos os valores na tela usando F-Strings (com chaves)
'''

nome = 'Everton'
idade = 23
altura = 1.70
peso = 65
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')

nome1 = " Meu nome é Dennis Ritchie "
print(nome1.strip()) # O método strip() remove todos os espaços no começo e no fim da string
print(len(nome1))   # O método len() retorna o tamanho da string
print(nome1.lower()) # O método lower() retorna a string em lower case
print(nome1.upper()) # O método upper() retorna a string em upper case
print(nome1.replace("Dennis", "Alan")) # O método replace substitui a string com outra string
print(nome1.split(" ")) # O método split separa a string em substrings caso haja um separador, nesse caso utilizamos o espaço (" ") e ele nos retorna uma lista de strings