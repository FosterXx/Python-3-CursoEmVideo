# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

valor = float(input("\nDigite o valor: "))

print("""
1 - Somar
2 - Subtrair
3 - Dobrar
4 - Metade
""")
op = int(input("Digite a opção: "))

if op == 1:
    valorSoma = float(input("\nDigite o valor para somar: "))
    resul = moeda.somar(valor, valorSoma)

elif op == 2:
    valorSub = float(input("\nDigite o valor para subtrair: "))
    resul = moeda.subtrair(valor, valorSub)

elif op == 3:
    resul = moeda.dobro(valor)
             
elif op == 4:
    resul = moeda.metade(valor)

else:
    print("\nDigite uma opção válida!\n")

print(f"\nO valor final é: {resul}\n")
