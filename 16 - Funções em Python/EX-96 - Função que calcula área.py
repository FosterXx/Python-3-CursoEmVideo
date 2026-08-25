# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    area = largura * comprimento
    return area


print(F"\N{'CALCULO DE AREA - TERRENO':^40}")
print("="*40)
largura = float(input("Digite a largura: "))
comprimento = float(input("Digite a comprimento: "))

print(f"\nA área do terreno é de {area(largura, comprimento):.2f} m².\n")
