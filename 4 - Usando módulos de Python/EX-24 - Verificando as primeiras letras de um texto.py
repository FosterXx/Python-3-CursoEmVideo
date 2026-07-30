# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cid = str(input("Digite o nome de uma cidade: ")).strip().upper()

print(cid[:5] == "SANTO")
