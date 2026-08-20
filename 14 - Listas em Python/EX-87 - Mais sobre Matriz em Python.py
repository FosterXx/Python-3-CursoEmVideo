# Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados.
# A soma dos valores da terceira coluna.
# O maior valor da segunda linha.

matriz = []
linha = []
pares = somaColuna = maiorLinha = 0

for l in range(0,3):
    for c in range(0,3):
        linha.append(int(input(f"Digite o valor da Linha[{l}] - Coluna [{c}]: ")))

    matriz.append(linha[:])
    linha.clear()

print("")

for l in range(0,3): # Percorre Todas as Linhas;
    for c in range(0,3): #Percorre Todos os Valores na Linha = Colunas;

        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c] # Soma os Pares da Matriz;

        if c == 2:
            somaColuna += matriz[l][c] # Soma a Terceira Coluna = Coluna[2];

        if l == 1 and matriz[l][c] > maiorLinha: 
            maiorLinha = matriz[l][c] # Registra o Maior Valor da Segunda Linha = Linha[1];

        print(f"[{matriz[l][c]:^5}]", end='') # Imprimi a Matriz;
    print()


print(f"\nSoma dos Pares: {pares}\nSoma Coluna[2]: {somaColuna}\nMaior Valor Linha[1]: {maiorLinha}\n") # Imprimi as Somas e o Maior Valor;
