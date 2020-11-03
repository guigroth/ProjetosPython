numero = int(input("Digite um número: "))
unidade = numero // 1 % 10 #A divisão inteira nesse caso faz com que o número já apareça formatado sem nenhum ponto flutuante (facilitando na hora do print).
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")

