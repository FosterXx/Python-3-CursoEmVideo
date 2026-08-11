# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
for c in range(3,500,3):
    if c % 2 != 0:
        soma += c
    else:
        pass
print(f"\nA soma de todos os numeros impares e multiplos de três é: {soma}\n")

