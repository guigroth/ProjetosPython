diasAlocados = int(input("Informe a quantidade de dias que o carro foi alugado: "))
kmRodados = float(input("Informe a quantidade de km rodados: "))
pago = (60 * diasAlocados) + (kmRodados * 0.15)
print(f"O preço total a pagar será de: {pago}R$")