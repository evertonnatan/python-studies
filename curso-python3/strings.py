# Strings são um tipo de dados em Python
# "Tudo" em Python são objetos

# Escapando caracteres:

print("Esse é meu \"texto\" (str)")

# O "*" operador cria várias cópias de uma string. Exemplo:
'''
>>> s = 'foo.'

>>> s * 4
'foo.foo.foo.foo.'
>>> 4 * s
'foo.foo.foo.foo.'

# Caso o operando multiplicador seja um número negativo ou zero, o resultado será um String vazia, como no exemplo abaixo:
>>> 'foo' * -8
''


'''

'''
Strings com aspas podem conter apóstrofos, como em "O símbolo ' é um apóstrofo", e strings com apóstrofos podem conter aspas, como em 'Os cavaleiros que dizem "Ni!"'. Strings delimitados por três aspas ou apóstrofos são chamadas de strings triplos (triple quoted strings). Eles podem conter aspas, apóstrofos ou strings entre aspas ou apóstrofos:

https://panda.ime.usp.br/pensepy/static/pensepy/02-Conceitos/conceitos.html

'''
print('''"Oh nao", exclamou ela, "A bicleta esta quebrada!"''')