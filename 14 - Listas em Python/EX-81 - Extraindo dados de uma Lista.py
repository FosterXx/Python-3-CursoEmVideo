# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, faça um programa que mostre:
# Quantos números foram digitados.
# A lista de valores, ordenada de forma decrescente.
# Se o valor 5 foi digitado e está ou não na lista.

valores = []

while True:
    valor = float(input("\nDigite o valor: "))
    valores.append(valor)

    next = str(input("\nDeseja continuar[Sim/Não]: ")).strip().upper()[0]
    if next in 'Nn' or next not in 'SsNn':
        break
       
print(f"\nNumeros Registrados: {len(valores)}")

valores.sort(reverse=True)
print(f"Lista Ordenada Decrescente: {valores}")

if 5 in valores:
    print("O número 5 foi digitado e está na lista!\n")
else:
    print("O número 5 não foi digitado e não está na lista!\n")
