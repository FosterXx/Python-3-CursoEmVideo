# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input("Digite o numero[0 a 20]: "))

        if 0 <= num <= 20:
            print(f"\nO numero {num} em exterso é {numeros[num]}!\n")
            break

        else:    
            print("Tente Novamente!", end=' ')

    next = str(input("Você gostaria e continuar[Sim/Não]: ")).strip().upper()[0]

    if next in 'Nn':
        break

print("\nFim do Programa!\n")
