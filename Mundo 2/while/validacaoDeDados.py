sexo = str(input("Digite seu sexo [M] ou [F]: ")).upper().strip()[0]
""" while sexo != "M" and sexo != "F": """
while sexo not in "MmFf": #MESMO COM A FUNÇÃO UPPER ATIVADA NA VARIÁVEL "SEXO" o melhor a fazer é colocar as letra maiúsculas e minúscolas na condição para evitar bugs.
    sexo = input("Dados incorretos, por favor digite seu sexo novamente: ") # UM INPUT NÃO IRÁ REPETIR INFINITAS VEZES, UM PRINT SIM.
print(f"Sexo {sexo} registrado com sucesso")
 