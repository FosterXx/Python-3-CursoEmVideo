# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(anoNasc):
    from datetime import date # Importar para usar apenas na função em escopo Local;
    anoAtual = date.today().year

    idade = anoAtual - anoNasc

    if idade < 16:
        return f"\nVoto Negado\nIdade: {idade} anos\n"
    elif 16 <= idade < 18:
        return f"\nVoto Opcional\nIdade: {idade} anos\n"
    else:
        return f"\nVoto Obrigatório\nIdade: {idade} anos\n"


# Programa Principal;
ano = int(input("Digite seu ano de nascimento: "))

print(voto(ano))

# print(voto(int(input("Digite seu ano de nascimento: ")))) # Opção;
