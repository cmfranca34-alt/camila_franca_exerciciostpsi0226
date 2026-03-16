#Crie um algoritmo que mostre os 10 primeiros números primos.


primos = 0 #comeca com numero 0, pois ainda nao tem nenhum numero 0
num = 2 # primeiro numero a ser testado. comeca logo pelo 2, porque o 1 nao eh primo

while primos < 10: # vai testando ate achar 10 primos
    primo = True # a cada num que entra eh dado como primo, ate que prove o contratio
    for i in range(2, num): # aqui vai testar os numeros, entre 2 e ele mesmo
        if num % i == 0:    # se algum dividir sem sobra,
            primo = False  #primo falso
    if primo:         #se primo vai      
        print(num)  #vai colocar na tela o numero e
        primos = primos + 1 #e adiciona em primos
    num = num + 1     # avanca para o proximo numero, sem isso vai ficar testando com 2 para sempre      

    