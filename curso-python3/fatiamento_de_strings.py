"""
Manipulando strings - Aula 06: https://youtu.be/QxjArQ9xZDg
* Strings indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Voce pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)


"""
# Positivos [0123456789]

from cgitb import text


texto = 'Python s2'
print(texto[8])

# Negativos -[987654321]
print(texto[-8])
print(texto[2:6])
print(texto[:6])
print(texto[7:])
print(texto[-1])
print(texto[0::2]) # pulando de 2 em 2



