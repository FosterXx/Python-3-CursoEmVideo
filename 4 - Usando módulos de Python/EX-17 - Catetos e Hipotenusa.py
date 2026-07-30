# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimentoda hipotenusa.

from math import hypot

catetoOp = float(input("\nDigite o comprimento do cateto oposto: "))
catetoAd = float(input("Digite o comprimento do cateto adjacente: "))

hip = hypot(catetoOp, catetoAd) # Maneira com modulo hypot do math.
# hip = (catetoOp ** 2 + catetoAd ** 2) ** (1/2) # Maneira matematica.

print(f"\nCateto oposto: {catetoOp}\nCateto Adjacente: {catetoAd}\nHipotenusa: {hip:.2f}\n")
    