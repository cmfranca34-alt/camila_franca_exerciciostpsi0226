def contar_minusculas(palavra):
    contador = 0
    for c in palavra:
        if 'a' <= c <= 'z':
            contador += 1
    return contador


def ordenar_por_minusculas(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if contar_minusculas(lista[j]) > contar_minusculas(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


palavras = []
quantidade = int(input("Quantas palavras queres inserir? "))

for i in range(quantidade):
    palavras.append(input(f"Palavra {i+1}: "))

ordenar_por_minusculas(palavras)

print("Ordenadas por nº de minúsculas:", palavras)