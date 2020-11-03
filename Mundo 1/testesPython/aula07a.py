n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
subtracao = n1 - n2
potenciacao = n1 ** n2
divisaoInteira = n1 // n2 
modulo = n1 % n2
raizQuadrada = n1 ** n2 / (1/2)
print(f"""O resultado da soma é: {soma},\nO resultado da múltiplicação é: {multiplicacao},
O resultado da divisão é: {divisao:.3f},\nO resultado da subtração é: {subtracao},
O resultado da potenciação é: {potenciacao},\nO resultado da divisao inteira é: {divisaoInteira},
O resultado do módulo é: {modulo},\nO resultado da raiz quadrada é: {raizQuadrada}""")
# ":.2f"(2 casas) para ajustar a quantidade da casas após a vírgula (no caso ponto).
# """ Use to a very long string ......
# ....that can span multiple lines """