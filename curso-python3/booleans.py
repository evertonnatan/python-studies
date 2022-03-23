'''
O tipo em Python para armazenar os valores verdadeiro e falso é chamado de bool, em homenagem ao matemático britânico George Boole. George Boole criou a Álgebra Booleana, que é a base de toda a aritmética computacional moderna.

Existem apenas dois valores booleanos. Eles são True e False. As iniciais maiúsculas são importantes, uma vez que true e false não são valores booleanos (lembre-se de que maiúsculas e minúsculas fazem diferença para o Python).

'''
print(True)
print(False)
print(type(True))
print(type(False))

# OPERADORES DE COMPARAÇÃO
'''
x != y               # x não é igual a y
x > y                # x é maior do que y
x < y                # x é menor do que y
x >= y               # x é maior ou igual a y
x <= y               # x é menor ou igual a y

Embora essas operações sejam provavelmente familiares a você, os símbolos em Python são diferentes dos símbolos matemáticos. Um erro comum é usar somente um símbolo de igual (=) em vez de dois sinais iguais (==). Lembre-se de que = é um operador de atribuição e o == é um operador de comparação. Também, os operadores =< ou => não existem.

Note também que um teste de igualdade é simétrico, mas atribuição não é. Por exemplo, se a == 7 então 7 == a. Mas, em Python, a expressão a = 7 é válida e 7 = a não é.
'''