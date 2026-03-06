
#Cria um programa que receba o nome de um dia da semana e diga se é dia útil ou fim de semana.
#Exemplo:
#Entrada → domingo
#Saída → Fim de semana

from unidecode import unidecode # para aceitar a insercao com ou sem acento

dia = unidecode(input("Insira o dia da semana: ")).lower() #o lower para aceitar maiusculas e minusculas

if dia == "sabado"  or dia == "domingo":
   print (" Fim de semana ")
else:
   print (" Dia útil ")

   
