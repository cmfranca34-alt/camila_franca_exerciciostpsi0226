#Altere o programa anterior para que mostre todas as tabuadas de 1 a 100. (ciclos for).

for numero in range(1, 101):

    print("\nTABUADA DO", numero)

    for i in range(1, 11):     #  4 espaços, está DENTRO do loop
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

