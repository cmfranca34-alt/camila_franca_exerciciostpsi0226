frase = input("Introduz uma frase: ")

palavras = frase.split()#divide frase em palavras

contador = {}

for p in palavras:  #percorre palavras
    if p in contador:     
        contador[p] += 1 #incrementa
    else:
        contador[p] = 1   # cria nova entrada

print(contador)