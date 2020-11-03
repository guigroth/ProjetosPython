print("-="*30)
print("SEQUÊNCIA DE FIBONACCI")
termos = int(input("Digite a quantidade de termos que deseja mostrar na tela: "))
n1 = 0
n2 = 1
print(f"{n1} -> {n2}",end=" ")
cont = 3
while cont <= termos:
    terceiro = n1 + n2
    print(f" -> {terceiro}",end="")
    n1 = n2
    n2 = terceiro
    cont += 1
print(' -> Fim')
print("-="*30)