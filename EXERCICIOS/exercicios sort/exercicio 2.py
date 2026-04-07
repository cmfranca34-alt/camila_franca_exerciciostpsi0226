# Compara duas palavras ignorando maiúsculas/minúsculas
def comparar_palavras_inverso(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()

    tamanho_minimo = min(len(p1), len(p2))

    for i in range(tamanho_minimo):
        if ord(p1[i]) > ord(p2[i]):
            return -1   # p1 vem antes (porque queremos Z → A)
        elif ord(p1[i]) < ord(p2[i]):
            return 1    # p2 vem antes

    # caso uma seja prefixo da outra
    if len(p1) > len(p2):
        return -1
    elif len(p1) < len(p2):
        return 1
    return 0


#Bubble Sort inverso
def ordenar_za(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparar_palavras_inverso(lista[j], lista[j + 1]) > 0:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


#Teste
palavras = []
quantidade = int(input("Quantas palavras queres inserir? "))

for i in range(quantidade):
    palavra = input(f"Palavra {i+1}: ")
    palavras.append(palavra)

print("Lista original:", palavras)

ordenar_za(palavras)

print("Ordem inversa (Z → A):", palavras)