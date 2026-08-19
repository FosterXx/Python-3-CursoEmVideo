# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

estoque = (
    'Lápis', 1.75,
    'Lápis', 21.75,
    'Lápis', 121.75,
    'Lápis', 21.75,
    'Lápis', 121.75,
    'Lápis', 21.75,
    'Lápis', 121.75,
)

print("-"*33)
print("ESTOQUE".center(33))
print("-"*33)

for pos in range (0, len(estoque)):
    if pos % 2 == 0:
        print(f"{estoque[pos]:.<22}", end='')
    else:
        print(f"R$ {estoque[pos]:>8.2f}")

print("-"*33)
