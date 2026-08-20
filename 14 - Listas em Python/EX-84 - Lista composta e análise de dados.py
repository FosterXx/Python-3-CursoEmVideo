# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas.
# Uma listagem com as pessoas mais pesadas.
# Uma listagem com as pessoas mais leves.

pessoas = []
dado = []
contP = mai = men = 0

while True:
    dado.append(str(input("Digite o nome: ")).strip().title()) 
    dado.append(float(input("Digite o peso: ")))

    if len(pessoas) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]

    pessoas.append(dado[:])
    dado.clear()
    contP += 1

    next = str(input("Deseja Continuar[Sim/Nao]: ")).strip()[0]
    if next not in 'SsNn' or next in 'Nn':
        break

print(f"\nPessoas Cadastradas: {contP}")

print(f"Maior Peso: {mai}KG - ", end='')
for p in pessoas:
    if p[1] == mai:
        print(f"[{p[0]}] ", end='')

print(f"\nMenor Peso: {men}KG - ", end='')
for p in pessoas:  
    if p[1] == men:
        print(f"[{p[0]}] ", end='')
