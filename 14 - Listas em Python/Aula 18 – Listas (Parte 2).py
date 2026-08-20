###############################################################

dados1 = ['Pedro',25]
dados2 = ['Maria',19]
dados3 = ['João',32]

pessoas = []

pessoas.append(dados1[:])
pessoas.append(dados2[:])
pessoas.append(dados3[:])

print(pessoas)
# [['Pedro',25], ['Maria',19], ['João',32]]

###############################################################

pessoas = [['Pedro',25], ['Maria',19], ['João',32]]

print(pessoas[0][0]) # Imprimi 'Pedro';
print(pessoas[1][1]) # Imprimi '19';
print(pessoas[2][0]) # Imprimi 'João';
print(pessoas[1]) # Imprimi '['Maria',19]'

###############################################################

teste = []
teste.append('Gustavo')
teste.append(40)
# ['Gustavo', 40] - teste

galera = []
galera.append(teste) # Criando uma ligação;
# ['Gustavo', 40] - galera
# ['Gustavo', 40] - teste

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
# ['Maria', 22], ['Maria', 22] - galera
# ['Maria', 22] - teste

# Como foi feito uma ligação, ao mudar a lista teste também muda a lista galera;

teste = []
teste.append('Gustavo')
teste.append(40)
# ['Gustavo', 40] - teste

galera = []
galera.append(teste[:]) # Com [:] copiamos todos os dados da lista teste para a lista galera;
# ['Gustavo', 40] - galera

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
# ['Gustavo', 40], ['Maria', 22] - galera
# ['Maria', 22] - teste

###############################################################

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] # 4 estruturas compostas em uma estrutura só;

print(f"galera[0]: {galera[0]}")
print(f"galera[1]: {galera[1]}")
print(f"galera[2][0]: {galera[2][0]}")
print(f"galera[2][1]: {galera[2][1]}")
print(f"galera[3]: {galera[3]}")

for p in galera:
    print(f"Nome: {p[0]} idade: {p[1]}")

###############################################################

galera = []
dado = []
maior = menor = 0

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))

    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade!")
        maior += 1
    else:
        print(f"{p[0]} é menor de idade!")
        menor -= 1

print(f"Maiores: {maior} - Menores: {menor}")
