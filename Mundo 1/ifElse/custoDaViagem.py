distancia = float(input("Digite a distância da viagem em Km: "))
print(f"Você está prestes a iniciar uma viagem de {distancia}Km")
if distancia < 200:
    custo = 0.50 * distancia
    print(f"O custo da viagem será de: {custo:.2f}R$")
else:
    custo = 0.45 * distancia
    print(f"A promoção foi aplicada, e o custo da viagem será de {custo:.2f}R$")