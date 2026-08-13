# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.

# saque = int(input("Digite do Saque: "))

# c50 = c20 = c10 = c1 = 0

# while saque > 0:

#     if saque >= 50:
#         c50 = saque // 50
#         saque = saque - 50 * c50

#     if saque >= 20:
#         c20 = saque // 20
#         saque = saque - 20 * c20

#     if saque >= 10:
#         c10 = saque // 10
#         saque = saque - 10 * c10

#     if saque >= 1:
#         c1 = saque // 1
#         saque = saque - 1 * c1

#     if saque == 0:
#         break
#     else:
#         print(f"\nResta: R${saque}\n")
# print(f"\nC50 = {c50}\n\nC20 = {c20}\n\nC10 = {c10}\n\nC1 = {c1}\n")

###############################################################

# Professor;

valor = int(input("Digite do Saque: "))

total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de {ced}!")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        totced = 0

        if total == 0:
            break
