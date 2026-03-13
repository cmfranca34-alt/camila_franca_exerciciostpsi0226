
#Ler 10 números, e determinar se o número par e número impar.


#loop de repeticao
for i in range (10): # vai repetir 10x para o utilizador colocar um numero
   num = int(input("Digite um número: ")) 
   if num % 2 == 0: #caso o numero for par
        print(f"{num} é par")
   else:
    print(f"{num} é ímpar")
        

