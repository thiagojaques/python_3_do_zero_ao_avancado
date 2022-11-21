# Lista é uma coleção ordenada e mutável.Permite membros duplicados.
# Lista sempre fica dentro de [ ]

#index:     0        1        2       3...
lista = ['tereré', 'água', 'limão', True, 2, 3.5]
print(lista)
print(type(lista))
print(lista[1]) #acessa o index de nº 1
print('-'*30)


# Tupla é uma coleção ordenada e imutável. Permite membros duplicados.
# Tuplas fica dentro de parênteses ( ).
# index:    0         1       2      3...
tupla = ('tereré', 'água', 'limão', True, 2, 3.5)
print(tupla)
print(type(tupla))
print(tupla[3]) #acessa o index de nº 3
print('-'*30)


# Dicionário é uma coleção ordenada e mutável. Nenhum membro duplicado.
#Dicionário ficam dentro de {} e sempre a chave vem acompanhada de um valor.

              #chave: valor  
dicionario = {'nome': 'tereré', 'nome': 'água', 'numero': 2, 'outroNumero': 5}
print(dicionario)
print(type(dicionario))
print(dicionario['numero']) #para acessar um valor de uma chave
print('-'*30)


# Set é uma coleção não ordenada e não indexada. Nenhum membro deplicado.

conjunto = {'tereré', 'água', 'limão', 2, 3.5}
print(conjunto)
print(type(conjunto))