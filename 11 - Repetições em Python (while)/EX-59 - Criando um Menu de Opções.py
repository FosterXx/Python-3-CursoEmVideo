# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = float(input("\nDigite o 1° valor: ")) 
n2 = float(input("Digite o 2° valor: ")) 
sleep(1)

menu = True

while menu == True:
    print("="*30)
    print("""\nSelecione a Operação:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
""")
    op = int(input("Operação: "))

    if op == 1:
        soma = n1 + n2
        print(f"\n{n1} + {n2} = {soma}\n")

    elif op == 2:
        mult = n1 * n2
        print(f"\n{n1} x {n2} = {mult}\n")

    elif op == 3:
        if n1 > n2:
            print(f"\nO número {n1} é maior que o número {n2}!\n")
        elif n2 > n1:
            print(f"\nO número {n2} é maior que o número {n1}!\n")
        else:
            print(f"\nOs números são iguais!\n")

    elif op == 4:
        print("\nDigite Novamente:\n")
        n1 = float(input("Digite o 1° valor: ")) 
        n2 = float(input("Digite o 2° valor: "))
        print("\n")

    elif op == 5:
        menu = False
        print("\nSaindo do Menu..\n")

    else:
        print("\nPor gentileza, digite uma das opções apresentadas!\n")
sleep(1)
print("\nFIM\n")


