# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

valorProduto = float(input("Digite o valor do produto: R$ "))

print(f"\nAplicando 5% de desconto no produto que custa R$ {valorProduto:.2f} reais, o novo preço será R$ {(valorProduto * 0.95):.2f} reais.\n")