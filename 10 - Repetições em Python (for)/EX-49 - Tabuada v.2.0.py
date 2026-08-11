# Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print("=-="*20)

tabu = int(input("Digite a tabuada que deseja ver: "))

print("=-="*20)

for c in range(1,11):
    print(f"{tabu} x {c} = {tabu * c}")

print("=-="*20)
