
#Escreva um programa que solicite um número ao utilizador até que o valor deste esteja entre os valores 1 e 100.
 #(Use o ciclo do ... while)

while True:  # loop infinito, fica repetindo até o break mandar parar
    
    num = int(input("Digite um número entre 1 e 100: "))  # pede o número ao utilizador
    
    if 1 <= num <= 100:  # verifica se o número está entre 1 e 100
        break  # número válido sai do loop

print(f"Número válido: {num}")  # só chega aqui quando o número for válido