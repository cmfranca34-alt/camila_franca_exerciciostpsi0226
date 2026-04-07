alunos = []  # lista para guardar vários alunos

while True:
    print("\n1 - Inserir")
    print("2 - Listar")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        aluno = {}  #cria dicionário vazio

        aluno["nome"] = input("Nome: ")      # adiciona nome
        aluno["idade"] = int(input("Idade: "))  # adiciona idade
        aluno["curso"] = input("Curso: ")    # adiciona curso

        alunos.append(aluno)  # guarda aluno na lista

    elif opcao == "2":
        for a in alunos:  # percorre todos os alunos
            print("\nnome:", a["nome"])  # imprime nome
            print("idade:", a["idade"])  # imprime idade
            print("curso:", a["curso"])# imprime curso

    elif opcao == "0":
        break  #termina programa