# Leia nome, média e situação (Aprovado/Reprovado) de um aluno e armazene em um dicionário, exibindo o resultado final.

alunos = {}

alunos['nome'] = str(input("Nome: "))
alunos['media'] = float(input(f"Média de {alunos['nome']}: "))

if alunos['media'] >= 7:
    alunos['situacao'] = 'Aprovado'
else:
    alunos['situacao'] = 'Reprovado'


print(f"\nNome: {alunos['nome']}\nMédia: {alunos['media']}\nSituação: {alunos['situacao']}\n")
