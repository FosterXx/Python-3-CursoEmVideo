# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidadede notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

def notas(notas):

    notas_dicionario = {}

    notas_dicionario['quantidade_notas'] = len(notas)
    notas_dicionario['maior_nota'] = max(notas)
    notas_dicionario['menor_nota'] = min(notas)
    notas_dicionario['media_turma'] = sum(notas)/len(notas)

    while True:
        op = str(input("Deseja Incluir a Situação[Sim/Não]: ")).strip().upper()[0]
        if op in 'SsNn':
            break
    if op in 'Ss':
            if notas_dicionario['media_turma'] < 5:
                notas_dicionario['situacao'] = 'Ruim'

            elif 5 <= notas_dicionario['media_turma'] < 7:
                notas_dicionario['situacao'] = 'Razoavel'

            elif notas_dicionario['media_turma'] >= 7:
                notas_dicionario['situacao'] = 'Bom'
            return notas_dicionario

    return notas_dicionario


nota_list = []
while True:
    while True:
        try:
            nota = float(input("Nota: "))
            nota_list.append(nota)
            break
        except:
            print("Error! Digite um número valido!")

    while True:
        next = str(input("Deseja continuar adicionando notas[Sim/Não]: ")).strip().upper()[0]
        if next in 'SsNn':
            break
    if next in 'Nn':
        break

notas_turma = notas(nota_list)
print(notas_turma)
