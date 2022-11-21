# criando aplicação que mostra seu nome e o IMC

nome = (input('Qual o seu nome?: '))

altura = float((input('E sua altura?: ')))

peso = float(input('Digite seu peso?: '))

imc = peso / (altura ** altura)

print('Seu IMC {} é {:.2f}'.format(nome,imc))