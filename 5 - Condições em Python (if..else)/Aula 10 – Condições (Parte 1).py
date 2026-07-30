###############################################################

# tempo = int(input("\nQuantos anos tem seu carro? "))

# if tempo <= 3:
#     print("Carro Novo")
# else: 
#     print("Carro Velho")

# # OU

# print("Carro Novo" if tempo >= 3 else "Carro Velho")

###############################################################

# Exemplos:

# nome = str(input("Digite seu nome: ")).strip().title()

# if nome == "Gabriel":
#     print("\nIgnácio?")
# else: 
#     print("\nAchei que te conhecia..")

# print(f"\nBom dia {nome}!\n")

###############################################################

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

print(f"\nA sua média é {media:.2f}")

# if media >= 6.0: # Condição Simples
#     print("\nParabens!")
# else:
#     print("\nEstude mais!")

# OU

print("Parabens!" if media >= 6 else "Estude mais!") # Condição Simplificada

###############################################################
