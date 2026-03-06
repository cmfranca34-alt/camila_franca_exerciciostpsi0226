
#Enunciado:
#O sistema de avaliação de uma disciplina tem três provas com pesos diferentes. A primeira tem peso 2, a segunda tem peso 3, e a terceira tem peso 5.
#  Crie um programa para calcular a média final de um aluno e mostrar se ele está APROVADO (nota >= 6) ou REPROVADO (nota < 6).
#Exemplo:
#Entrada: Nota1 = 7, Nota2 = 6, Nota3 = 9
#Saída esperada:
#Média: 7.4
#Aprovado

nota1 = float(input("Insita a nota 1: "))
nota2 = float(input("Insira a nota 2: "))
nota3 = float(input("Insira a nota 3: "))

media = (nota1 *2 + nota2 *3 + nota3 *5) / 10

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
