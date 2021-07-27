# Programador: Victor Hugo | algoritmo: Manipulações de strings | data: 18/07/2021

# Uma string sempre terá o seu tamanho que é a quantidade total de elementos 
# E o seu indice, vale lembrar que o indice é aonde podemos acessar um elemento específico da String
nome = 'EmEngArda'
sobrenome = 'silva'
frase = 'melhor refeição arroz e feijão'

# 1 - Imprima nome e sobrenome concatenados
print(5*"=","Exemplo 1",5*"=")
print(nome+' '+sobrenome)
print('\n')
# 2 - Retorne o tamanho de uma string
print(5*"=","Exemplo 2",5*"=")
print(len(nome))
print('\n')
# 3 - Retorne a quantidade de indices de uma String
# É calculado o número total de elementos menos 1 para obter o total de indices
print(5*"=","Exemplo 3",5*"=")
print(len(nome)-1)
print('\n')
# 4 - Imprima a primeira letra da string maiúscula
print(5*"=","Exemplo 4",5*"=")
print(nome.capitalize())
print('\n')
# 5 - Imprima quantas vezes a letra "a" aparece em nome
print(5*"=","Exemplo 5",5*"=")
print(nome.count('a'))
print('\n')
# 6 - Verifique se uma string começa com uma sequência de caracteres
print(5*"=","Exemplo 6",5*"=")
print(nome.startswith('emeng'))
print('\n')
# 7 - Verifique se uma string termina com uma sequência de caracteres
print(5*"=","Exemplo 7",5*"=")
print(nome.endswith('rda'))
print('\n')
# 8 - Verifique se a string possui algum elemento alfanúmerico (letra ou número)
print(5*"=","Exemplo 8",5*"=")
print(nome.isalnum())
print('\n')
# 9 - Verifique se uma string possui apenas conteúdo alfabético
print(5*"=","Exemplo 9",5*"=")
print(nome.isalpha())
print('\n')
# 10 - Verifique se todas as letras de uma string são minúsculas ou maiúsculas
print(5*"=","Exemplo 10",5*"=")
print(f'Todas as letras são minúsculas ? {nome.islower()}')
print(f'Todas as letras são maiúsculas ? {nome.isupper()}') 
print('\n')
# 11 - Retorna uma cópia da String com todas as letras maiúsculas e minúsculas
print(5*"=","Exemplo 11",5*"=")
print(f'Nome em maiúsculo: {nome.upper()}')
print(f'Nome em minúsculo: {nome.lower()}')
print('\n')
# 12 - Inverta o conteúdo da String (maiusculos ficam minusculos e assim por diante)
print(5*"=","Exemplo 12",5*"=")
print(f'Invertendo... {nome.swapcase()}')
print('\n')
# 13 - Converter para maiúsculo as primeiras letras de cada palavra
print(5*"=","Exemplo 13",5*"=")
print(f'Titulo: {frase.title()}')
print('\n')
# 14 - Transforme uma String em uma lista
print(5*"=","Exemplo 14",5*"=")
print(f'Lista: {frase.split()}')
print('\n')
# 15 - Substitua uma palavra na String
print(5*"=","Exemplo 15",5*"=")
print(frase.replace('feijão','macarrão'))
print('\n')
# 16 - Retorne o indice em que uma letra se encontra em uma determinada String
print(5*"=","Exemplo 16",5*"=")
print(f'A letra "r" se encontra no indice: {nome.find("r")}')
print(f'O indice 6 encontrado na variável nome é: {nome[6]} ')
print('\n')
# 17 - Ajuste o nome para ser impresso no centro
print(5*"=","Exemplo 17",5*"=")
print(nome.center(22))