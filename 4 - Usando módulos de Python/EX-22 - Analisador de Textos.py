# Crie um programa que leia um nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiusculas e minusculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ").strip()

# Nome Maiusculo:
print(f"Seu nome em maiusculo é: {nome.upper()}")

# Nome Minusculo:
print(f"Seu nome em minusculo é: {nome.lower()}")

# Quantidade de letras:
print(f"Seu nome completo tem {len(nome.replace(' ',''))} letras.")

# Quantidade de letras primeiro nome:
print(f"Seu primeiro nome tem {len(nome.split()[0])} letras.")
