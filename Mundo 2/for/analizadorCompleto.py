maioridadeH = 0
nomehmaisvelho = ""
somaidade = 0
menoridadeM = 0

for x in range (1, 5):
    print(f"-----{x}º PESSOA-----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("[M/F]: ")).strip().upper()
    somaidade += idade / 4
    if x == 1 and sexo in "M":
        nomehmaisvelho = nome
        maioridadeH = idade
    if sexo in "M" and idade > maioridadeH:
        maioridadeH = idade
        nomehmaisvelho = nome
    if sexo in "F" and idade < 20:
        menoridadeM += 1
    
print(f"A média de idade do grupo é de: {somaidade} anos")
print(f"O nome do homem mais velho é: {nomehmaisvelho} e ele tem {maioridadeH} anos")
print(f"Um total de {menoridadeM} mulheres tem menos que 20 anos.")


    
