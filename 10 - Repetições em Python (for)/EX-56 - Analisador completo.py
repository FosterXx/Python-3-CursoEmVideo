# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho, e quantas mulheres têm menos de 20 anos.

print("="*16)

# Inicializa a variavel da MEDIA de idade;
media = 0.0

# Incializa variaveis para a IDADE e NOME do homem mais velho;
nomeH = ''
idadeH = 0.0

# Inicializa variavel de CONTAGEM das mulheres com < 20 anos;
contM = 0

for pessoa in range(1,5):
    nome = str(input("Nome: ")).title().strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    print("="*16)

    # Soma as idades para a MEDIA;
    media += idade

    # Verifica o homem mais velho e registra seu NOME e IDADE;
    if sexo == 'M' and idadeH == 0.0:
        idadeH = idade
        nomeH = nome
    elif sexo == 'M' and idadeH < idade:
        idadeH = idade
        nomeH = nome

    # Verifica se é mulher com menos de 20 anos e registra a CONTAGEM;
    if sexo == 'F' and idade < 20:
        contM += 1

# Calcula MEDIA de idade do grupo;
media = media / 4

# Saida de dados;
print(f"\nMedia de Idade do Grupo: {media:.2f} anos\nHomem mais Velho: {nomeH} com {idadeH} anos\nMulheres com Menos de 20 Anos: {contM}")
