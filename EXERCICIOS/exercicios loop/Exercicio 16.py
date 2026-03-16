#Elabore um programa que constitua a média de 30 números pares que sejam introduzidos.
#  Validando a entrada de números inteiros entre 1 e 50.

soma = 0  #vai acumulando a soma de todos os números
contador = 0   #conta quantos números pares válidos já foram inseridos

while contador < 30:   #repete até ter 30 números pares válidos

    numero = int(input("Digite um número par entre 1 e 50: "))  #lê o número

    if numero < 1 or numero > 50:  #verifica se está fora do intervalo permitido
        print("Número inválido! Digite entre 1 e 50")

    elif numero % 2 != 0:     #verifica se é ímpar (% é o resto da divisão)
        print("Número inválido! Digite apenas números PARES")

    else:        #se passou nas duas validações...
        soma = soma + numero    #adiciona o número à soma
        contador = contador + 1   #conta mais um número válido
        print("Número aceite! Faltam", 30 - contador, "números")

media = soma / 30      #calcula a média depois dos 30 números

print("Soma total:", soma)
print("Média dos 30 números:", media)