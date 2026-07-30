###############################################################

# Fatiando uma frase:

# frase = "Curso em Video Python"

# frase[9] # Imprimi apenas o caracter do indice 9.

# print(frase[9:14]) #Imprimi o caracter 9 até o 13 (conta o primeiro e exclui o ultimo indice)

# print(frase[9:21:2]) # imprimi do indice 9 até o indice 20 (:2 = Pulando de 2 em 2).

# print(frase[:5]) # Começa do indice 0 imprimindo do 0 até o 4.

# print(frase[15:]) # Começa do indice 15 até o final imprimindo do 15 até o 20.

# print(frase[9::3]) # Começa do indice 9 até o final imprimindo do 9 até o 20 enquanto pula de 3 em 3.

# ###############################################################

# # Analisar a string:

# len(frase) # Imprimi a quantidade de caracteries.

# frase.count('o') # Contar quantas vezes aparece a letra o (minuscula) na string.

# frase.count('o',0,13) # Contar quantas vezes aparece a letra o (minuscula) na string com fatiamento (do 0 até o 12).

# frase.find('deo') # Diz em qual momento encontrou "deo". ex: de 11,12 e 13, ele diz que encontrou em 11.
# frase.find('Android') # Quando não existir, ele retornará -1 que quer dizer que não foi encontrado!

# 'Curso' in frase # Se existir ele falará "True" que existe. Caso Contrario, False.

# ###############################################################

# # Metodos: # Obrigatorio o () no final de cada metodo.

# frase.replace('Python','Android') # Vai trocar a palavra "Python" pela palavra "Android".

# frase.upper() # Deixa tudo em maiusculo.

# frase.lower() # Deixa tudo em minusculo.

# frase.capitalize() # Deixa todos os caracteres para minusculo e a primeira letra para maiusculo.

# frase.title() # Analisa cada frase na string usando os espaços como quebra, coloca tudo em minusculo e deixa cada primeira letra de cada palavra maiusculo.

# # Ex: "   Aprenda Python  "
# frase.strip() # Remove os primeiros e ultimos espaços desnecessários.

# frase.rstrip() # "r" significa right e indica para remover apenas os espaços da direita.
# frase.lstrip() # "l" significa left e indica para remover apenas os espaços da esquerda.

# frase.split() # Faz uma divisão de cada palavra usando o espaço como divisor e gera uma lista com todas as palavras.
# '-'.join(frase) # Juntar todos os elementos de frase e entre cada palavra ele coloca um traço onde tinha o espaço (possivel colocar espaço no lugar do traço também).

###############################################################

#Testes:

frase = "Curso em Video Python"

print(frase[3])
print(frase[3:14])
print(frase[15:])
print(frase[:21:2])

print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designer'
s at Letraset and James Mosley, the librarian at St Bride Printing Library in London, took
a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets.""")
# Facilita para criar interfaces interativas usando o print(""" abc """)

print(frase.count('o')) 
print(frase.upper().count('O')) # Deixa tudo em maiusculo e conta o O maiusculo.

print(len(frase.strip())) # Mostra quantas caracteres temos em frase e o strip tira todos os espaços indesejados.

print(frase.replace('Python','Android')) # Imprimi ja alterando na hora - Temporario.

# frase = frase.replace('Python','Android') # Faz a alteração e sub-escreve salvando a nova versão na variavel - Definitivo.
# print(frase)

print('Curso' in frase) # Retorna True por 'Curso' estar em frase.
print(frase.find('Curso')) # Retorna indice 0, posição onde a palavra começa.
print(frase.find('curso')) # Retorna indice -1, porque não existe curso com minusculo na string.
print(frase.lower().find('curso')) # Retorna indice 0, posição onde a palavra começa pois toda a string foi toda transformada em minusculo.

dividido = frase.split() #Divide toda a frase e salva palavra por palavra em uma lista chamada 'dividido'.

print(dividido[2]) # Mostra a palavra que está no indice 2 (Video).
print(dividido[2] [3]) # Mostra caracter que está no indice 3 da palavra que está no indice 2.



