from time import sleep
num = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
opcao = 0
print("="*0)
while opcao != 5:
    opcao = int(input('''O que deseja fazer com os 2 valores?
[1] Somar
[2] Multiplicar
[3] Maior Valor
[4] Novos Números
[5] Sair: ''')) 
    if opcao == 1:
        print(f"A soma de {num} + {num2} é igual a: {num + num2}")
    elif opcao == 2:
        print(f"A multiplicação de {num} x {num2} é igual a: {num * num2}")
    if opcao == 3:
        if num > num2:
            print(f"O MAIOR valor é: {num}")
        else:
            print(f"O MAIOR valor é: {num2}")
    elif opcao == 4:
        num = int(input("Digite um NOVO valor: "))
        num2 = int(input("Digite outro valor: "))
    elif opcao > 5:
        print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE")
    sleep(1.5)
print("="*20)
print("Fim, Volte Sempre! :)")
print("="*20)
     

    