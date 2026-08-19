# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = (
    'Correr',
    'Voar',
    'Nadar',
    'Viver',
    'Morrer',
    'Assistir',
    'Faculdade',
)

for p in palavras:
    print(f"\nA palavra '{p.upper()}' possui as vogais:", end=' ')

    for letra in p:
        if letra in "AaEeIiOoUu":
            print(f"{(letra).lower()}", end=' ')

print("\n\nPrograma Finalizado!\n")
