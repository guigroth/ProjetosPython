print("{:=^30}".format(" GROTHSTORE "))
valorProduto = float(input("Digite o valor total de sua compra: R$"))
print('''Escolha seu método de pagamento: 
[ 1 ] À vista em dinheiro/cheque tem 10% de desconto
[ 2 ] À vista no cartão tem 5% de desconto
[ 3 ] Em até duas vezes no cartão (preço formal)
[ 4 ] 3x ou mais no cartão (20% de juros) ''')
opcao = int(input("Sua opção: "))
if opcao == 1:
   total = valorProduto - (valorProduto * 0.10)
elif opcao == 2:
  total = valorProduto - (valorProduto * 0.05)
elif opcao == 3:
    total = valorProduto
    print(f"A sua compra de R${valorProduto:.2f} parcelada em 2x irá custar: R${total / 2} cada parcela.")
elif opcao == 4:
   total = valorProduto + (valorProduto * 0.2)
   parcela = int(input("Quantas parcelas você deseja? ")) 
   totalParc = total / parcela
   print(f"A sua compra de R${valorProduto} parcelada em {parcela} vezes, será de R${totalParc:.2f}")
else:
    total = valorProduto
    print("OPÇÃO INVÁLIDA, DIGITE NOVAMENTE!")
print(f"Sua compra de RS${valorProduto:.2f}, no final irá custar: R${total:.2f}")