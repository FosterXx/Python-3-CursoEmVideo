# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para Binário
# - 2 para Octal
# - 3 para hexadecimal

print("=-="*25)

num = int(input("\nDigite um número: "))
print("\nEscolha a base de conversão digitando as seguintes opções:\n") # Recebe dados e faz a interação com o usuário;
print("[1] - Base Binária\n[2] - Base Octal\n[3] - Base Hexadecimal\n")
base = int(input("Opção: "))

print("=-="*25)

if base == 1:
    print(f"\nO número {num} convertido para Binário é igual a {bin(num)[2:]}\n") # Coversão para Binário;

elif base == 2:
    print(f"\nO número {num} convertido para Octal é igual a {oct(num)[2:]}\n") # Coversão para Octal;

elif base == 3:
    print(f"\nO número {num} convertido para Hexadecimal é igual a {hex(num)[2:]}\n") # Coversão para Hexadecimal;
    
else:
    print("\nError\n") # Error padrão;

print("=-="*25)
