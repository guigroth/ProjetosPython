print("="*15)
print("-"*15)
print("GERADOR DE P.A ")
print("-"*15)
priTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termos = priTermo
cont = 1
print(f"A razão de {priTermo} é:")
while cont <= 10:
    print(f"{termos} -> ", end="")
    cont += 1
    termos += razao
print("Fim")
print("="*15)
