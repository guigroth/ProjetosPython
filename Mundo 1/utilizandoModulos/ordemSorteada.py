from random import shuffle
primeiro = input("Digite o nome do primeiro aluno: ")
segundo = input("Digite o nome do segundo aluno: ")
terceiro = input("Digite o nome do terceiro aluno: ")
quarto = input("Digite o nome do quarto aluno: ")
lista = [primeiro, segundo, terceiro, quarto]
shuffle(lista) #o método shuffle serve para embaralhar uma lista.
print(f"O Aluno sorteado foi: {lista}")