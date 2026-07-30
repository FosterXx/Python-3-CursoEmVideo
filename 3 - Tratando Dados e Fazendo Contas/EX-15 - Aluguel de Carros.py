# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por Km rodado.

rodagem = float(input("\nDigite quantos km o carrou rodou: "))
tempo = int(input("Digite quantos dias o carro ficou alugado: "))

aluguel = (rodagem * 0.15) + (tempo * 60)

print(f"\nO carro ficou {tempo} dia(s) alugado e percorreu {rodagem} km, sendo assim, o valor total a pagar será de R$ {aluguel:.2f}\n")
