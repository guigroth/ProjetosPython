#from math import factorial
#fatorial = factorial(num)
num = int(input("Digite um número para calcular seu fatorial: "))
cont = num
fact = 1 
print(f"Calculando o fatorial de {num}! = ", end="")
while cont > 0:
    print(f"{cont} ", end="")
    print("x" if cont > 1 else " = ", end=" ")
    fact *= cont
    cont -= 1
print(f"{fact} ")

