notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}

for aluno in notas:           # percorre alunos
    soma = 0                  # acumulador
    lista = notas[aluno]      # lista de notas

    for nota in lista:        # percorre notas
        soma += nota          # soma

    media = soma / len(lista) # calcula média

    print(aluno + ":", media)