# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior;
# O segundo valor é maior;
# Não existe valor maior, os dois são iguais;

num1 = int(input("Digite o numero A: ")) # Entrada de Dados;
num2 = int(input("Digite o numero B: "))

if num1 > num2:
    print("\nO valor A é maior!\n")

elif num1 < num2:
    print("\nO valor B é maior!\n") # Comparações e Mensagens Correspondentes;

elif num1 == num2:
    print("\nNão existe valor maior, os valores A e B são iguais!\n")

else:
    print("\nERROR\n") # Error Padrão
