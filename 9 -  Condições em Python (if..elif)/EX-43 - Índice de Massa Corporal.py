# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela:
# Abaixo de 18.5; Abaixo do Peso
# Entre 18.5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
print("=-="*25)
print("CALCULADOR IMC")
print("=-="*25)

peso = float(input("\nDigite seu peso em KG (Ex: 88.9): "))
altura = float(input("Digite sua altura em metros(Ex: 1.79): "))

imc = peso / (altura **2)

if imc > 0 and imc < 18.5:
    print(f"\nAbaixo do Peso! IMC: {imc:.2f}\n")

elif imc >= 18.5 and imc < 25:
    print(f"\nPeso Ideal! IMC: {imc:.2f}\n")

# opção: elif 18.5 <= imc < 25 # Serve e fica mais otimizado;

elif imc >= 25 and imc < 30:
    print(f"\nSobrepeso! IMC: {imc:.2f}\n")

elif imc >= 30 and imc < 40:
    print(f"\nObesidade! IMC: {imc:.2f}\n")

elif imc >= 40:
    print(f"\nObesidade Mórbida! IMC: {imc:.2f}\n")

else:
    print("\nError!\n")

print("=-="*25)