# https://www.delftstack.com/pt/howto/python/python-pass/

'''
A instrução pass é usada em Python quando algum código é solicitado sintaticamente, mas o usuário não deseja que o programa faça nada. 
Pode haver diferentes razões por trás disso; pode ser que o usuário planeje adicionar o código posteriormente ou pode ser usado para ignorar 
algumas exceções levantadas durante o tempo de execução.

O código de exemplo a seguir demonstra como usar a instrução pass no caso em que o usuário deseja adicionar o código mais tarde:

def myfunc(x):

    if x > 0:
        print('Input is greater than zero')
    else:
        #add code here
        pass
Se a instrução pass não foi adicionada no exemplo de código acima, o compilador teria retornado SyntaxError ou IdentationError.

Também podemos usar a instrução pass para ignorar uma exceção em Python, conforme demonstrado no código de exemplo fornecido abaixo:

def divide(x, y):
    z = None
    try:
        z = x/y
    except:
        pass
    return z

divide(6,0)
No código de exemplo acima, usamos a instrução pass junto com as instruções try e except para lidar com o ZeroDivisionError e evitar que o código trave.

'''

# EXEMPLO DADO PELO PROFESSOR LUIZ OTÁVIO NA AULA 27:
valor = True

if valor:
    pass
else:
    print('Thau!')

# Também é possível utilizar elipses (três pontinhos - ...)
aprovado = True

if aprovado:
    ...
else: 
    print("Reprovado")