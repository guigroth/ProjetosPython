maior = 0
menor = 0
for x in range(1, 6):
    peso = float(input(f"O peso da {x}º pessoa é: "))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O Maior peso foi de: {maior}")
print(f"O Menor peso foi de: {menor}")        


