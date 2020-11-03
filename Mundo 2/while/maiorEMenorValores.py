#LEMBRAR DE NÃO REPETIR DECLARAÇOES DE VARIÁVEIS, POIS PODE ACARRETAR EM ERROS DURANTE A EXECUÇÃO!!
opcao = "s"
maior = menor = soma = cont = num = 0
while opcao in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input("Quer continuar? [S/N]")).upper().split()[0]
print(f"Você digitou {cont} números, e a média é {soma / cont}") #Média direto no print para economizar linhas.
print(f"O maior valor foi {maior} e o menor foi {menor}")
print("Fim")
    
