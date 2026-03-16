
#Elabore um ciclo for para produzir o seguinte output.
#	1
#	22
#	333
#	4444
#	55555

for i in range (1, 6): # i vai ser 1 a 5
    for j in range(1, i+1): #repete i vezes
          print(i, end="") #mostra sem saltar a linha
    print()

