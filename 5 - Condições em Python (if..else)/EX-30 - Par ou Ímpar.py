# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = int(input("Digite um numero inteiro: ")) # Recebe o numero

if num % 2 == 0: # Se o resto de divisão for 0.
    print(f"\nO numero {num} é PAR!\n") # Imprimi que o numero é Par.
else: # Se o resto de divisão não for 0.
    print(f"\nO numero {num} é IMPAR!\n") # Imprimi que o numero é Impar.
