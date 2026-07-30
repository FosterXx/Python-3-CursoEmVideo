# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste ângulo.

from math import cos, sin, tan,radians

angulo = float(input("\nDigite um ângulo: "))

anguloRad = radians(angulo)

cosseno = cos(anguloRad)
seno = sin(anguloRad)
tangente = tan(anguloRad)

print(f"\nÂngulo: {angulo}°\nCosseno: {cosseno:.2f}\nSeno: {seno:.2f}\nTangente: {tangente:.2f}\n")