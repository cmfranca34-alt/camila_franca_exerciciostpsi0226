
#Enunciado:
#Crie um programa que leia a nota de 10 alunos (notas de 0 a 20), calcule a média das notas e mostre a média. 
# Além disso, informe quantos alunos ficaram com a nota igual ou acima da média. 

print ("Insira as notas dos alunos abaixo entre 0 a 20")
nota1 = float(input("Insita a nota do primeiro aluno : "))
nota2 = float(input("Insira a nota do segundo alunno: "))
nota3 = float(input("Insira a nota do terceiro aluno: "))
nota4 = float(input("Insita a nota do quarto aluno: "))
nota5 = float(input("Insira a nota do quinto aluno: "))
nota6 = float(input("Insira a nota do sexto aluno: "))
nota7 = float(input("Insita a nota do sétimo aluno: "))
nota8 = float(input("Insira a nota do oitavo aluno: "))
nota9 = float(input("Insira a nota do nono aluno: "))
nota10 = float(input("Insira a nota do décimo aluno: "))

notas = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10)
media = notas / 10

print(f"A média das notas dos alunos é {media}")

if notas >= media:
    print(f" Ficaram {notas} com a nota igual ou acima da media")

