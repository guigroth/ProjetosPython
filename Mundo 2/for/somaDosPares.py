soma = 0
cont = 0
for x in range(1, 7):
    x = int(input(f"Digite o {x}º numero inteiro: "))
    if x % 2 == 0:
        soma += x
        cont += 1
print(f"Você informou {cont} números pares e a soma deles é igual a: {soma}")
