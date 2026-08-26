# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import date

def voto(anoNasc):
    anoAtual = date.today().year

    idade = anoAtual - anoNasc

    return



# Programa Principal;
ano = int(input("Digite seu ano de nascimento: "))

voto(ano)