def comparar_palavras(p1, p2):
    tamanho_minimo = min(len(p1), len(p2))

    for i in range(tamanho_minimo):
        if ord(p1[i]) < ord(p2[i]):
            return -1
        elif ord(p1[i]) > ord(p2[i]):
            return 1

    if len(p1) < len(p2):
        return -1
    elif len(p1) > len(p2):
        return 1
    return 0


def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparar_palavras(lista[j], lista[j + 1]) > 0:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def agrupar_palavras(lista):
    grupos = {}

    for palavra in lista:
        inicial = palavra[0].lower()

        if inicial not in grupos:
            grupos[inicial] = []

        grupos[inicial].append(palavra)

    # ordenar cada grupo
    for chave in grupos:
        ordenar_lista(grupos[chave])

    return grupos


palavras = []
quantidade = int(input("Quantas palavras queres inserir? "))

for i in range(quantidade):
    palavras.append(input(f"Palavra {i+1}: "))

resultado = agrupar_palavras(palavras)

print("Grupos organizados:")
for chave in resultado:
    print(chave, ":", resultado[chave])