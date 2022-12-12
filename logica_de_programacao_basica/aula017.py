# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')
if senha == '123456':
    print('Acesso Permitido')

if not senha:
    print('Campo obrigatório')

if senha != '123456':
    print('Senha inválida')