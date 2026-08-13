# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000.
# C) Qual é o nome do produto mais barato.

contP = 1
totGasto = valorProdBarato = 0.0
prod1000 = 0
prodBarato = ''

while True:
    next = ' '

    print(f"\nCompra de Produto {contP}:\n")
    
    nome = str(input("Nome: ")).strip().title()
    valor = float(input("Preço: "))

    totGasto += valor

    if valor > 1000:
        prod1000 += 1

    if contP == 1 or valor < valorProdBarato:
        prodBarato = nome
        valorProdBarato = valor

    contP +=1

    while next not in 'SsNn':
        next = str(input("Deseja Continuar[S/N]:")).strip().upper()[0]

    if next in 'Nn':
        break

print(f"\nTotal Gasto: R$ {totGasto:.2f}\nProdutos +1000: {prod1000}\nProduto mais Barato: {prodBarato} - R$ {valorProdBarato:.2f}\n")
