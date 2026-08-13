# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

p18 = homens = mulheres20 = 0
contP = 1

while True:
    next = sexo = ' '

    print(f"\nCadastro Pessoa {contP}:")
    idade = int(input("Digite a idade: "))
    while sexo not in 'MmFf':
        sexo = str(input("Digite o sexo[M/F]: ")).strip().upper()[0]

    print(f"\nPESSOA {contP} CADASTRADA!")
    contP += 1

    if idade > 18:
        p18 += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres20 += 1

    while next not in 'SsNn':
        next = str(input("\nDeseja Continuar[Sim/Não]: ")).strip().upper()[0]
    if next in 'Nn':
        break 

print(f"\nPessoas +18: {p18}\nHomens Cadastrados: {homens}\nMulheres -20: {mulheres20}\n")
