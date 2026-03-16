
#Elabore um programa que determine os múltiplos de 5 mas não múltiplos de 3 …. De 1 a 1000 deve ser a sequência.

for numero in range(1, 1001):   # percorre todos os números de 1 a 1000

    if numero % 5 == 0 and numero % 3 != 0:   # se é múltiplo de 5 E não é múltiplo de 3
        print(numero)                 