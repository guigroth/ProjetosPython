from math import sin, cos, tan, radians
angulo = float(input("Digite o valor do ângulo: "))
#PRIMEIRO ESCREVE-SE A IDENTIDADE TRIGONOMÉTRICA, DEPOIS CONVERTE-SE PARA RADIANOS!
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'''O valor do seno de {angulo} é: {seno:.2f},
O valor do cosseno de {angulo} é: {cosseno:.2f},
O valor da tangente de {angulo} é: {tangente:.2f}''')
