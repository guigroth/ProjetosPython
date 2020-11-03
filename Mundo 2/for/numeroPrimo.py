num = int(input("Digite um número: "))
total = 0
for x in range(1, num + 1):
    if num % x == 0:
        print("\033[33m", end=" ")
        total += 1 #TODA VEZ QUE O NÚMERO FOR DIVISÍVEL PELO VALOR ATUAL DE "x" NO RANGE, O TOTAL RECEBERÁ +1.
    else:
        print("\033[31m", end=" ")
    print(f"{x}", end="")
print(f"\n\033[mO número {num} foi divisível {total} vezes")
if total == 2: # NO MOMENTO EM QUE O TOTAL RECEBER 2 VALORES, O NÚMERO SERÁ PRIMO.
    print("E por isso é um número primo")
else:
    print("E por isso não é um número primo")