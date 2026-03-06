
#Recebe um dicionário com as chaves "categoria" e "preco".
#Retorna:
#•	“Produto de luxo” se categoria for “eletrônico” e preço acima de 1000
#•	“Produto comum” se categoria for “eletrônico” e preço até 1000
#•	“Produto alimentar” se categoria for “alimento”
#•	“Categoria desconhecida” caso contrário
#Exemplo:
#Entrada → {"categoria": "eletrônico", "preco": 1500}
#Saída → Produto de luxo

from unidecode import unidecode # para aceitar a insercao com ou sem acento

categoria = unidecode(input("Insira a categoria (eletrônico/alimento ou outro): ")).lower()
preco = float(input("Insira o preço: "))
produto = {"categoria": categoria, "preco": preco}  # criação do dicionário

if produto ["categoria"] == "eletronico" and preco > 1000:
    print(f"Produto de luxo")
elif produto ["categoria"] == "eletronico" and preco  <= 1000:
    print(f"Produto comum")
elif produto ["categoria"] == "alimento":
    print("Produto alimentar")
else:
    print("Categoria desconhecida")
