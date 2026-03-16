
#Elabore um programa que lê um número e escreve quantos divisores ele possui.

num = int(input("Digite um número: "))  # pede um número ao utilizador

contar = 0  # começa com 0 divisores, igual ao soma = 0 da média

# range(inicio, fim +1)
for i in range(1, num + 1):  # testa todos os números de 1 até o próprio num
    if num % i == 0:  # se dividir sem sobra, é divisor!
        contar = contar + 1  # conta mais um divisor

print(f"O número {num} tem {contar} divisores")  # mostra o resultado 