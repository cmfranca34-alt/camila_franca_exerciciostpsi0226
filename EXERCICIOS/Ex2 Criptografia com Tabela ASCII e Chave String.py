def calcular_chave_numerica(chave):
    soma = 0         #começa a soma em 0
    for c in chave:   #percorre cada letra da chave
        soma = soma + ord(c)  # soma o valor ASCII de cada letra
    return soma     #devolve o total (ex: "chave" -> 519)
 
 
def criptografar(mensagem, chave):
    chave_num = calcular_chave_numerica(chave)  #calcula a chave numérica
    codigos = []  #lista vazia para guardar os códigos
 
    for c in mensagem:     #percorre cada caractere da mensagem
        valor_encriptado = ord(c) + chave_num   #soma o ASCII do caractere com a chave
        codigos.append(valor_encriptado)   #adiciona o código à lista
 
    return codigos                              #devolve a lista de códigos
 
 
def descriptografar(codigos, chave):
    chave_num = calcular_chave_numerica(chave)      # calcula a mesma chave numérica
    mensagem = ""                                   # começa com string vazia
 
    for codigo in codigos:                          # percorre cada código encriptado
        valor_original = codigo - chave_num         # subtrai a chave para obter o ASCII original
        mensagem = mensagem + chr(valor_original)   # converte o número de volta para letra
 
    return mensagem                                 # devolve a mensagem original
 
 
def listar(codigos):
    print("\nCódigos encriptados:")
    for i in range(len(codigos)):       # percorre os índices da lista
        print("posição", i, "->", codigos[i])
 
 
# -------------------------------------------------------
# PROGRAMA PRINCIPAL COM MENU
 
codigos_guardados = []  # lista para guardar os códigos entre opções do menu
 
while True:
    print("\n1 - Criptografar mensagem")
    print("2 - Descriptografar mensagem")
    print("3 - Listar códigos encriptados")
    print("4 - Sair")
 
    opc = input("Escolha uma opção: ")
 
    match opc:
 
        case "1":
            mensagem = input("Introduz a mensagem: ")
            chave = input("Introduz a chave: ")
 
            if len(chave) == 0:                             # impede chave vazia
                print("Erro: a chave não pode estar vazia!")
            else:
                chave_num = calcular_chave_numerica(chave)
                codigos_guardados = criptografar(mensagem, chave)
                print("Chave numérica:", chave_num)
                print("Códigos encriptados:", codigos_guardados)
 
        case "2":
            if len(codigos_guardados) == 0:                 # verifica se já há mensagem encriptada
                print("Ainda não há mensagem encriptada!")
            else:
                chave = input("Introduz a chave para descriptografar: ")
                if len(chave) == 0:                         # impede chave vazia
                    print("Erro: a chave não pode estar vazia!")
                else:
                    resultado = descriptografar(codigos_guardados, chave)
                    print("Mensagem original:", resultado)
 
        case "3":
            if len(codigos_guardados) == 0:                 # verifica se já há mensagem encriptada
                print("Ainda não há mensagem encriptada!")
            else:
                listar(codigos_guardados)
 
        case "4":
            print("A sair...")
            break                                           # termina o ciclo
 
        case _:
            print("Opção inválida!")