soma = cont = 0
while True: #While True é um looping infinito, e só pode ser interrompido pelo uso do break.
    num = int(input("Digite um número: [999 para parar]: "))
    if num == 999:
        break
    cont += 1
    soma += num # A SOMA E O CONT PRECISAM ESTAR APÓS O BREAK, PARA QUE O 999 NÃO SEJA INCLUÍDO NO RESULTADO!
print(f"Você digitou um total de {cont} números e a soma deles é igual a {soma}")
print("Fim")