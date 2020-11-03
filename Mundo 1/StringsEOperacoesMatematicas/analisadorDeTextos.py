nome = str(input("Digite seu nome completo: ")).strip()
separador = nome.split()
print("Analizando seu nome...",
f"\nEscrito com todas as letras maiúsculas fica: {nome.upper()}",
f"\nEscrito com todas as letras minúsculas fica: {nome.lower()}",
f"\nSeu nome ao todo tem: {len(nome)} letras",
f"\nO seu primeiro nome é {separador[0]}, e a quantidade de letras que ele possui é: {len(separador[0])}") 