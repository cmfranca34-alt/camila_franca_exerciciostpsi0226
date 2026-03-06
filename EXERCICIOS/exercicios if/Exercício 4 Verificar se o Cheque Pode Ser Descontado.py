#Enunciado:
#Desenvolva um Programa que leia o saldo inicial de um cliente de banco e leia também o valor de um cheque. Analise se o cheque pode ser descontado. Se o cheque não puder ser descontado, mostre essa informação, caso contrário, desconte o cheque e informe o saldo atualizado.
#Exemplo:
#Entrada: Saldo = 500, Cheque = 300
#  #Saída esperada:
#Cheque descontado, saldo: 200


saldo_inicial = int(input("Insira o seu saldo inicial: "))
valor_cheque = int(input("Insira o saldo do seu cheque: "))

if saldo_inicial > valor_cheque:
    descontado = saldo_inicial - valor_cheque 
    print(f"Cheque descontado: saldo {descontado}")
else :
    print(f"Cheque näo pode ser descontado, saldo incial abaixo do esperado")