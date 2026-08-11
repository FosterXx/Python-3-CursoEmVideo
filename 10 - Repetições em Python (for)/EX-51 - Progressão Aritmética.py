# Leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão, usando a estrutura for.

print("<>"*20)

print("\n          10 TERMOS DE UMA PA\n")

print("<>"*20)

primeiro = int(input("\nDigite o primeiro termo: "))
razao = int(input("\nDigite a razão: "))

ultimo = primeiro + (10 - 1) * razao # Formula do 10° Termo;

for c in range(primeiro,ultimo + razao,razao):
    print(c, end=' > ')

print("FIM\n")

print("<>"*20)