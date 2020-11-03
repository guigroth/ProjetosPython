soma = 0 #Acumulador
cont = 0 #Contador
for x in range(1, 501, 2): #Maneira mais fácil de fazer com que o laço mostre um número ímpar.
    if x % 3 == 0:
        soma += x
        cont += 1
print(f"a soma de todos os {cont} valores é: {soma}")
