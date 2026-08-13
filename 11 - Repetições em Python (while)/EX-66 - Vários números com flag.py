# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999. No final, mostre quantos números foram digitados e qual foi a soma entre eles (utilizando break para desconsiderar o flag).

soma = cont = num = 0

while True:
    num = int(input("Digite um número [999 para PARAR]: "))

    if num == 999:
        break
    else:
        soma += num
        cont += 1

print(f"\nNumeros Digitados: {cont}\nSoma: {soma}\n")
