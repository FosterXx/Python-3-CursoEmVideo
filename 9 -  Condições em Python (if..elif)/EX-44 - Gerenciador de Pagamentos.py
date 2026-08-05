# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de Desconto
# À vista no cartão: 5% de Desconto
# Em até 2x no cartão: Preço Normal
# 3x ou mais no cartão: 20% de Juros

print("=-="*25)
produto = float(input("\nDigite o valor do produto: "))
print("-"*75)

print("""
Selecione a forma de pagamento disponivel abaixo:

[1] Dinheiro/Cheque - À vista
[2] Cartão de Credito
""")

formaP = int(input("\nOpção: "))

if formaP == 1:
    valorPagar = produto * 0.95
    print(f"\nVocê receberá 5% de desconto!\nValor a Pagar: R$ {valorPagar:.2f}\n")

elif formaP == 2:
    parcela = int(input("\nDigite o numero de parcelas: "))

    if 0 < parcela <= 2:
        valorPagar = produto 
        print(f"\nValor a Pagar: {parcela}x de R$ {(valorPagar/parcela):.2f}\n")
    elif parcela > 2:
        valorPagar = produto * 1.20
        print(f"\n3x ou mais no cartão terá 20% de juros aplicada ao valor do produto!\nValor a Pagar: {parcela}x de R$ {(valorPagar/parcela):.2f}\n")

else: 
    print("\nError!\n")

print("=-="*25)


