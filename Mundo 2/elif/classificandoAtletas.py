from datetime import date
anoAtual = date.today().year
anoNasc = int(input("Digite seu ano de nascimento: "))
idade = anoAtual - anoNasc
print(f"O atleta tem {idade} anos de idade")
if idade <= 9:
    print("Sua categoria é MIRIM")
elif idade <= 14:
    print("Sua categoria é INFANTIL")
elif idade <= 19:
    print("Sua categoria é JÚNIOR")
elif idade <= 25:
    print("Sua categoria é SÊNIOR")
elif idade > 25:
    print("Sua categoria é MASTER")

