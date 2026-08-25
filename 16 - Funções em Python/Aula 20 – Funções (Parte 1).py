###############################################################

# Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.

###############################################################

def lin(): # Função de Mostrar Linha;
    print("="*40)


lin() # Chama a função e imprimi a linha;
print("         CADASTRO DE PRODUTOS          ")
lin()
###############################################################

def titulo(txt):
    print("="*40)
    print(txt)
    print("="*40)


titulo('         CADASTRO DE XXXXXXXX          ')

titulo('         CADASTRO DE YYYYYYYY          ')

titulo('         CADASTRO DE ZZZZZZZZ          ')

###############################################################

def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"Resultado = {s}")

def contador(*num): # * significa desempacotar
    print(num)
    tamanho = len(num) # Mostra o tamanho
    for v in num:
        print(v) # Mostra Valor por Valor


# a = 4
# b = 5
# s = a + b
# print(s) # 9
soma(4, 5) # Passo os valores para a função e ela executa;

soma(b=8, a=9) # Se for deixar explicito qual é qual, tem que ser os dois parametros!
# soma(b=8, 9) - O python não reconhece que só sobrou o A para o 9, da ERRO!

soma(2, 1) # Se não deixar explicito, o primeiro parametro vira A e o segundo B, conforme definido;

# soma(3,7,8) # Da erro pois a função foi definida para dois parametros;

# MASSSS... Empacotamento;

contador(4, 6, 8, 10, 12) # Cria uma Tupla = (4, 6, 8, 10, 12)
contador(8, 0) # Cria uma Tupla = (8, 0)
contador(6, 8, 7) # Cria uma Tupla = (6, 8, 7)

###############################################################

def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos +=1
        

valores = [7, 2, 5, 0, 4] # Lista de Valores;
dobra(valores) # Função para dobrar cada valor da lista;
print(valores) # [14, 4, 10, 0, 8]

###############################################################
