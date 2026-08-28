# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='', gols=0):

    global cont_ficha
    if nome == '':
        nome = f'Jogador {cont_ficha}'
        cont_ficha += 1

    print("~"*30)
    print(f"FICHA - {nome}".center(30))
    print("-"*30)
    print(f"\nNome do Jogador: {nome}")
    print(f"Total de Gols: {gols}")
    print("~"*30)
    

cont_ficha = 1 # Contador de Jogadores para a Função (ficha);

while True:
    while True:
        if not nome.isnumeric():
            nome = str(input("Registre seu Nome: ")).strip().title()
            break
        else:
            print("\nSistema não aceita números, por favor, tente novamente!\n")

    while True:
        try:
            totalGols = int(input("Registre seus Gols: "))
            break
        except:
            print("\nDigite um número INTEIRO (ex: 1, 2, 3..)!\n")

    ficha(nome, totalGols)

    while True:
        next = str(input("Gostaria de registrar um novo Jogador[Sim/Não]: ")).strip().upper()[0]
        if next in 'SsNn':
            break
    if next in 'Nn':
        break

    print()
