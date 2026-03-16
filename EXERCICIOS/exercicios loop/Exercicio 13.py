
#Elabore um programa que leia um número e mostre a tabuada. (multiplicar de 1 a 10)

numero = int(input("Digite um número: "))  # lê o número e converte para inteiro

print("\nTABUADA DO", numero)

for i in range(1, 11):     # repete de 1 até 10
    resultado = numero * i   # multiplica o número por i
    print(numero, "x", i, "=", resultado)  # mostra a operação na tela

