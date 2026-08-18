###############################################################

# Tuplas = Guarda até 4 valores;

# 4 valores em 4 indices = ( 0 , 1 , 2 , 3 )

# lanche = ('burguer','suco','pizza','pudim')

# # Fatiamento;
# print(lanche[0:3]) # ('burguer','suco','pizza')
# print(lanche[-1]) # ('pudim')
# print(lanche[1:]) # ('suco','pizza','pudim')
# print(lanche[-3]) # ('suco')

# # Ler os elementos da tupla;
# len(lanche) # 4 elementos

# # Percorrer todos os elementos da tupla;
# for c in lanche:
#     print(c)

###############################################################

# AS TUPLAS SÃO IMUTÁVEIS! Não tem como trocar o PUDIM por SORVETE!

lanche = ('Hamburguer','Suco','Pizza','Pudim','Batata Frita')

# for comida in lanche:
#     print(f"Eu vou comer {comida}!")

# Eu vou comer Hamburguer!
# Eu vou comer Suco!
# Eu vou comer Pizza!
# Eu vou comer Pudim!

# for cont in range(0, len(lanche)):
    # print(lanche[cont])

# Hamburguer cont = 0
# Suco cont = 1
# Pizza cont = 2
# Pudim cont = 3
# Batata Frita cont = 4

# for pos, comida in enumerate(lanche): # Enumerate pega o indice e o valor;
#     print(f"Vou comer {comida} na posição {pos}!")

# Vou comer Hamburguer na posição 0!
# Vou comer Suco na posição 1!
# Vou comer Pizza na posição 2!
# Vou comer Pudim na posição 3!
# Vou comer Batata Frita na posição 4!

###############################################################

# print(lanche)
# # ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# print(sorted(lanche))
# ['Batata Frita', 'Hamburguer', 'Pizza', 'Pudim', 'Suco'] # Transforma em uma lista para colocar em ordem

###############################################################

# a = (2, 5, 4)
# b = (5, 8, 1, 2)

# c = a + b # (2, 5, 4, 5, 8, 1, 2)
# c = b + a # (5, 8, 1, 2, 2, 5, 4)

# print(c.count(5)) # Quantas vezes apareceu o numero '5' na variavel c;

# print(c.index(8)) # Mostra o indice (posição) que está o numero '8'; Pega o primeiro valor que aparecer.

# print(c.index(5, 2)) # Começa a partir do indice 2; Deslocamento;

###############################################################

pessoa = ('Gustavo', 39, 'M', 86.55) # Recebe varios tipos de variaveis na Tupla;

print(pessoa)

# Não é possível fazer alterações na tupla como deletar um item da tupla, tipo pessoa[2], mas podemos deletar a tupla inteira;

print(pessoa)

###############################################################
