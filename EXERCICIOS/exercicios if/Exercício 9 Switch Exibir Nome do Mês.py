#enunciado
#Leia um número inteiro de 1 a 12 e mostre o nome do mês correspondente. Caso o número não seja válido, mostre uma mensagem de erro.
#Exemplo:
#Entrada: 5
#Saída esperada: Maio

num = int(input("Insira um número inteiro entre  1 a 12: "))

if num > 12 or num < 1:
   print (f" Número inválido, insira um número inteiro entre 1 e 12 ")
else:
   match num:
        case 1:
            print("Janeiro")
        case 2:
            print("Fevereiro")
        case 3:
            print("Março")
        case 4:
            print("Abril")
        case 5:
            print("Maio")
        case 6:
            print("Junho")
        case 7:
            print("Julho")
        case 8:
            print("Agosto")
        case 9:
            print("Setembro")
        case 10:
            print("Outubro")
        case 11:
            print("Novembro")
        case 12:
            print("Dezembro")

# meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
 #        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

#num = int(input("Insira um número inteiro entre 1 a 12: "))

#if 1 <= num <= 12:
 #   print(meses[num - 1])
#else:
 #   print("Número inválido, insira um número inteiro entre 1 e 12")