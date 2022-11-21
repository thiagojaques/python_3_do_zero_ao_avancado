# if / elif .../ else
# se / se não se / se não

#cond = False

#if cond == True:
    #print('esse codigo funcionou')
#else:
    #print('esse codigo é falço')

nome_de_usuario = str(input('Digite seu nome: '))
idade = int(input('Qual a sua idade: '))

if idade >= 18:
    print('Olá {}, você tem {} anos --Acesso permitido--'.format(nome_de_usuario,idade))

elif idade <= 17:
    print('{} é menor de idade --Acesso negado--'.format(nome_de_usuario))

else:
    print('Digite algo válido')