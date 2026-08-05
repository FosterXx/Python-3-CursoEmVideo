# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vCasa = float(input("\nDigite o valor da casa: R$ "))
salario = float(input("Digite seu salário mensal: R$ ")) # Recebe dados;
anosP = int(input("Digite em quantos anos vai pagar: "))

vPrestacao = vCasa / (anosP * 12) # Valor das prestações mensais;

limite = salario * 0.3 # Limite de 30% do salario;

if vPrestacao <= limite:
    print(f"\nEmpréstimo Aprovado!\nValor da Casa: R$ {vCasa:.2f}\nValor da Prestação: R$ {vPrestacao:.2f}\nMeses a Pagar: {anosP * 12}\n")

elif vPrestacao > limite:
    print(f"\nEmpréstimo Negado!\nA prestação de R$ {vPrestacao:.2f} excedeu o limite de 30% de seu salário de R$ {salario:.2f}\n")

else:
    print("\nERROR\n")
