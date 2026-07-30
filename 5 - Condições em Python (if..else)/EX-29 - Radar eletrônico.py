# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

speed = int(input("Digite a velocidade do carro: ")) # Captura a velocidade.

if speed > 80: # Se estiver acima da velocidade maxima entra na condição simples.
   
    multa = float(speed - 80) * 7.0 # Calcula a multa.

    print(f"\nVocê foi multado!\nValor a Pagar: R$ {multa:.2f}\n") # Informa que foi multado e o valor.

print(f"\nSiga com segurança!\nVelocidade: {speed}Km/h\n") # Mensagem de praxe que sempre vai aparecer.
