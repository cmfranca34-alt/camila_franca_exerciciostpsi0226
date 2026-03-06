
#Recebe uma operação (em texto) e dois números.
#Operações válidas: "soma", "subtrai", "multiplica", "divide".
#Exemplo:
#Entrada →
#Operação: "divide"
#Número 1: 20
#Número 2: 4
#Saída → 5

operacao = input("Insira a operação pretendida (soma, subtrai, multiplica ou divide): ").lower()
num1 = float(input("Insira o número 1: "))
num2 = float(input("Insira o número 2: "))

if operacao == "soma":
    print(num1 + num2)
elif operacao == "subtrai":
    print(num1 - num2)
elif operacao == "multiplica":
    print(num1 * num2)
elif operacao == "divide":
    if num2 == 0:
        print("Erro: não é possível dividir por zero!")
    else:
        print(num1 / num2)
else:
    print("Operação desconhecida")
    
