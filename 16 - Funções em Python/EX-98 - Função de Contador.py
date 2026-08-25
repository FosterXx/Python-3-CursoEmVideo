# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# De 1 até 10, de 1 em 1.
# De 10 até 0, de 2 em 2.
# Uma contagem personalizada.

from time import sleep

def contador(inicio, fim, passo):
    print("~"*25)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont} ", end='', flush=True)
            sleep(.5)
            cont += passo
        print("FIM")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ", end='', flush=True)
            sleep(.5)
            cont -= passo
        print("FIM")


contador(1, 10, 1)
contador(10, 0, 2)

print("~"*25)

print("\nAgora é sua vez, defina os parametros para uma contagem personalizada:")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio,fim,passo)
