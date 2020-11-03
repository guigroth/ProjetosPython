print("="*15)
print("GERADOR DE P.A ")
print("="*15)
priTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termos = priTermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termos} -> ", end="")
        termos += razao
        cont += 1
    print("PAUSA...")
    mais = int(input("Quantos termos você deseja mostrar a mais? [Digite 0 para finalizar]: "))
print(f"Você finalizou sua P.A mostrando um total de {total} termos!")
print("Fim...")
