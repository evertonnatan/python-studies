'''
Operadores Lógicos 
and, or, not
in e not in
'''

# Exemplo da aula

usuario = input("Nome de usuário: ")
senha = input("Senha do Usuário: ")

usuario_bd = 'everton'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print("Usuário logado no sistema")
else:
    print("Usuário ou senha inválidos, tente novamente!")