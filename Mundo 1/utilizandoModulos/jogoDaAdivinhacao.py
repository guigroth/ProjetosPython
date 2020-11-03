from random import randint
from time import sleep
print("=" * 33)
print("BEM VINDO AO JOGO DA ADIVINHAÇÃO!")
print("=" * 33)
numero = int(input("Digite um número: "))
numeroCPU = randint(0, 5)
print("PPROCESSANDO...")
sleep(1)
print(f"EU ESCOLHI O NÚMERO: {numeroCPU}")
if numeroCPU ==  numero:
    print("Você Ganhou! Boooooa Men Jogou o Fino do Fino")
else:
    print("Você Perdeu! kkk ruinzão")
