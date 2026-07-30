# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1.00 = R$ 3.27

real = float(input("Digite o valor em reais(ex: R$ 2705.57): R$ "))

dolar = real / 3.27

print(f"\nCom R$ {real} reais você pode comprar US$ {dolar:.2f} dólares.\n")
