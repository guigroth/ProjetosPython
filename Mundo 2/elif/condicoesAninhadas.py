nome = str(input("Digite seu nome: ")).strip()
if nome == "Guilherme":
    print("Que nome bonito! :)")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bastante popular no Brasil!")
    
# in = se 'x' está dentro de 'y' irá retornar "true", por isso não foi necessário usar lista aqui.(espaços separam automaticamente).
elif nome in ("Joyce Ana Claudia Jessica Juliana"): 
    print("Belo nome feminino! :)")
print(f"Bom dia {nome}!")