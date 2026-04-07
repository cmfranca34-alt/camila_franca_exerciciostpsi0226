#Função que compara duas palavras letra a letra usando ord()
#Devolve: -1 se p1 vem antes, 1 se p2 vem antes, 0 se são iguais

def comparar_palavras(p1, p2):
    tamanho_minimo = min(len(p1), len(p2))

    for i in range(tamanho_minimo):
        if ord(p1[i]) < ord(p2[i]):
            return -1    #p1 vem antes (letra mais "baixa" no alfabeto)
        elif ord(p1[i]) > ord(p2[i]):
            return 1      #p2 vem antes

    # Se chegámos aqui, uma palavra é prefixo da outra
    # Ex: "casa" e "casamento" -> "casa" vem primeiro (é mais curta)
    if len(p1) < len(p2):
        return -1
    elif len(p1) > len(p2):
        return 1
    return 0  #palavras iguais


# Bubble Sort: compara pares e troca se estiverem fora de ordem
def ordenar_az(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if comparar_palavras(lista[j], lista[j + 1]) > 0:
                #Troca as duas palavras de posição
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


palavras1 = []

quantidade = int(input("Quantas palavras queres inserir? "))

for i in range(quantidade):
    palavra = input(f"Insere a palavra {i + 1}: ")
    palavras1.append(palavra)

print("Palavras inseridas :", palavras1)
ordenar_az(palavras1)
print("Palavras inseridas por ordem alfabética:", palavras1)
