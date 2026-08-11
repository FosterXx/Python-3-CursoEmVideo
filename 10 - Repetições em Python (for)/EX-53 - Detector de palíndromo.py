# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços [Exemplos: APOS O POHA, A SACADA DA CASA, O LOBO AMA O BOLO].

frase = str(input("Digite uma frase: ")).strip().upper() # Recebe a frase

palavras = frase.split() # Divide a frase em palavras

junto = ''.join(palavras) # junta as frases sem o espaço

inverso = junto[::-1] # Macete do fatiamento do Python para pegar a frase inversa;

# inverso = ''
# for letra in range(len(junto)-1,-1,-1): # Foi da ultima letra até a primeiro, voltando de 1 em 1;
#     inverso += junto[letra]

if inverso == junto: # Verificações
    print("\nTemos um Palíndromo!\n")
else:
    print("\nNão temos um Palíndromo!\n")

