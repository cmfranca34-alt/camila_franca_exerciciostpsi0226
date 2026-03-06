
#Enunciado:
 #Leia 10 números e determine quantos são pares e quantos são ímpares.
#Exemplo:
# Entrada: 2, 3, 5, 6, 8, 9, 10, 12, 14, 15
# Saída esperada:
#Pares: 6
#Ímpares: 4

pares = 0
impares = 0 # contadores que vao guardar os numeros

for i in range(10): # loop que repete 10x. o i ]e uma variavel que comeca em 0 e vai ate o 9
    num = int(input(f"Insira o número {i+1}: "))  # A cada repetição, pede um número ao usuário
    if num % 2 == 0:
        pares+= 1
    else:
        impares +=1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
