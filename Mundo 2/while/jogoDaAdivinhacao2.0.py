from random import randint
numCPU = randint(0, 10)
tentativas = 0
acertou = False #Por padrão uma variável recebe True, então trocamos para false para manipula-la em seguida dento do laço.
while not acertou: # Mesmo que "while acertou == True"
    num = int(input("Digite um número novamente: "))
    tentativas += 1
    if num < numCPU:
        print("MAIOR... tente novamente")
    elif num > numCPU:
        print("MENOR... tente novamente")
    else:
        acertou == True 
        print(f"Você acertou, eu pensei no número {numCPU}, você tentou {tentativas} vezes até acertar.")