num = cont = soma = 0  #Forma simplificada para declarar um valor inicial que sejam iguais para várias variáveis ao mesmo tempo.
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um  número [999 para parar]: "))
print(f"Você digitou um total de {cont} números, e a soma de todos eles é igual a: {soma}")
print("Fim")


