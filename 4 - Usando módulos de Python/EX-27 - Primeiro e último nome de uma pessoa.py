# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Ultimo: Souza

nome = str(input("Digite seu nome completo: ")).strip().split()

print(f"Seu primeiro nome é: {nome[0]}")
print(f"Seu ultimo nome é: {nome[-1]}")
