###############################################################

# c = 1 

# while c !=10:
#     print(c)
#     c+=1

# print("Acabou")

###############################################################

# Usamos FOR quando sabemos quando começa e quando termina;
# for c in range(1,3):
#     n = int(input("Digite o numero: "))

# Usamos WHILE quando não sabemos quando termina;
# r = 'S'

# while r == 'S': # FLAG = Ponto de Parada, Condição de Parada
#     n = int(input("Digite o numero: "))
#     r = str(input("Quer continuar? [S/N] ")).strip().upper()

# print("Fim")

###############################################################

n = 1
par = 0
impar = 0

while n != 0:
    n = int(input("Digite o numero: "))

    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1


print(f"\nPar: {par}\nImpar: {impar}\n")

