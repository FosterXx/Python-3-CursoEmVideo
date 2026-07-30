###############################################################

# +  Adição
# -  Subtração
# *  Multiplicação
# /  Divisão
# %  Resto de Divisão (5 // 2 é igual a 2 e sobra 1, esse é o resto de divisão)
# **  Potencia
# //  Divisão Inteira (Dividir sem usar a virgula - ex: 5 // 2 é igual a 2)
# == Igual a

###############################################################

# Ordem de Precedencia - mais importante

# ()
# **
# * / // %
# + -

###############################################################

# Exemplos:

# 5 + 3 * 2
# 5 + 6
# 11

# 3 * 5 + 4**2
# 3 * 5 + 16
# 15 + 16 
# 16

# 3 * (5 + 4)**2
# 3 * (9)**2
# 3 * 81
# 243

# 81 ** (1/2) - Raiz Quadrada
# 9

# "Olá" * 5
# OláOláOláOláOlá

# print("="*20)
# ====================

###############################################################

# Não é operadores aritmetricos, apenas uma funcionalidade do Py

# nome = input("Digite seu nome: ")

# print(f"Seja bem vindo {nome:20}!")
# Seja bem vindo IG                  !

# print(f"Seja bem vindo {nome:^20}!")
# Seja bem vindo          IG         !

# print(f"Seja bem vindo {nome:>20}!") ## ou < para oposto
# Seja bem vindo                   IG!

# print(f"Seja bem vindo {nome:=^20}!")
# Seja bem vindo =========IG=========!

###############################################################

# n1 = int(input("Digite o n1: "))
# n2 = int(input("Digite o n2: "))

# # print(f"A soma é {n1+n2}") # Para casos que não vou usar a soma em outros momentos. Para caso precise futuramente, usar variaveis.

# soma = n1 + n2
# mult = n1 * n2
# div = n1 / n2
# divInt = n1 // n2
# pot = n1 ** n2

# print(f"A soma é {soma} - A multiplicação é {mult} - A divisão é {div:.2f}", end=" ") # :.2f é com dois pontos flutuantes (ex: 1,33 inves de 1,333333333333)
# print(f"- A divisão inteira é {divInt} - A potência é {pot}") # Com o end=" " no final da linha de cima, vai emendar o primeiro print e o segundo sem quebrar linha.
# print("Agradeço por aparecer!\nAté a proxima!") # Diferente do \n que força uma quebra de linha

###############################################################



