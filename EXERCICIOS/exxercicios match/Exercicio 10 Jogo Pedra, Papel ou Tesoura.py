
#Cria um programa que receba duas jogadas:
#* Jogador 1
#* Jogador 2
#Usa match para determinar o resultado:
#* Pedra ganha de Tesoura
#* Tesoura ganha de Papel
#* Papel ganha de Pedra
#* Se forem iguais, é Empate
#Exemplo: Entrada → Jogador 1: pedra Jogador 2: tesoura Saída → Jogador 1 venceu

j1 = input("Jogador 1: ").lower()
j2 = input("Jogador 2: ").lower()

match (j1, j2):
    case ("pedra", "tesoura"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra"):
        print("Jogador 2 venceu")
    case ("tesoura", "papel"):
        print("Jogador 1 venceu")
    case ("papel", "tesoura"):
        print("Jogador 2 venceu")
    case ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("pedra", "papel"):
        print("Jogador 2 venceu")
    case (x, y) if x == y:
        print("Empate")
    case _:
        print("Jogada inválida")