import sys 
print("=" * 24)
print("ANALIZADOR DE TRIÂNGULOS")
print("=" * 24)
a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

if a < b + c and b < a + c and c < a + b:
    print("Essas 3 retas podem formar um triângulo.")
    if a == b == c: #Maneira simples de expressar uma igualdade (sem usar and ou or).
        print("Este triângulo é EQUILÁTERO")
    elif a == b or a == c and b == a or b == c and c == a or c == b:
        print("Este triângulo é ISÓSCELES")
    else:
        print("Este triângulo é ESCALENO") #Quando for expressar uma diferença, não é possível simplifica-la.
    """ elif a != b or a != c and b != a or b != c and c != a or c != b: 
        print("Este triângulo é ESCALENO") """
else:
    print("Essas 3 retas não podem formar um triângulo.")
    sys.exit()
