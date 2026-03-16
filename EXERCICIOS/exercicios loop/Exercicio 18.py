#Elabore um programa que leia uma entrada e diga quantos números perfeitos existem. 
# Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial. 6=3+2+1 .


inicial = int(input("Digite um número "))  #lê o limite

contador = 0  #conta quantos números perfeitos foram encontrados

print("NÚMEROS PERFEITOS")

for numero in range(1, inicial + 1):    # percorre todos os números de 1 até o limite

    soma_divisores = 0                 # zera a soma dos divisores para cada número

    for divisor in range(1, numero):   # percorre todos os números menores que o número
        if numero % divisor == 0:      # se o resto é zero, é divisor
            soma_divisores = soma_divisores + divisor  # acumula o divisor na soma

    if soma_divisores == numero:       # se a soma dos divisores é igual ao número
        print(numero, "é perfeito! Divisores: ")  
        for divisor in range(1, numero):   # percorre de novo para mostrar os divisores
            if numero % divisor == 0:
                print(divisor, end=" ")    # mostra o divisor na mesma linha

        print("")          # pula linha depois de mostrar os divisores
        contador = contador + 1  #conta mais um número perfeito