frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
juntar = "".join(palavras)
inverso = ""
inverso = juntar[::1] #Maneira mais simples utilizando fatiamento de strings.
""" for x in range (len(juntar) -1, -1, -1): # O primeiro -1 é para o range contar até a última letra da frase, o segundo é para ir até a primeira letra,
    inverso += juntar[x]                 # E o último é para voltar de trás pra frente de 1 em 1. """
if juntar == inverso:
    print(f"O inverso de {juntar} é  {inverso}, ou seja, essa frase é um Palíndromo")
else:
    print(f"O inverso de {juntar} é  {inverso}, ou seja, essa frase não é um Palíndromo")
