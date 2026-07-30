###############################################################

# ANSI para cores = escape sequence

# \033[(style) (text) (back)m # Codigo para aplicar cores e estilos ao Python


# Codigos de Style que melhor funcionam para python:

# 0 = None # Sem nada
# 1 = Bold # Negrito
# 4 = Underline # Sublinhado
# 7 = Negative # Inverter as configurações (Oque colocou para Fundo vai para Letra e vice-versa)

# Codigos de Cores para Text:

# 30 = Branco
# 31 = Vermelho
# 32 = Verde
# 33 = Amarelo
# 34 = Azul
# 35 = Magenta
# 36 = Ciano
# 37 = Cinza

# Para colocar mais cores precisa de biblioteca e modulos.

# Codigos de Cores para Background:

# 40 = Branco
# 41 = Vermelho
# 42 = Verde
# 43 = Amarelo
# 44 = Azul
# 45 = Magenta
# 46 = Ciano
# 47 = Cinza

###############################################################

nome = 'Gabriel'

cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretobranco':'\033[7;30m',
}

print(f"{cores['azul']}Boa tarde {cores['amarelo']}{nome}{cores['limpa']}")
print(f"{cores['azul']}Como vai?\n{cores['limpa']}")
