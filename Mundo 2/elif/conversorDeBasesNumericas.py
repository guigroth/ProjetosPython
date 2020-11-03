numero = int(input("Digite um número: "))
print('''Escolha uma das opções abaixo para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')
opcao = int(input("Sua opção é: "))
if opcao  == 1:
    print(f"Seu número convertido para binário é: {bin(numero)}")
elif opcao == 2:
    print(f"Seu número convertido para octal é: {oct(numero)}")
elif opcao == 3:
    print(f"Seu número convertido para hexadecimal é: {hex(numero)}")
else:
    print("Opção Inválida")

