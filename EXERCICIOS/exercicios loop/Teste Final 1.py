#Elabore um programa que leia um valor de entrada e mostre para cada valor até ao 1 
#(se é número Primo, Quantos divisores e números perfeitos) o Programa deve validar entradas entre 1 e 30.000, 
#e parar de 10 em 10 valores com instrução para parar ou continuar. No mesmo programa use um menu e 
#Elabore uma calculadora simples (+,-,*,/) com a função extra tabuada. Validar entradas de 1 a 1000 
#(nota a tabuada deve apresentar todas as multiplicações de 1 ate ao máximo introduzido) deve parar de 20 em 20 valores.

while True:   #fica repetindo o menu até o utilizador sair

    
    print("  ========= MENU ========")
    print("1 - Analisador de Números")
    print("2 - Calculadora")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção (1,2 ou 0): "))

#### opção 1 ###

#primo, divisores e ns perfeitos

    if opcao == 1:
        numero = int(input("Digite um número entre 1 e 30000: "))
        if numero < 1 or numero > 30000:
            print("Número inválido! Digite um número entre 1 e 30000: ")
        else:
            contador_pausa = 0 # conta de 10 em 10 para pausar

            for n in range(numero, 0, -1):   # percorre do número até 1
                print("NÚMERO:", n)

                primo = True #vai assumir que é primo
                if n < 2:
                    primo = False # porque 0 e 1 não são primos

                for d in range (2, n): #vai testar todos os divisors de 2 até n-1
                    if n % d == 0:   #se encontrar um divisor
                        primo = False #não é primo
                        break #para aqui
                if primo:
                    print(" O número é primo")
                else:
                    print(" O número não é primo")


                # agora vamos contar os divisores
                
                soma_divisores = 0    # soma para verificar se é perfeito
                total_divisores = 0    # conta quantos divisores tem

                for d in range(1, n + 1):  # testa de 1 até o próprio número
                    if n % d == 0:         # se divide certinho...
                        total_divisores = total_divisores + 1  # conta o divisor
                        if d != n:         # não inclui o próprio número na soma
                            soma_divisores = soma_divisores + d  # acumula para verificar perfeito

                print("Divisores:", total_divisores)


                #aqui vamos verificar se é perfeito

                if soma_divisores == n:
                    print("O número é perfeito ") 
                    for d in range(1, n):
                        if n % d == 0:
                            print("d")
                    print(")")
                else:
                    print("O número não é perfeito")

                contador_pausa = contador_pausa + 1   # conta mais um valor mostrado

                if contador_pausa == 10:    # a cada 10 valores, pausa
                    resposta = input("\nContinuar? (s = sim / n = não): ")
                    if resposta == "n":
                        break              # sai do loop
                    contador_pausa = 0     # zera o contador e continua


#### opção 2 ####
    elif opcao == 2:

        while True:   # fica no menu da calculadora até o utilizador sair

            print("CALCULADORA")
            print("===================")
            print("1 - Somar")
            print("2 - Subtrair")
            print("3 - Multiplicar")
            print("4 - Dividir")
            print("5 - Tabuada")
            print("0 - Voltar ao Menu")


            opcao_calculadora = int(input("Escolha uma opção (1, 2, 3, 4, 5 ou 0) "))

            if opcao_calculadora == 0: #volta ao menu principal
                break

            elif opcao_calculadora in [1, 2, 3, 4]:

                a =  int(input("Digite o primeiro número (1 a 1000): "))
                b =  int(input("Digite o segundo número (1 a 1000): "))

                if a < 1 or a > 1000 or b < 1 or b > 1000:
                    print("Números inválidos! Digite entre 1 e 1000.")

                else:
                    if opcao_calculadora == 1:
                        resultado = a + b
                        print(a, "+", b, "=", resultado)

                    elif opcao_calculadora == 2:
                        resultado = a - b
                        print(a, "-", b, "=", resultado)

                    elif opcao_calculadora == 3:
                        resultado = a * b
                        print(a, "*", b, "=", resultado)

                    elif opcao_calculadora == 4:
                        if b == 0:
                            print("Erro! Não é possível dividir por zero.")
                        else:
                            resultado = a / b
                            print(a, "/", b, "=", resultado)

            elif opcao_calculadora == 5: #tabuada

                maximo = int(input("Digite o número máximo da tabuada (1 a 1000): "))

                if maximo < 1 or maximo > 1000:
                    print("Número inválido! Digite entre 1 e 1000.")

                else:

                    contador_pausa = 0   # conta de 20 em 20 para pausar

                    for numero in range(1, maximo + 1):    # para cada número de 1 até o máximo

                        print("TABUADA DO", numero)

                        for i in range(1, 11):             # multiplica de 1 a 10
                            resultado = numero * i
                            print(numero, "x", i, "=", resultado)
                            contador_pausa = contador_pausa + 1  # conta cada linha

                            if contador_pausa == 20:       # a cada 20 linhas, pausa
                                resposta = input("\nContinuar? (s = sim / n = não): ")
                                if resposta == "n":
                                    break
                                contador_pausa = 0

                        else:            # se o for de dentro terminou normalmente...
                            continue     # continua o for de fora

                        break            # se deu break no for de dentro, sai do for de fora também

            else:
                print("Opção inválida!")

    ### opção sair ####
    
    elif opcao == 0:
        print("")
        print("Programa encerrado!")
        break   # sai do loop principal

    else:
        print("Opção inválida!")





                 
