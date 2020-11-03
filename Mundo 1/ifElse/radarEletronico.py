velocidade = float(input("Digite a velocidade atual do seu carro: "))
multa = (velocidade - 80) * 7.00
if velocidade > 80:
    print(f"Você ultrapassou o limite permitido, sua multa será de {multa:.2f}R$.")
else:
    print(f"Você está dentro do limite permitido, prossiga com segurança.")
print("Tenha um bom dia motorista!")