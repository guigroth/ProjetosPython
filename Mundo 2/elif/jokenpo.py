from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
opcaoCPU = randint(0, 2)
print("{:=^50}".format(" BEM VINDO AO JOKENPO! "))
print('''ESCOLHA UMA DAS OPÇÕES ABAIXO: 
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA ''')
opcao = int(input("Digite sua opção: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
print("-=" * 15)
print(f"Você escolheu {itens[opcao]}") #Mostra ao usuário o que está contido dentro dos parênteses, e não o seu índice.
print(f"O computador escolheu {itens[opcaoCPU]}")
print("-=" * 15)
if opcaoCPU == 0:
    if opcao == 0:
        print("Empate Técnico")
    elif opcao == 1:
        print("Você ganhou!")   
    elif opcao == 2:
        print("Você perdeu!") 
    else:
        print("Opção Inválida!")
elif opcaoCPU == 1:
    if opcao == 1:
        print("Empate Técnico")
    elif opcao == 0:
        print("Você perdeu!")   
    elif opcao == 2:
        print("Você ganhou!")
    else:
        print("Opção Inválida!")
elif opcaoCPU == 2:
    if opcao == 2:
        print("Empate Técnico")
    elif opcao == 0:
        print("Você ganhou!")   
    elif opcao == 2:
        print("Você perdeu!")
    else:
        print("Opção Inválida!")

