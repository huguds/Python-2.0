# Programador: Victor Hugo | algoritmo: Operadores Lógicos e relacionais | data: 18/07/2021

#Operadores Relacionais
# a == b | igual a
# a != b | diferente de
# a > b  | maior que
# a < b  | menor que
# a >= b | maior ou igual a
# a <= b | menor ou igual a

#Operadores Lógicos
# OR | OU lógico
# AND | E lógico
# not | negação

# 1 - Exercicio utilizando operadores relacionais
print(5*"=","Exemplo 1",5*"=");
a = 10
b = 12
print (f'A é igual a B ? {a == b}')
print (f'A é diferente de B ? {a != b}')
print (f'A é maior que B ? {a > b}')
print (f'A é menor que B ? {a < b}')
print (f'A é maior ou igual a B ? {a >= b}')
print (f'A é menor ou igual a B ? {a <= b}')
print ('\n')
# 2 - Exercício utilizando operadores lógicos
# Dica - utilize operadores relacionais quando tiver duas ou mais expressões
boolean = True
print(5*"=","Exemplo 2",5*"=");
print (f'A é maior ou menor que B ? {a > b or a < b}') # Basta uma expressão ser verdadeira para ser TRUE
print (f'A é maior e menor que B ? {a > b and a < b}') # As duas expressões precisam ser verdadeira para ser TRUE
print (f'variável "boolean" é igual a: {boolean}')
print (f'Negação da variável "boolean": {not boolean}')
