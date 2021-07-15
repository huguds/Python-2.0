# Programador: Victor Hugo | algoritmo: Exercícios utilizando operadores e variáveis | data: 14/07/2021
# Utilizamos o input para ler a entrada de dados
# Nesta lista de exercicios contém um format que serve justamente para formatar a string e imprimir de acordo com o que usuário deseja


# 1 - O algoritmo terá que pedir para o usuário digitar dois números inteiros e soma-los.
print(5*"=","Exemplo 1",5*"=");
x = int(input("Digite o primeiro número: "));
y = int(input("Digite o segundo número: "));
print("O resultado da soma é: ",x+y);
print("\n");
# 2 - Faça um algoritmo que calcule a idade de acordo com o ano de nascimento e o ano atual.
print(5*"=","Exemplo 2",5*"=");
anoAtual = 2021;
anoNascimento = int(input("Digite o seu ano de nascimento: "));
print("A sua idade é: ",anoAtual-anoNascimento);
print("\n")
# 3 - Em uma loja de doces cada bala custa 20 centavos. Calcule quanto uma pessoa irá gastar se comprar 30 balas.
print(5*"=","Exemplo 3",5*"=");
precoBala = 0.20;
qtdBala = 30;
print("O valor total é de:",precoBala*qtdBala);
print("\n");
# 4 - Um cliente comprou 30 balas e gastou no total 6 reais. Calcule qual é o valor de cada bala.
print(5*"=","Exemplo 4",5*"=");
precoTotal = 6;
precoCadaBada = precoTotal/30;
print(f"O preço de cada bala é de: {precoTotal/30:.2f} reais");
print("\n");
# 5 - Faça um algoritmo que calcule a potência de um número
print(5*"=","Exemplo 5",5*"=");
numero = int(input("digite qual será o valor do número: "));
potencia = int(input("Digite qual será o valor da potência: "));
print(f"O resultado da potência {numero} elevado a {potencia} é de: {numero**potencia}");
print ("\n");
# 6 - Crie um algoritmo que calcule uma divisão retornando o resto
print(6*"=","Exemplo 6",5*"=");
dividendo = 135;
divisor = 2;
quociente = dividendo // divisor;
resto = dividendo % divisor;
print("Quociente: ",quociente);
print("Resto: ",resto);