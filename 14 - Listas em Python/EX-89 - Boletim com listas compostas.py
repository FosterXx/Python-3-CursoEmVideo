# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from time import sleep

boletins = []
aluno = []
cadastrado = False

while True:
    nome = str(input("Digite o Nome do Aluno: ")).strip().title()

    for a in boletins:
        if a[0] == nome:
            cadastrado = True
            break

    if cadastrado == False:
        n1 = float(input("Digite a N1: "))
        n2 = float(input("Digite a N2: "))

        aluno.append(nome)
        aluno.append(n1)
        aluno.append(n2)

        boletins.append(aluno[:])
        aluno.clear()
        print("\nCadastro Realizado!\n")

    else:
        print("\nAluno Já Cadastrado!\n")

    next = str(input("Deseja Continuar[Sim/Não]: ")).strip().upper()[0]
    if next not in 'SN' or next in 'N':
        break

print("\n")
sleep(.5)
print("=+="*20)
for a in boletins:
    print(f"BOLETIM - {a[0]}".center(60))
    print("-"*60)

    media = (a[1] + a[2]) / 2

    print(f"\nMédia Final: {media:.2f}\n")

    sleep(.5)

    notasVer = str(input(f"Deseja ver as notas do aluno {a[0]}[Sim/Não]: ")).strip().upper()[0]

    sleep(.5)

    if notasVer in 'S':
        print(f"\nN1 = {a[1]}")
        print(f"N2 = {a[2]}\n")

    sleep(1)
    print("=+="*20)

###############################################################

# PROFESSOR

ficha = []

while True:
    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))

    media = (n1 + n2) / 2

    ficha.append([nome, {n1, n2}, media])

    resp = str(input("Quer continuar? [S/N] "))
    if resp in 'Nn':
        break

print("-="*30)
print(f"{"No.":<4}{"NOME":<10}{"MÉDIA":>8}")
print("-"*26)

for i, a in enumerate(ficha):
    print(f"`{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print("-"*35)
    opc = int(input("Mostrar notas de qual aluno? [999 interrompe]: "))

    if opc == 999:
        print("FINALIZANDO...")
        break

    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")

print("<<< VOLTE SEMPRE >>>")
