
#Enunciado:
#Uma loja oferece descontos de acordo com o valor da compra:
#10% para compras até 200,00€.
#15% para compras entre 200,01€ e 500,00€.
#20% para compras acima de 500,00€.
#Desenvolva um Programa que leia o nome do cliente e o valor da compra e mostre o valor do desconto e o valor total a pagar.
#Exemplo:
# Entrada: Cliente: João, Compra: 350
#Saída esperada:
#  Nome: João
#Compra: 350,00€
#Desconto: 52,50€
#Total a pagar: 297,50€

nome_cliente = str(input ("Escreva seu nome: "))
valor_compra = float(input("Qual o valor da sua compra? "))

if valor_compra <= 200 :
    desconto = valor_compra * 0.10
elif valor_compra >= 201 and valor_compra == 500 :
    desconto = valor_compra * 0.15
else :
    desconto = valor_compra * 0.20
 
 
total_pagar = valor_compra - desconto

print((f"Cliente: {nome_cliente}\n Compra: {valor_compra}\n Desconto: {desconto}\n Total a pagar: {total_pagar}"))




