valorDaCasa = float(input("Digite o valor da casa: R$"))
salario = float(input("Quanto você ganha? "))
anos =  int(input("Em quantos anos deseja pagar? "))
prestacao = valorDaCasa / (anos * 12) #Ao multiplicar a quantidade de ANOS por 12, teremos a quantidade de MESES que o usuário irá pagar.
print(f"Para pagar uma casa de {valorDaCasa:.2f} em {anos} a prestação será de R${prestacao:.2f}")
if prestacao >= salario * 0.30:
    print("Emprestimo Negado!, a prestação excede a 30% do seu salário.")
else:
    print("Emprestimo Aceito!, Parabéns.")


