# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m = float(input("Digite um valor em metros (ex: 2.50): "))

cm = m * 100
mm = m * 1000

print(f"\nMetros: {m}\nCentimetros: {cm}\nMilimetros: {mm}")