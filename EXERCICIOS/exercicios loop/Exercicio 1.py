
# Crie um algoritmo que mostre os 30 primeiros números ímpares e pares.

pares = []
impares = [] # lista para guardar os numeros

#loop de repeticao
for i in range (1, 61): 
    if i % 2 == 0: # condicional, e a % (modulo) retorna o resto da divisao. Nesse caso se restar 0 é par.
        pares.append(i) #vai adiconando os numeros pares na lista
    else:
        impares.append(i) # append é o metodo; vai adicionando os numeros impares na lista

print(f"Pares: {pares}")
print(f"[Ímpares: {impares}")


