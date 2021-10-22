# Programador: Victor Hugo | algoritmo: Estrutura de Repetição for | data: 05/08/2021
# O laço de repetição for precisa de uma váriavel de inicio e uma distância para ser percorrida.
# Sendo utilizado para percorrer listas, dicionários e strings
# 1 - Faça um algoritmo que conte de 0 até 10
print(5*"=","Exemplo 1",5*"=")
num = 0; x = 1; i = 0; soma_dos_numeros = 0; z = 0; maiorNome = 0;
for x in range(10):
    print(x, end=" ")  # end é utilizado para imprimir os valores na mesma linha
print('\n')
# 2 - Faça um algoritmo que mostre todos os nomes de um lista
print(5*"=","Exemplo 2",5*"=")
nomes = ['Asdrubal','Welisson','Emengarda','Vladilson']
for x in nomes:
    print(x)
print('\n')
# 3 - Faça um algoritmo que transforme todos elementos de uma lista em maiusculo
print(5*"=","Exemplo 3",5*"=")
for x in nomes:
    print(x.upper())
print('\n')
# 4 - Faça um algoritmo que mostre a quantidade de indices e elementos de uma lista
print(5*"=","Exemplo 4",5*"=")
for x in nomes:
    i+=1
qtdElements = i
qtdIndices = i-1
print(f"O número de elementos é de: {qtdElements}")
print(f"O número de indices é de: {qtdIndices}")
print('\n')
# 5 - Faça um algoritmo que calcule a soma e a média de uma lista
print(5*"=","Exemplo 5",5*"=")
numeros = [5,5,5,5,5,5,5,5]
for x in numeros:
    z += 1
    soma_dos_numeros += x
print(f'A soma dos números é de: {soma_dos_numeros}')
print(f'A média dos números é de: {soma_dos_numeros/z}')
print('\n')
# 6 - Crie um algoritmo que enumere a quantidade de números
print(5*"=","Exemplo 6",5*"=")
for num, x in enumerate(numeros):
    num+=1
    print (f"{num} : {x}")
print('\n')