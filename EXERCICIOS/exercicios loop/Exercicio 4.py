
#Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não.

num = int(input("Digite um número: ")) 

primo = True # comeca o jogo asumindo que é primo ou seja bandeira verde

#só que quando chega aqui, vai ver se segue a bandeira verde ou nao:

for i in range (2, num): # vai testar o numero aleatorio a partir do 2 até ele mesmo.
   
   if num % i == 0:  # algum testador divide por ele alem dele proprio 
        primo = False # entao marca que nao é primo


if primo:
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")        