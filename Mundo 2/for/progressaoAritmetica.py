priTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = priTermo + (11 - 1) * razao # Fórmula do Enésimo Número (P.A), O 10 DENTRO DO PARÊNTESES APENAS REPRESENTA A QUANTIDADE DE ELEMENTOS QUE SERÃO MOSTRADOS.
for x in range(priTermo, decimo, razao):
    print(f"{x}", end=' -> ')
print("ACABOU") 