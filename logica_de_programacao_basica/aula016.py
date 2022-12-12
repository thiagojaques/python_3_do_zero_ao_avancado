# Operadores lógicos
# and (e) or (ou) not (não)
# and só será executado se todas as condições for TRUE
# Se qualquer valor for considerado falso a expressão inteira será avaliada naquele valor.
# São considerados falsy 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor ou  nenhum valor

entrada = input('Quer Entrar?: sim ou não ')
senha = input('Senha: ')
senha_permitida = '123456'
if entrada == 'sim' or 'entrar' and senha == senha_permitida:
    print('Acesso Permitido')

else:
    print('Acesso negado')


senha = input('Senha: ') or 'Sem senha'
