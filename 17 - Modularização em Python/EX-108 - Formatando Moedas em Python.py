# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda

valor = float(input("\nDigite o valor: R$ "))

print("""
1 - Aumentar
2 - Diminuir
3 - Dobrar
4 - Metade
""")
op = 0

while op not in range(1,4+1):
    op = int(input("Digite a opção: "))

    if op in range (1,2+1):
        taxa = float(input("\nDigite a taxa(ex: 50, 60 = %): "))
 
        if op == 1:
            resul = moeda.aumentar(valor, taxa)

        elif op == 2:
            resul = moeda.diminuir(valor, taxa)

    elif op == 3:
        resul = moeda.dobro(valor)

    elif op == 4:
        resul = moeda.metade(valor)

    else:
        print("\nDigite uma opção válida!\n")

resulFormatado = moeda.formatacao(resul)

print(f"\nO valor final é: {resulFormatado}\n")
