medida = float(input("Digite uma quantidade em metros: "))
print(f"""{medida} Metros equivalem a:
{medida / 10} decâmetro,
{medida / 100} hectômetro,
{medida / 1000} quilômetros,
{medida * 10:.0f} decímetros,
{medida * 100:.0f} centímetro(s)
{medida * 1000:.0f} milímetros,""")
