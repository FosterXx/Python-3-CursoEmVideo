###############################################################

# if
# elif # Condição alinhada simples
# else

# if # Apenas pode usar um if
# elif
# elif # Pode usar quantos elif quiser mas precisa existir um if
# elif
# else # Pode usar um ou nenhum else

###############################################################

# Exemplos

nome = str(input("\nDigite seu nome: ")).title().strip()

if nome == 'Gustavo':
    print("\nQue nome bonito!\n")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Gabriel':
    print("\nSeu nome é bem popular no Brasil!\n")
else:
    print("\nSeu nome é comum!\n")
