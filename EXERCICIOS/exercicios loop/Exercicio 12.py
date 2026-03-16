
#Elabore um programa que leia quantos números quer que se efetue a soma, subtrações, 
# divisões, multiplicações e no fim por meio de um acumulador diga quantas operações foram efetuadas. Exemplo 
# introduzindo o número 60 o programa deve apresentar 60 a somar, dividir multiplicar e subtrair por todos os números menores que ele.

numero = int(input("Digite um número: "))  # le o número digitado e converte para inteiro
acumulador = 0  # começa o contador zerado

print("\nSOMAS\n")  

for i in range(1, numero): # repete para cada número de 1 até (numero - 1)
    resultado = numero + i  # faz a soma e guarda o resultado
    print(numero, "+", i, "=", resultado)  # mostra a operação na tela
    acumulador = acumulador + 1  # adiciona 1 ao contador de operações


print("\nSUBTRAÇÕES\n")  

for i in range(1, numero):# repete para cada número de 1 até (numero - 1)
    resultado = numero - i    # faz a subtração e guarda o resultado
    print(numero, "-", i, "=", resultado)  # mostra a operação na tela
    acumulador = acumulador + 1  # adiciona 1 ao contador de operações

print("\nMULTIPLICAÇÕES\n")

for i in range(1, numero):  # repete para cada número de 1 até (numero - 1)
    resultado = numero * i    # faz a multiplicação e guarda o resultado
    print(numero, "*", i, "=", resultado)  # mostra a operação na tela
    acumulador = acumulador + 1  # adiciona 1 ao contador de operações


print("\nDIVISÕES\n")

for i in range(1, numero):  # repete para cada número de 1 até (numero - 1)
    resultado = numero / i    # faz a divisão e guarda o resultado
    print(numero, "/", i, "=", resultado)  # mostra a operação na tela
    acumulador = acumulador + 1  # adiciona 1 ao contador de operações