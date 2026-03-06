
#Enunciado:
#Desenvolva um programa que analise 3 valores inteiros e informe qual o maior e qual o menor deles.
#Exemplo:
#Entrada: num1 = 5, num2 = 2, num3 = 8
#Saída esperada:
#Maior: 8
#Menor: 2



num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

# Encontrar o maior
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

# Encontrar o menor
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print(f"Maior: {maior}")
print(f"Menor: {menor}")