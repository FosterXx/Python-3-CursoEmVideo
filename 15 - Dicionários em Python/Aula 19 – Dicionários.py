###############################################################

dados = dict() # Dicionario
dados = {'nome':'Pedro', 'idade':'25'} # Dicionario

print(dados['nome']) # Pedro 
print(dados['idade']) # 25

dados['sexo'] = 'M' # Adiciona um novo elemento SEXO no dicionario;

del dados['idade'] # Delete o elemento IDADE

###############################################################

filme1 = {
    'titulo':'Star Wars',
    'ano':'1977',
    'diretor':'George Lucas'
}

print(filme1.values()) # Retorna todos os valores do dicionario; ['Star Wars', '1977', 'George Lucas'];
print(filme1.keys()) # Retorna todas as chaves do dicionario; ['titulo', 'ano', 'diretor'];
print(filme1.items()) # Pega os dois; [('titulo', 'Star Wars'), ('ano', '1977'), ('diretor', 'George Lucas')]

for k, v in filme1.items():
    print(f"O {k} é {v}!")
    # O titulo é Star Wars!
    # O ano é 1977!
    # O diretor é George Lucas!

filme2 = {
    'titulo':'Avengers',
    'ano':'2012',
    'diretor':'Joss Whedon'
}

filme3 = {
    'titulo':'Matrix',
    'ano':'1999',
    'diretor':'Wachowski'
}

listaLocadora = [filme1, filme2, filme3] # Podemos armazenar DICIONARIOS dentro de LISTAS;

print(listaLocadora)
# [{'titulo': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}, {'titulo': 'Avengers', 'ano': '2012', 'diretor': 'Joss Whedon'}, {'titulo': 'Matrix', 'ano': '1999', 'diretor': 'Wachowski'}]

print(listaLocadora[0]['ano']) # 1977
print(listaLocadora[2]['titulo']) # Matrix

###############################################################

pessoas = {
    'nome':'Gustavo',
    'sexo':'M',
    'idade':22
}

print(pessoas) # {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome']) # Gustavo
print(pessoas['idade']) # 22

print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.") # O Gustavo tem 22 anos.

print(pessoas.keys()) # dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) # dict_values(['Gustavo', 'M', 22])
print(pessoas.items()) # dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])

for k in pessoas.keys():
    print(k)
    # nome
    # sexo
    # idade

for k in pessoas.values():
    print(k)
    # Gustavo
    # M
    # 22

for k, v in pessoas.items():
    print(f"{k} = {v}")
    # nome = Gustavo
    # sexo = M
    # idade = 22

pessoas['nome'] = 'Leandro'
del pessoas['idade']

for k, v in pessoas.items():
    print(f"{k} = {v}")
    # nome = Leandro
    # sexo = M

###############################################################

brasil = []

estado1 = {
    'uf':'Rio de Janeiro',
    'sigla':'RJ'
}
estado2 = {
    'uf':'São Paulo',
    'sigla':'SP'
}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
# [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]

print(brasil[0]['uf']) # Rio de Janeiro
print(brasil[1]['sigla']) # SP

###############################################################

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))

    brasil.append(estado.copy()) # opção .copy() pois não daria certo usar o [:] devido ao dicionario;

print(brasil)
# [{'uf': 'Minas', 'sigla': 'MG'}, {'uf': 'ACre', 'sigla': 'ac'}, {'uf': 'Amazonas', 'sigla': 'am'}]

for e in brasil: # Percorre a Lista;
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
        # O campo uf tem valor minas
        # O campo sigla tem valor m
        # O campo uf tem valor sao paulo
        # O campo sigla tem valor sp
        # O campo uf tem valor acre
        # O campo sigla tem valor ac
    for v in e.values():
        print(v, end='')
    print()
        # O campo uf tem valor Acre
        # O campo sigla tem valor AC
        # AcreAC
        # O campo uf tem valor Amazonas 
        # O campo sigla tem valor AM
        # AmazonasAM
        # O campo uf tem valor Para
        # O campo sigla tem valor PA
        # ParaPA
        