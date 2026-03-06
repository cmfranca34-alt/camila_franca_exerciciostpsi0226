
#Analisa um valor e retorna o seu tipo:
#•	Número inteiro
#•	Número decimal
#•	String numérica
#•	String textual
#•	Lista
#•	Tipo desconhecido
#Exemplo:
#Entrada → [10, 20, 30]
#Saída → Lista

valor = input("Insira um valor:")

if valor.startswith("[") and valor.endswith("]"):
    print("Lista")
elif "." in valor:
    try:
        float(valor)
        print("Número decimal")
    except:
        print("String textual")
elif valor.isnumeric():
    print("Número inteiro")
elif valor.isalpha():
    print("String textual")
else:
    print("Tipo desconhecido")