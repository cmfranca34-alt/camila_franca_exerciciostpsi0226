
#Recebe um dicionário com as chaves "status" e "tempo_resposta".
#Retorna:
#•	“Servidor ativo” se o status for “ok”
#•	“Servidor lento” se o status for “ok” e o tempo de resposta for maior que 200 ms
#•	“Servidor indisponível” se o status for “erro”
#•	“Estado desconhecido” caso contrário
#Exemplo:
#Entrada → {"status": "ok", "tempo_resposta": 350}
#Saída → Servidor lento

status = input("Insira o status (ok ou erro): ").lower()
tempo_resposta = float(input("Insira o tempo de resposta do servidor: "))
servidor = {"status": status, "tempo_resposta": tempo_resposta}  # criação do dicionário

if servidor["status"] == "ok" and tempo_resposta < 200:
    print(f"Servidor ativo")
elif servidor ["status"] == "ok" and tempo_resposta > 200:
    print(f"Servidor lento")
elif servidor ["status"] == "erro":
    print("Servidor indisponível")
else:
    print("Estado desconhecido")

    