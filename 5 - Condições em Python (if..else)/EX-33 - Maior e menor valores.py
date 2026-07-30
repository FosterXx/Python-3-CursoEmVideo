# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Minha solução (leiga e trabalhosa):

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# if num1 > num2 and num1 > num3:
#     print(f"Maior: {num1:.2f}")
#     if num2 < num3:
#         print(f"Menor: {num2:.2f}")
#     else:
#         print(f"Menor: {num3:.2f}")

# elif num2 > num1 and num2 > num3: # Ele não tinha ensinado elif ainda kkk mas eu já conhecia e usei no automatico :b
#     print(f"Maior: {num2:.2f}")
#     if num1 < num3:
#         print(f"Menor: {num1:.2f}")
#     else:
#         print(f"Menor: {num3:.2f}")

# elif num3 > num1 and num3 > num2:
#     print(f"Maior: {num3:.2f}")
#     if num2 < num1:
#         print(f"Menor: {num2:.2f}")
#     else:
#         print(f"Menor: {num1:.2f}")

# elif num1 == num2 == num3:
#     print(f"São todos iguais! {num1:.2f} = {num2:.2f} = {num3:.2f}")

# else:
#     print("ERROR")

###############################################################

# Solução do professor Guanabara:

#Verificando quem é menor:

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

#Verificando quem é maior:

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f"Maior: {maior:.2f}")
print(f"Menor: {menor:.2f}")
