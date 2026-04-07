produto = {}  # dicionário vazio

produto["nome"] = "Telemóvel"  #adiciona nome
produto["preço"] = 1500     #adiciona preço
produto["stock"] = 30      #adiciona stock

del produto["stock"]  #remove a chave "stock"

print(produto)  #mostra resultado final