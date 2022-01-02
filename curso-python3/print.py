# Este é um comentário
print('Hello, World')  #Este também é um comentário (PEP 8 fala que se deve adicionar 2 espaços, após o último caractere, em um comentário de linha )

# Comentário de múltiplas linhas em Python (usa-se 3 aspas (simples ou dulpas), antes e 3 depois)
"""
print("linha 01")
print("linha 02")
print("linha 03")
"""

print("linha 04")
print("linha 05")
print("linha 06")
print("linha 07")

# print com vários paramêtros, separados por espaços:
print("Everton", "Natan")

# print com vários paramêtros, separados por separador:
print("Everton", "Natan", sep="-")

# print com vários paramêtros, separados por separador com o paramêtrp end ao final:
print("Everton", "Natan", sep="-", end=" CPF nº")

# Exercício de fixação:
# Fazendo com que a função print mostre uma sequência de número no formato de um CPF:
print('824', '189', '073', sep=".", end='-')
print('18')