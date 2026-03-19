# : Elabore uma base de dados de clientes de uma fábrica de materiais. 
# O programa deverá possibilitar inserção e listagem dos clientes bem como as compras por eles efetuadas( Númcli(Automático),
#  NomCli, morada, tel, nif, compra, Divfin ). Divida final=compra – desconto, valor do desconto se compra for entre 100 e 200 é 5%,
#  se for superior a 200 e inferior a 500 é 10% se superior a 500 é 15%. O programa deve validar todas as entradas e na listagem 
# deve parar cliente a cliente e ser possível busca direta por número de cliente.

clientes = []   # cria uma lista vazia para guardar todos os clientes
id_cliente = 1 # define o número inicial do cliente, vai aumentando automaticamente

while True: # loop infinito para o menu continuar a aparecer até o utilizador sair

    print("\n  BASE DE DADOS CLIENTES")    #mostra o título do menu
    print("1 - Inserir Cliente")       #opção 1 do menu
    print("2 - Listar Clientes")  # opção 2 do menu
    print("3 - Buscar por Nº Cliente")   #opção 3 do menu
    print("0 - Sair")    # opção para encerrar o programa

    opcao = int(input("Escolha uma opção: "))  # lê a opção do utilizador e converte para número inteiro

    # ---- OPÇÃO 1: INSERIR CLIENTE ----
    if opcao == 1:          #verifica se o utilizador escolheu a opção 1

        print("\n INSERIR CLIENTE")  #mostra o título da secção

        while True:     #loop que repete até o nome ser válido
            nomcli = input("Nome do cliente: ") #pede o nome ao utilizador
            if len(nomcli) < 2:   #verifica se o nome tem menos de 2 caracteres
                print("Nome inválido! Digite pelo menos 2 caracteres.")  # avisa se for inválido
            else:
                break      #sai do loop se o nome for válido

        while True:             # loop que repete até a morada ser válida
            morada = input("Morada: ")    # pede a morada ao utilizador
            if len(morada) < 5:      #verifica se a morada tem menos de 5 caracteres
                print("Morada inválida! Digite pelo menos 5 caracteres.")  # avisa se for inválida
            else:
                break  #sai do loop se a morada for válida

        while True:     #loop que repete até o telefone ser válido
            tel = input("Telefone (9 dígitos): ")   # pede o telefone ao utilizador
            if len(tel) == 9 and tel.isdigit():    #verifica se tem exatamente 9 dígitos numéricos
                break       #sai do loop se for válido
            else:
                print("Telefone inválido! Digite exatamente 9 números.")  #avisa se for inválido

        while True:            #loop que repete até o NIF ser válido
            nif = input("NIF (9 dígitos): ")   #pede o NIF ao utilizador
            if len(nif) == 9 and nif.isdigit():   #verifica se tem exatamente 9 dígitos numéricos
                break      #sai do loop se for válido
            else:
                print("NIF inválido! Digite exatamente 9 números.")  #avisa se for inválido

        while True:    #loop que repete até o valor da compra ser válido
            try:       #tenta executar o bloco, se falhar vai para o except
                compra = float(input("Valor da compra (€): "))  #pede o valor e converte para decimal
                if compra < 0:     #verifica se o valor é negativo
                    print("Valor inválido! O valor não pode ser negativo.")  # avisa se for negativo
                else:
                    break          #sai do loop se o valor for válido
            except ValueError:     #apanha o erro se o utilizador escrever letras em vez de números
                print("Valor inválido! Digite um número.")  # avisa que tem de escrever um número

        # Calcular desconto
        if compra >= 100 and compra <= 200:  #verifica se a compra está entre 100€ e 200€
            desconto = compra * 0.05      #aplica 5% de desconto
        elif compra > 200 and compra < 500:    #verifica se a compra está entre 200€ e 500€
            desconto = compra * 0.10      # aplica 10% de desconto
        elif compra >= 500:           # verifica se a compra é igual ou superior a 500€
            desconto = compra * 0.15      # aplica 15% de desconto
        else:
            desconto = 0   # sem desconto para compras abaixo de 100€

        divfin = compra - desconto    # calcula a dívida final subtraindo o desconto à compra

        cliente = {               #cria um dicionário com todos os dados do cliente
            "numcli"  : id_cliente,             # número único gerado automaticamente
            "nomcli"  : nomcli,         # nome inserido pelo utilizador
            "morada"  : morada,        # morada inserida pelo utilizador
            "tel"     : tel,        # telefone inserido pelo utilizador
            "nif"     : nif,  # NIF inserido pelo utilizador
            "compra"  : round(compra, 2),  # valor da compra arredondado a 2 casas decimais
            "desconto": round(desconto, 2), # valor do desconto arredondado a 2 casas decimais
            "divfin"  : round(divfin, 2)   # dívida final arredondada a 2 casas decimais
        }

        clientes.append(cliente)      # adiciona o dicionário do cliente à lista principal
        id_cliente += 1       # aumenta o número automático para o próximo cliente

        print("\nCliente inserido com sucesso!") # confirma que o cliente foi guardado
        print("Nº Cliente  :", cliente["numcli"])   # mostra o número do cliente
        print("Nome        :", cliente["nomcli"])  # mostra o nome do cliente
        print("Morada      :", cliente["morada"])  # mostra a morada do cliente
        print("Telefone    :", cliente["tel"])    # mostra o telefone do cliente
        print("NIF         :", cliente["nif"])  # mostra o NIF do cliente
        print("Compra      :", cliente["compra"], "€")  # mostra o valor da compra
        print("Desconto    :", cliente["desconto"], "€")  # mostra o valor do desconto
        print("Dívida Final:", cliente["divfin"], "€")  # mostra a dívida final

    # ---- OPÇÃO 2: LISTAR CLIENTES ----
    elif opcao == 2:            # verifica se o utilizador escolheu a opção 2

        if len(clientes) == 0:        # verifica se a lista de clientes está vazia
            print("Nenhum cliente registado!")   # avisa se não houver clientes
        else:
            print("\n  LISTA DE CLIENTES")  #mostra o título da listagem
            print("  Total:", len(clientes), "clientes")  # mostra quantos clientes existem no total

            for i in range(len(clientes)):    # percorre todos os clientes da lista um a um
                print("\nNº Cliente  :", clientes[i]["numcli"])   # mostra o número do cliente atual
                print("Nome        :", clientes[i]["nomcli"])     # mostra o nome do cliente atual
                print("Morada      :", clientes[i]["morada"])  # mostra a morada do cliente atual
                print("Telefone    :", clientes[i]["tel"])    # mostra o telefone do cliente atual
                print("NIF         :", clientes[i]["nif"]) # mostra o NIF do cliente atual
                print("Compra      :", clientes[i]["compra"], "€")  # mostra o valor da compra
                print("Desconto    :", clientes[i]["desconto"], "€")# mostra o valor do desconto
                print("Dívida Final:", clientes[i]["divfin"], "€")  # mostra a dívida final

                if i < len(clientes) - 1:   # verifica se ainda há mais clientes para mostrar
                    resposta = input("\nPróximo cliente? (s = sim / n = parar): ")  # pergunta se quer continuar
                    if resposta.lower() == "n": # .lower() aceita tanto "N" como "n"
                        break       # para a listagem se o utilizador escrever "n"

    # ---- OPÇÃO 3: BUSCAR POR Nº CLIENTE ----
    elif opcao == 3:   # verifica se o utilizador escolheu a opção 3

        if len(clientes) == 0:     # verifica se a lista de clientes está vazia
            print("Nenhum cliente registado!")   # avisa se não houver clientes para procurar
        else:
            try:        # tenta executar o bloco, se falhar vai para o except
                num = int(input("Digite o número do cliente: "))  # pede o número e converte para inteiro
                encontrado = False      # começa a assumir que o cliente não existe

                for cliente in clientes:     # percorre cada cliente da lista à procura do número
                    if cliente["numcli"] == num: # compara o número de cada cliente com o número pedido
                        encontrado = True  # marca que encontrou o cliente
                        print("\nCliente encontrado!")       # confirma que encontrou
                        print("Nº Cliente  :", cliente["numcli"])   # mostra o número do cliente
                        print("Nome        :", cliente["nomcli"]) # mostra o nome do cliente
                        print("Morada      :", cliente["morada"]) # mostra a morada do cliente
                        print("Telefone    :", cliente["tel"])  # mostra o telefone do cliente
                        print("NIF         :", cliente["nif"])   # mostra o NIF do cliente
                        print("Compra      :", cliente["compra"], "€") # mostra o valor da compra
                        print("Desconto    :", cliente["desconto"], "€") #mostra o valor do desconto
                        print("Dívida Final:", cliente["divfin"], "€") #mostra a dívida final
                        break   # para a busca assim que encontrar o cliente

                if not encontrado:    # se depois de percorrer tudo não encontrou
                    print("Cliente nº", num, "não encontrado!")  # avisa que o cliente não existe

            except ValueError:   # apanha o erro se o utilizador escrever letras
                print("Número inválido! Digite um número inteiro.")  # avisa que tem de ser um número

    # ---- OPÇÃO 0: SAIR ----
    elif opcao == 0:  # verifica se o utilizador escolheu sair
        print("A sair... Até logo!")   # mostra mensagem de despedida
        break    # quebra o while True e encerra o programa

    else:    # se o utilizador escrever um número fora de 0 a 3
        print("Opção inválida! Escolha entre 0 e 3.")  #avisa que a opção não existe


