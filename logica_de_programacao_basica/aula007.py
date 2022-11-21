#Precedência dos operadores

# primeiro: tudo o que tiver dentro de parenteses (2+2(1+1)1) os mais internos são executado primeiro

# segundo: potências **
# 
# terceiro: multiplicação *, /, //, %
# 
# quarto: + -
# 

problema = 5 + (2 ** 2) + 2
print(problema)

problema2 = 5 + 2 ** (2 + 2)
print(problema2)

problema3 = 5 + 2 ** (2 + (2 + 2))
print(problema3)