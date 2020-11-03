peso = float(input("Digite seu peso (KG): "))
altura = float(input("Digite sua altura(m): "))
imc = peso / (altura ** 2)
print(f"O seu IMC é de {imc:.1f}")
if imc < 18.5:
    print("Você está abaixo do peso ideal, cuidado!")
elif imc >= 18.5 and imc < 25: # Ou 18.5 <= 18.5 imc < 25
    print("Você está no peso ideal")
elif imc >= 25 and imc < 30: # Ou 25 <= imc < 30
    print("Você está no sobrepeso")
elif imc >= 30 and imc < 40: # Ou 30 <= imc < 40
    print("Você está na obesidade")
elif imc > 40:
    print ("Você está na obesidade morbida, cuidado!")