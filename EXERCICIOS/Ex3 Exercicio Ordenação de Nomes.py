nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade"
]
 
 
def comparar_strings(s1, s2):
    #Compara duas strings caractere a caractere usando ord()
    tamanho_minimo = min(len(s1), len(s2))
 
    for i in range(tamanho_minimo):
        if ord(s1[i]) < ord(s2[i]):
            return -1   # s1 vem antes
        elif ord(s1[i]) > ord(s2[i]):
            return 1    # s2 vem antes
 
    #Uma é prefixo da outra → a mais curta vem primeiro
    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1
    return 0  # iguais
 
 
def comparar_nomes_completos(nome1, nome2):
    #Separar primeiro nome e apelido
    #Assumimos formato "Primeiro Apelido"
    partes1 = []
    partes2 = []
 
    palavra = ""
    for c in nome1 + " ":
        if c == " ":
            if len(palavra) > 0:
                partes1.append(palavra)
            palavra = ""
        else:
            palavra += c
 
    palavra = ""
    for c in nome2 + " ":
        if c == " ":
            if len(palavra) > 0:
                partes2.append(palavra)
            palavra = ""
        else:
            palavra += c
 
    if len(partes1) > 0:
        primeiro1 = partes1[0]
    else:
        primeiro1 = ""
 
    if len(partes1) > 1:
        apelido1 = partes1[1]
    else:
        apelido1 = ""
 
    if len(partes2) > 0:
        primeiro2 = partes2[0]
    else:
        primeiro2 = ""
 
    if len(partes2) > 1:
        apelido2 = partes2[1]
    else:
        apelido2 = ""
 
    #1º critério: comparar pelo primeiro nome
    resultado_primeiro = comparar_strings(primeiro1, primeiro2)
 
    if resultado_primeiro != 0:
        return resultado_primeiro
 
    #2º critério (desempate): comparar pelo apelido
    return comparar_strings(apelido1, apelido2)
 
 
def ordenar_nomes(lista):
    # Bubble Sort usando comparar_nomes_completos()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparar_nomes_completos(lista[j], lista[j + 1]) > 0:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
 
 
 
print("Lista original:")
for nome in nomes:
    print(" ", nome)
 
ordenar_nomes(nomes)
 
print("\nLista ordenada:")
for nome in nomes:
    print(" ", nome)