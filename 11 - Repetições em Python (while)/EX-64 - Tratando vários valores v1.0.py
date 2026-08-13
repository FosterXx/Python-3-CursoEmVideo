# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada (flag). No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = 0
soma = 0
num = 0

# Ouu

# cont = soma = num = 0

while num != 999:
    num = int(input("Digite um número [999 para PARAR]: "))

    if num == 999:
        break
    else:
        soma += num
        cont += 1

print(f"\nNumeros Digitados: {cont}\nSoma: {soma}\n")

###############################################################

# Professor;

# cont = soma = 0

# num = int(input("Digite um número [999 para PARAR]: "))

# while num != 999:
              
#     soma += num
#     cont += 1

#     num = int(input("Digite um número [999 para PARAR]: "))
              
# print(f"\nNumeros Digitados: {cont}\nSoma: {soma}\n")
