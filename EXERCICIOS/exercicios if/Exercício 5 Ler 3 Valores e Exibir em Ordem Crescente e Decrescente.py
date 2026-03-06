
# Enunciado:
#Ler 3 valores inteiros e apresentar os valores dispostos em ordem crescente e decrescente.
#Exemplo:
#Entrada: num1 = 4, num2 = 9, num3 = 2
#Saída esperada:
#Crescente: 2, 4, 9
#Decrescente: 9, 4, 2

num1 = int(input ("Insira o primeiro número :"))
num2 = int(input("insira o segundo número :"))
num3 = int(input("insira o terceiro número :"))

if num1 > num2  and num1 > num3 and num2 > num3:
    print (f"Crescente {num3} , {num2}, {num1} ")
    print (f"Decrescente {num1} , {num2}, {num3} ")
    

else:
  print (f"Decrescente {num3} , {num2}, {num1} ")
  print (f"Crescente {num1} , {num2}, {num3} ")
   



