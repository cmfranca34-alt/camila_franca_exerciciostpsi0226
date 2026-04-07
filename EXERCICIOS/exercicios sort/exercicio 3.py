def ordenar_caracteres(palavra):
    lista = list(palavra)  #divide em caracteres
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if ord(lista[j]) > ord(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return "".join(lista)


palavra = input("Insere uma palavra: ")
resultado = ordenar_caracteres(palavra)

print("Palavra ordenada:", resultado)