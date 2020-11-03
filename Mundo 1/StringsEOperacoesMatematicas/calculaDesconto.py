precoProduto = float(input("Digite o preço do produto: "))
desconto = int(input("Digite a porcentagem de desconto: "))
prodComDesconto = precoProduto * desconto / 100
print(f"O produto que custava {precoProduto}, na promoção de {desconto}% de desconto, custará {prodComDesconto}R$")
