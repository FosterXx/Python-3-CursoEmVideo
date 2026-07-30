# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex:
# Digite um numero: 1834
# Unidade: 4 Dezena: 3 Centena: 8 Milhar: 1

num = int(input("Digite um numero de 0 a 9999: ")).strip()

numU = num // 1 % 10 # Exemplo: 1212 divisão inteira por 1 = 1212 resto de divisão por 10 (1212 / 10 = sobra 2).
numD = num // 10 % 10 # Exemplo: 1212 divisão inteira por 10 = 121 resto de divisão por 10 (121 / 10 = sobra 1).
numC = num // 100 % 10 # Exemplo: 1212 divisão inteira por 100 = 12 resto de divisão por 10 (12 / 10 = sobra 2).
numM = num // 1000 % 10 # Exemplo: 1212 divisão inteira por 1000 = 1 resto de divisão por 10 (1 / 10 = sobra 1).
                        # Exemplo²: 212 divisão inteira por 1000 = 0 resto de divisão por 10 (0 / 10 = sobra 0).

print(f"\nUnidades: {numU}\n\nDezenas: {numD}\n\nCentenas: {numC}\n\nMilhares: {numM}\n")
