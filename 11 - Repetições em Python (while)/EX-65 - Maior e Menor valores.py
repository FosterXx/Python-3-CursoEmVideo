# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# num = int(input("\nDigite um valor inteiro: "))

# soma = maior = menor = num

# next = 'S'
# cont = 1

# while next in 'Ss':

#     num = int(input("\nDigite um valor inteiro: "))
    
#     soma += num
#     cont +=1
    
#     if num > maior:
#         maior = num
#     elif num < menor:
#         menor = num

#     if cont >= 2:
#         next = str(input("\nDeseja continuar a digitar valores? ")).upper().strip()[0]

# media = soma / cont

# print(f"\nMedia dos Numeros: {media}\nMaior Numero: {maior}\nMenor Numero: {menor}\n")


#############################################################################################

# Professor;

resp = 'S'

soma = cont = maior = menor = 0

while resp in 'Ss':
    num = int(input("\nDigite um número: "))
    soma += num
    cont += 1

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    
    resp = str(input("\nDeseja Continuar? [S/N] ")).upper().strip()[0]

media = soma / cont

print(f"\nMedia dos Numeros: {media}\nMaior Numero: {maior}\nMenor Numero: {menor}\n")
 