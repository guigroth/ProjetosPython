cidade = str(input("Digite o nome da sua cidade natal: ")).strip()
print(f"O nome da sua cidade começa com Santo?: {cidade[:5].upper() == 'SANTO'}")