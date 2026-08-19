###############################################################

lista = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lista)
# ['Hamburguer', 'Suco', 'Pizza', 'Pudim']

lista[3] = 'Picolé'
print(lista)
# ['Hamburguer', 'Suco', 'Pizza', 'Picolé']

# Diferença que Tuplas são imutaveis e Listas são mutaveis;

###############################################################

lista.append('Cookie') # Adicionar elemento - ultima posição;
# ['Hamburguer', 'Suco', 'Pizza', 'Picolé', 'Cookie']

lista.insert(0,'Hotdog') # Adicionar elemento em indice determinado;
# ['Hotdog', 'Hamburguer', 'Suco', 'Pizza', 'Picolé', 'Cookie']

del lista[3] # Deletar elemento;
lista.pop(3) # Pop geralmente remove o ultimo elemento, porém posso passar o indice determinado;
# lista.remove('Pizza') # Remove com base no elemento e não com o indice;
# ['Hotdog', 'Hamburguer', 'Suco', 'Picolé', 'Cookie']

lista.pop() # Remove o ultimo elemento;
# ['Hotdog', 'Hamburguer', 'Suco', 'Picolé']

if 'Pizza' in lista: # Verifica se o elemento Pizza está na lista e remove se True;
    lista.remove('Pizza') 

valores = list(range(4,11))
print(valores)
# [4, 5, 6, 7, 8, 9, 10]

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() # Organiza os valores;
# [0, 2, 3, 4, 5, 8, 9]

valores.sort(reverse=True) # Organiza os valores de forma reversa;
# [9, 8, 5, 4, 3, 2, 0]

len(valores) # Verifica quantos elementos existem na lista;
# 7

###############################################################

valores = []

for cont in range(1,4):
    valores.append(int(input(f"Digite o {cont}° valor: ")))

for i, v in enumerate(valores):
    print(f"No indice {i} encontrei o valor {v}..")

print("\nFim do Programa!\n")

listaA = [2, 3, 4, 7]
listaB = listaA

print(f"ListaA: {listaA}\nListaB: {listaB}")
# ListaA: [2, 3, 4, 7]
# ListaB: [2, 3, 4, 7]

listaB[2] = 8
print(f"ListaA: {listaA}\nListaB: {listaB}")
# ListaA: [2, 3, 8, 7]
# ListaB: [2, 3, 8, 7]

# Cria uma ligação entre os pedidos (listaB = listaA), se eu mudar listaB a listaA muda também;

listaB = listaA[:] # Joga todos os valores de A para B;
listaB[2] = 9
print(f"ListaA: {listaA}\nListaB: {listaB}")
# ListaA: [2, 3, 8, 7]
# ListaB: [2, 3, 9, 7]
