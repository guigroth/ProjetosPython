print("="*8)
print("TABUADA")
print("="*8)
while True:
    num = int(input("Digite um número para ver sua tabuada! (Negativo para finalizar): "))
    if num < 0:
        break
    for x in range(1, 11):
        print(f"{num} X {x} = {num * x}")
print("Fim")
