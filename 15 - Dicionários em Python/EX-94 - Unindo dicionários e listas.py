# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) A média de idade;
# C) Uma lista com as mulheres;
# D) Uma lista de pessoas com idade acima da média;

pessoa = {}
pessoas = []

somaIdade = 0

print("=="*20)
print(f"{'Cadastro de Pessoa':^40}")
print("=="*20)

while True:
    pessoa.clear()

    pessoa['nome'] = str(input("Nome: ")).strip().title()

    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("ERROR! Digite M para Masculino ou F para Feminino!")

    pessoa['idade'] = int(input("Idade: "))
    somaIdade += pessoa['idade']

    pessoas.append(pessoa.copy())

    while True:
        next = str(input("Gostaria de Continuar[Sim/Não]: ")).strip().upper()[0]
        if next in 'NnSs':
            break
        print("ERROR! Digite Sim ou Não para continuar!")

    if next in 'Nn':
        print("\nFinalizando..\n")
        break

print("="*40)

print(f"\nA) Pessoas Cadastradas: {len(pessoas)}")

media = somaIdade / len(pessoas)
print(f"\nB) Média de Idade: {media:.2f} anos")

print("\nC) Mulheres Cadastradas: ", end='')
for v in pessoas:
    if v['sexo'] == 'F':
        print(f"{v['nome']}", end=' ')
print()

print("\nD)Pessoas Acima da Idade Media: ")
for v in pessoas:
    if v['idade'] > media:
        for k, v in v.items():
            print(f"{k} = {v};", end=' ')
        print()

print("\n<<<ENCERRADO>>>\n")
