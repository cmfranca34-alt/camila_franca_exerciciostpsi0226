#Ler a nota de 10 alunos, calcular a media e mostrar essa média.


soma = 0 #comecar a contar do 0 e vai adicionando
#loop de repeticao
for i in range (10): # vai repetir 10x para o utilizador colocar um numero
   nota = int(input("Digite a nota do aluno: ")) 
   soma = soma + nota
   media = soma / 10

print(f"A média das notas dos alunos é {media}")