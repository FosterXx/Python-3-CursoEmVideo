# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

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

print(f"\nO valor final é: R$ {resul}\n")
