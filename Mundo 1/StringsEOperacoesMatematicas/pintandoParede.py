largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
tinta = area / 2
print(f"""Sua parede tem a dimensão de: {largura}x{altura} 
Sua área é de: {area:.3f}m².
Você precisará de: {tinta:.2f}litros de tinta para pintar essa parede.""")