# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

num = float(input("Digite um numero: "))

print(f"\nO dobro de {num:.2f} é {(num*2):.2f}")
print(f"O triplo de {num:.2f} é {(num*3):.2f}")
print(f"A raiz quadrada de {num:.2f} é {(num**(1/2)):.2f}")