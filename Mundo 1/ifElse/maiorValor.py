v1 = float(input("Digite um valor: "))
v2 = float(input("Digite outro valor: "))
v3 = float(input("Digite outro valor: "))
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
print(f"O menor numero é: {menor}")

maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

print(f"O maior numero é: {maior}")



