# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = []
linha = []

for l in range(0,3):
    for c in range(0,3):
        linha.append(int(input(f"Digite o valor da Linha[{l}] - Coluna [{c}]: ")))

    matriz.append(linha[:])
    linha.clear()

print("")

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
    
print("\nFIM\n")
