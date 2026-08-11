# Crie um programa que leia o ano de nascimento de sete pessoas. No final, encante quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

anoAtual = date.today().year

maiores = 0
menores = 0

for pessoas in range(1,8):
    anoNasc = int(input(f"Digite o ano de nascimento da {pessoas}° pessoa: "))

    if (anoAtual - anoNasc) >= 18:
        maiores += 1
    elif (anoAtual - anoNasc) < 18:
        menores += 1
    else:
        print("\nERROR\n")

print(f"Maiores: {maiores}")
print(f"Menores: {menores}")
