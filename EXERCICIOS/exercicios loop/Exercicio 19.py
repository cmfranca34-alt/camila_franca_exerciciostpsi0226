#Escreva um programa que mostre os primeiros 60 números da serie bonatchi.
# 1, 1, 2, 3, 5, 8, 13, 21.
# Como se constrói.
# 1+1=2
# 1+2=3
# 2+3=5

a = 1  # primeiro número da sequência
b = 1  #segundo número da sequência

print("SEQUÊNCIA DE FIBONACCI - PRIMEIROS 60 NÚMEROS")

print(a)  # mostra o primeiro número
print(b)  # mostra o segundo número

contador = 2  # já mostrou 2 números (o 'a' E o 'b')

while contador < 60:       # repete até mostrar 60 números

    c = a + b              # soma os dois anteriores para gerar o próximo
    print(c)               # mostra o novo número

    a = b                  # o primeiro vira o segundo
    b = c                  # o segundo vira o novo

    contador = contador + 1  # conta mais um número mostrado