# Váriaveis são usadas para salvar algo na memória do computador.

# PEP8: inicie variáveis com letras minúsculas, pode usar: números e underline_ .

# O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome(variável).

# Uso: nome_variavel = expressão

#nome_completo = input('Digite seu nome completo: ')
#print(nome_completo)

#nome = str(input('Digite seu nome completo: '))

#idade = int(input('Qual a sua idade: '))
#print(idade())

nome = str(input('Qual o seu nome?: '))
idade = int(input('Qual a sua idade?: '))
ano_nascimento = input('Qual o ano do seu nascimento?: ')
maior_de_idade = input('Você é maior de idade?: ')
altura = input('E qual a sua altura?: ')

print('{} tem a idade de {}, nasceu em {} é maior de idade {} e tem a altura de {} metros.'.format(nome,idade,ano_nascimento,maior_de_idade,altura))
