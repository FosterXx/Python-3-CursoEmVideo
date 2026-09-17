###############################################################

# def fatorial(n):
#     f = 1
#     for c in range(1,n+1):
#         f *= c
#     return f

# def dobro(n):       # Codigo vai ficando muito grande;
#     return n*2      # Criar um modelo e enviar as def para "uteis.py"

# def triplo(n):
#     return n*3

# from uteis import fatorial, dobro # Possível também, mas não indicado;
from uteis import numeros# 

num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}!")

# Isso foi um exemplo de modulos;

###############################################################

# PACOTES

# Se no modulo uteis tiver muitas funções, dificulta a ideia de uma melhor organização, ai que vem a junção de modulos separados por assunto, um PACOTE.
# Detro de um pacote, podemos ter funções relacionadas a numeros, datas, strings, cores, dentre outros.
# Para isso, criamos pastas como por exemplo Uteis(pacote) -> cores(pacote) -> __init__.py (necessario ter este nome)


# Parei em 25:57, considerar uns 24:30 e rever.
