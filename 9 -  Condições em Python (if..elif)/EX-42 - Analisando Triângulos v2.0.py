# Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
# Equilátero: Todos os lados iguais.
# Isósceles: Dois lados iguais.
# Escaleno: Todos os lados diferentes.

print("=-="*25)
r1 = float(input("Primeira segmento: "))
r2 = float(input("Segunda segmento: "))
r3 = float(input("Terceira segmento: "))
print("=-="*25)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("\nPodem formar um triângulo!")

    if r1 == r2 == r3:
        print("\nSerá um triângulo Equilátero - Todos os lados iguais!\n")
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print("\nSerá um triângulo Isósceles - Dois lados iguais!\n")
    elif r1 != r2 != r3 != r1:
        print("\nSerá um triângulo Escaleno - Todos os lados diferentes!\n")

else:
    print("\nNão podem formar um triângulo")

print("=-="*25)
