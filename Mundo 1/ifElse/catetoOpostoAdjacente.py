#Usando import
from math import hypot
comprimentoCatOp = float(input("Qual é o comprimento do cateto oposto? ")) 
comprimentoCatAdj = float(input("Qual é o comprimento do cateto adjacente? "))
hipotenusa = hypot(comprimentoCatOp, comprimentoCatAdj)
print(f"O Comprimento da hipotenusa é igual a: {hipotenusa:.2f}")



""" comprimentoCatOp = float(input("Qual é o comprimento do cateto oposto? "))
comprimentoCatAdj = float(input("Qual é o comprimento do cateto adjacente? "))
hipotenusa = (comprimentoCatOp ** 2 + comprimentoCatAdj ** 2) ** (1/2) #FÓRMULA PARA CALCULAR HIPOTENUSA
print(f"O comprimento da hipotenusa é igual a: {hipotenusa:.2f}")
 """

