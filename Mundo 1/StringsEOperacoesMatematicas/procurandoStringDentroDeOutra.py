""" nome = str(input("Digite seu nome: ")).strip()
contem = nome.upper().find("Silva")
print(f"O seu nome contém Silva? {bool(contem)}") """

nome = str(input("Digite seu nome: ")).strip()
print(f"O seu nome contém Silva? {'SILVA' in nome.upper()}")