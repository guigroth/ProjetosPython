salario = float(input("Digite seu salário: "))
if salario >= 1250:
    bonificacao = salario * 0.10
    print(f"O seu novo salário será de: {bonificacao + salario:.2f}R$")
else:
    bonificacao = salario * 0.15
    print(f"O seu novo salário será de {bonificacao + salario:.2f}")