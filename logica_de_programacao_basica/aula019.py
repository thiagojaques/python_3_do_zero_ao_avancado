nome = 'Maria Carmo'
 
if ' ' in nome:
    print(f'O nome {nome} tem espaços.')
else:
    print(f'O nome {nome} NÃO tem espaços.')

numero = 10
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')