# https://www.w3schools.com/python/ref_func_len.asp


usuario = input ('Digite o seu usuário: ')

qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres!')
else:
    print('Você foi cadastrado no sistema')

# print(usuario, qtd_caracteres, type(qtd_caracteres))