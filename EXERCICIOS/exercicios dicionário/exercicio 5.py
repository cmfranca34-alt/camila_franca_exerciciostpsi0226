palavra = input("Introduz uma palavra: ")

contador = {}  # dicionário para contagem

for letra in palavra:  # percorre cada letra
    if letra in contador:  #se já existe
        contador[letra] += 1  #incrementa
    else:
        contador[letra] = 1   #cria com valor 1

print(contador)