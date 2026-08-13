# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 → 1 → 1 → 2 → 3 → 5 → 8

termos = int(input("\nTermos: "))

cont = 3
t1 = 0
t2 = 1

print(f"\n{t1} > {t2}", end=' > ')

while cont <= termos:

    novo = t1 + t2

    print(novo, end=' > ')

    t1 = t2
    t2 = novo
    cont += 1

print("FIM")
