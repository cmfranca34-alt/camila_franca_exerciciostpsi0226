d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

resultado = {}  # novo dicionário

for chave in d1: #copia d1
    resultado[chave] = d1[chave]

for chave in d2: #copia d2
    resultado[chave] = d2[chave]

print(resultado)