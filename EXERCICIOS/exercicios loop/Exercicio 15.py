#Elabore um programa que escreva no ecrã todas as 
#linhas de código ASCII(0 a 255) e o código correspondente. Dispor de 20 em 20 com a condição de continuação ou saída do programa.

contador = 0  #conta quantos caracteres já foram mostrados nessa rodada

for codigo in range(0, 256):  #percorre todos os códigos de 0 a 255

    caractere = chr(codigo)  #converte o número no caractere ASCII correspondente

    print(codigo, "=", caractere)  #mostra o número e o caractere

    contador = contador + 1  #adiciona 1 ao contador

    if contador == 20:  #quando chegar a 20 caracteres mostrados...

        resposta = input("\nContinuar? (s = sim / n = não): ")  #pergunta se quer continuar

        if resposta == "n":  #se digitou n...
            print("Programa encerrado!")
            break  #para o loop e sai do programa

        contador = 0  #se digitou s, zera o contador e continuas
