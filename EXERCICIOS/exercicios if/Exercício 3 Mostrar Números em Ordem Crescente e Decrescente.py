#Crie 2 variáveis (num1 e num2) e leia o valor para cada uma delas. Mostre os valores de forma crescente e decrescente.
#Exemplo:
#Entrada: num1 = 7, num2 = 2
#Saída esperada:
#Crescente: 2, 7
#Decrescente: 7, 2


num1 = int(input("Insira o primeiro número:"))
num2 = int(input("Insira o segundo número: "))

if num1 > num2  :
    print (f"Decrescente {num1} , {num2}")
    print (f"Crescente {num2} , {num1}")

else:
    print (f"Crescente {num1} , {num2}")
    print (f"Decrescente {num2} , {num1}")
    