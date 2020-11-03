from datetime import date
anoAtual = date.today().year 
maioridade = 0
menorIdade = 0
for x in range(1, 8):
    dataNasc = int(input(f"Em que ano nasceu a {x}º pessoa? "))
    idade = anoAtual - dataNasc
    if idade >= 18 :
        maioridade += 1
    else:
        menorIdade += 1
print(f"Ao todo tivemos {maioridade} pessoas maiores de idade.")
print(f"E tivemos {menorIdade} pessoas menores de idade.")
    