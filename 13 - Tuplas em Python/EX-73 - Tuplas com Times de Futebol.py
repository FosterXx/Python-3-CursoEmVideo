# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense (ou outro time de sua escolha).

times = (
    'Palmeiras',
    'Flamengo',
    'Athletico-PR',
    'Fluminense',
    'Cruzeiro',
    'Bahia',
    'Red Bull Bragantino',
    'Atlético-MG',
    'Corinthians',
    'Coritiba',
    'Botafogo',
    'Vitória',
    'São Paulo',
    'Santos',
    'Grêmio',
    'Internacional',
    'Mirassol',
    'Remo',
    'Vasco',
    'Chapecoense',
)

print("\nA) Apenas os 5 primeiros colocados:")

for indice in range(0,5):
    print(f"{indice + 1}° - {times[indice]}")

print("\nB) Os últimos 4 colocados da tabela:")
for indice in range(-4,-0):
    print(f"{times.index(times[indice])+1}° - {times[indice]}")        

print("\nC) Uma lista com os times em ordem alfabética:")
for time in sorted(times):
    print(time)

print("\nD) Em que posição na tabela está o time da Chapecoense (ou outro time de sua escolha):")
print(f"A Chapecoense está em {times.index('Chapecoense')+1}° lugar na tabela - Indice {times.index('Chapecoense')}\n")

###############################################################

# Forma mais pratica:

# print(f"\nOs primeiros 5 colocados: {times[0:5]}")
# print("=-" * 25)
# print(f"\nOs ultimos 4 colocados: {times[-4:]}")
# print("=-" * 25)
# print(f"\nTimes em ordem alfabetica: {sorted(times)}")
# print("=-" * 25)
# print(f"\nA Chapecoense está em {times.index('Chapecoense')+1}° lugar na tabela - Indice {times.index('Chapecoense')}\n")

###############################################################
