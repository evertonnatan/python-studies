'''
Condições IF, ELIF e ELSE 

A sintaxe de um comando if se parece com:

    if EXPRESSÃO BOOLEANA:
        COMANDOS_1        # executados se condição tem valor True
    else:
        COMANDOS_2        # executados se condição tem valor False

Não há limite no número de comandos que podem aparecer nos dois blocos de um comando if, mas tem que haver pelo menos um comando em cada bloco. Cada bloco de else precisa ter exatamente um bloco de if correspondente. Se você quer encadear comandos if-else juntos, você precisa usar a construção de blocos aninhados. 
'''

if False:
    print("Verdadeiro.")
elif False:
    print("Agora é verdadeiro")
elif True:
    print("Mais uma verdadeira")
else:
    print("Não é verdadeiro")
