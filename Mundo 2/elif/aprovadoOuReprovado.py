n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
if media >= 7:
    print("Você está aprovado, Parabéns!")
elif media >= 4 and media <= 6.9:
    print("Você está em recuperação.")
elif media < 4:
    print("Você está reprovado.")
