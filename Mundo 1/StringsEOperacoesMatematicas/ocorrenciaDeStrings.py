frase = str(input("Digite uma frase: ")).strip().upper()
contadorDeLetras = frase.count("A")
posicaoIni = frase.find("A")
posicaoFi = frase.rfind("A")
print(f"A letra 'A' aparece {contadorDeLetras} vezes na frase")
print(f"A letra 'A' aparece pela primeira vez na posição: {posicaoIni + 1}") # +1 para "facilitar" a leitura de posições, fazedo com que se inicie a partir de 1.
print(f"A letra 'A' aparece pela última vez na posição: {posicaoFi + 1}")