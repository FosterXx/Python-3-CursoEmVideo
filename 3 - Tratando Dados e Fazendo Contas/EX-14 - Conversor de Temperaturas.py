# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

celsius = float(input("\nDigite a temperatura em °C: "))

fahrenheit = (celsius * 1.8) + 32

print(f"\nA temperatura de {celsius:.2f} °C equivale a {fahrenheit:.2f} °F.\n")
