# Programador: Victor Hugo | algoritmo: Estrutura condicional if/else | elif | data: 29/07/2021

# 1 - Uma escola avalia seus alunos com duas provas anuais.
# Onde é necessário uma media 7 para ser aprovado.Faça um algoritmo que calcule a média de um aluno
print(5*"=","Exemplo 1",5*"=")
prova1 = 5; prova2 = 10; media = (prova1+prova2)/2;
if (media >= 7): # Entre os parenteses é definido a condição
    print('Aluno aprovado :)') # Se a condição for verdadeira ira retornar este resultado
else:
    print('Aluno reprovado :(') # Se a condição for falsa irá retornar este outro resultado
print('\n')
# 2 - Você está em uma loja de sapatos, selecione a marca do tênis que deseja comprar
print(5*"=","Exemplo 2",5*"=")
opc = int(input('1-Adidas\n2-Nike\n3-Mizuno\n4-Oakley\nSua opção: '))
EstoqAdidas = True; EstoqNike = True; EstoqMizuno = True; EstoqPuma = False;
if (opc == 1):
    print('\n')
    print('Adidas')
    if(EstoqAdidas == True):
        print('Estoque !')
    else:
        print('Sem estoque !')
elif(opc == 2): # O elif tem a mesma função de um else if
    print('\n')
    print('Nike')
    if(EstoqNike == True):
        print('Estoque !')
    else:
        print('Sem estoque !')
elif(opc == 3):
    print('\n')
    print('Mizuno')
    if(EstoqMizuno == True):
        print('Estoque !')
    else:
        print('Sem estoque !')
elif(opc == 4):
    print('\n')
    print('Puma')
    if(EstoqPuma == True):
        print('Estoque !')
    else:
        print('Sem estoque !')
# 3 - Faça um algoritmo que receba um número e verifica se ele é par ou ímpar utilizando somente
# uma linha de comando
x = 0
print(5*"=","Exemplo 3",5*"=")
print("Par" if x % 2 == 0 else "Impar") # É possivel utilizar uma expressão condicional no python
print(x % 2 == 0 and "Par" or "Impar") # O mesmo é utilizado para o boolean 