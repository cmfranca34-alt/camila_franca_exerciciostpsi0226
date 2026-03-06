
#. Análise de mensagem
#Recebe uma mensagem e retorna:
#•	“Saudação” se for “olá” ou “bom dia”
#•	“Pergunta” se terminar com “?”
#•	“Despedida” se contiver “tchau” ou “adeus”
#•	“Mensagem genérica” caso contrário
#Exemplo:
#Entrada → “Tudo bem?”
#Saída → Pergunta

mensagem = input("Insira uma mensagem: ").lower()

if mensagem == "olá" or mensagem =="bom dia":
    print("Saudação")
elif mensagem.endswith("?"):
    print("Pergunta")
elif mensagem == "tchau" or mensagem == "adeus":
    print("Despedida")
else:
    print("Mensagem genérica")