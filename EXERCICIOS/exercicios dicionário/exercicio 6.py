vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}

total = 0  # acumulador

for mes in vendas:        # percorre chaves
    total += vendas[mes]  # soma valores

print("Total:", total)