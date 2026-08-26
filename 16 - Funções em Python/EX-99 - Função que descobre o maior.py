# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    print(f"O maior valor é o número {max(*num)}!")


numList = []

while True:
    num = int(input("Digite um número: "))

    numList.append(num)

    while True:
        next = str(input("Deseja Continuar[Sim/Não]: ")).strip().upper()[0]
        if next in 'NnSs':
            break
    if next in 'Nn':
        break
print()

maior(numList)
