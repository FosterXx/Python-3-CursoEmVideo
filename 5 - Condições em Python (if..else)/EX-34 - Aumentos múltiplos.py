# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%.

salario = float(input("\nDigite seu salario(Ex: 1250): R$ "))

if salario > 1250:
    salarioR = salario * 1.10
else:
    salarioR = salario * 1.15

print(f"Seu salário com o aumento será de R$ {salarioR:.2f}") # Eu usaria um elif e colocaria um print exclusivo para 10% e para 15%, mas vou me abster.
