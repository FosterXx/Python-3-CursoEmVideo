# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando R% 0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas.

distancia = int(input("\nDigite quantos km percorreu na viagem: ")) # recebe os km que percorreu

if distancia <= 200: # Se a distancia for até 200 km.
    passagem = distancia * 0.50 # Calcula passagem com 0,50 por Km.
else: # Se a distancia for maior que 200 km.
    passagem = distancia * 0.45 # Calcula passagem com 0,45 por Km.

print(f"\nObrigado pela viagem!\nPassagem: R$ {passagem:.2f}\n") # Imprimi na tela o valor da passagem.
