
#Recebe um dicionário com as chaves "tipo" e "valor".
#Exibe:
#•	“Compra de X€” se tipo for “compra”
#•	“Venda de X€” se tipo for “venda”
#•	“Pedido desconhecido” caso contrário
#Exemplo:
#Entrada → {"tipo": "venda", "valor": 250}
#Saída → Venda de 250€

tipo = input("Insira o tipo (compra/venda): ").lower()
valor = float(input("Insira o valor em €: "))
pedido = {"tipo": tipo, "valor": valor}  # criação do dicionário

if pedido["tipo"] == "compra":
    print(f"Compra de {pedido['valor']}€")
elif pedido["tipo"] == "venda":
    print(f"Venda de {pedido['valor']}€")
else:
    print("Pedido desconhecido")