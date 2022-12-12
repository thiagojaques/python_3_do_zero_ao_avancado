# Operadores in e not in
# Strings são iteráveis


nome = 'Thiago'
print(nome[2])
print(15 * '-')
print(type(nome))
print(15 * '-')
print('iago' in nome)
print(15*'-')
print('e' not in nome)


msg = input('Digite uma mensagem: ')
encontrar = input('Qual palavra ou letra deseja encontrar na mensagem?: ')

if encontrar in msg:
    print(f'{encontrar} está na sua mensagem.')

else:
    print(f'{encontrar} não enstá na sua mensagem.')