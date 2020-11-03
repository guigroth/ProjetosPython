from random import randint
print("="*22)
print("JOGO DO PAR OU IMPAR!")
print("="*22)
total = cont = vitoriasConsecutivas = 0
num = int(input("Digite um valor: "))
parImpar = str(input("Par ou Impar? [P/I]")[0].upper())
numCPU = randint(1, 10)
total = num + numCPU

while total % 2 == 0 and parImpar == "P":
    print(f"Você jogou {num} e a CPU jogou {numCPU}, totalizando {total}")
    print("Você Venceu!")
    vitoriasConsecutivas += 1
    print("Vamos jogar novamente...")
    if total % 2 == 0 and parImpar == "I":
        print(f"Você jogou {num} e a CPU jogou {numCPU}, totalizando {total}")
        print("A CPU Venceu!")
        break
    elif total % 2 != 0 and parImpar == "I":
        print(f"Você jogou {num} e a CPU jogou {numCPU}, totalizando {total}")
        print("Você Venceu!")
        vitoriasConsecutivas += 1
        print("Vamos jogar novamente...")
    elif total % 2 != 0 and parImpar == "P":
        print(f"Você jogou {num} e a CPU jogou {numCPU}, totalizando {total}")
        print("A CPU Venceu!")
        break
print(f"Você venceu um total de {vitoriasConsecutivas}")
    
    
