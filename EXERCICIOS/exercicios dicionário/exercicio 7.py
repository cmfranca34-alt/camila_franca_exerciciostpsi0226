d = {'a': 1, 'b': 2, 'c': 3}

invertido = {}  # novo dicionário

for chave in d: # percorre original
    valor = d[chave]  # guarda valor
    invertido[valor] = chave # troca posição

print(invertido)