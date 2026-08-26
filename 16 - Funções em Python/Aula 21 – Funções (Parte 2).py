###############################################################
# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.
###############################################################
##Interactive Help

# help(print);

# terminal --> digitar (Python) --> digitar (help()) e testar os comandos;

# print(print.__doc__);

###############################################################
##Docstrings

from time import sleep # Importa a função de alguma biblioteca;

def contador(i, f, p):
    # Essas três aspas duplas abrem uma docstring que ao dar o comando help(a função aqui) ele aparece ensinando oque é cada termo; 
    """
    --> Faz uma contagem e mostra na tela.
    :parametro i: início da contagem
    :parametro f: fim da contagem
    :parametro p: passo da contagem
    :return: sem retorno
    Função criada por Gabriel Ignácio Aprendendo Docstrings;
    """
    c = 0
    while c <= f:
        print(f"{c} ", end='')
        c += p
    print("FIM!")


help(contador)

###############################################################
##Argumentos Opcionais

# Colocar =0 como por exemplo está nos parametros, os transforma em parametros opcionais. Se a função receber 2 valores (A e B) o sistema vai considerar o C como 0;
def somar(a=0, b=0, c=0):
    """
    --> Faz a soma de três valores e mostra na tela.
    :parametro a: o primeiro valor
    :parametro b: o segundo valor
    :parametro c: o tereiro valor
    Função criada por Gabriel Ignácio Aprendendo Docstrings;
    """
    s = a + b + c
    print(f"A soma vale {s}")


somar(c=4, a=2)

###############################################################
##Escopo de Variáveis

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ A variavel n é Global, funciona em todo o escopo; escopo Global;
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ A variavel x é Local, neste caso, só funciona dentro da função; escopo Local;
def teste():
    x = 8
    print(f"Função Teste: n vale {n}") # 2
    print(f"Função Teste: x vale {x}") # 8
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ A variavel x é Local, neste caso, só funciona dentro da função; escopo Local;


# Programa principal
n = 2
print(f"Programa Principal: {n}") # 2
# print(f"Programa Principal: {x}") # Error
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ A variavel n é Global, funciona em todo o escopo; escopo Global;

# --------------------------------------------------------------

# No caso de ter uma variavel a = 2 em escopo local e uma variavel a = 4 no escopo global, os valores são diferentes e usados cada um em seu escopo;

def funcao():
    k = 4
    print(f"k em Local vale {k}") # 4


# Programa principal
k = 2
print(f"k em Global vale {k}") # 2
# --------------------------------------------------------------

# Podemos pedir para utilizar o valor da variavel Global 'A' dentro de um escopo Local, inves de criar uma variavel 'A' Local

def funcao():
    global j
    print(f"j em Local mas usando variavel global vale {j}") #2


# Programa principal
j = 2
print(f"j em Global vale {j}") # 2

###############################################################
##Retorno de Valores

def somar(a=0, b=0, c=0):

    s = a + b + c

    return s # Envia apenas o valor de 'S';


# Programa Principal
r1 = somar(3, 2, 5) 
r2 = somar(2, 2) # Guarda os valores em uma variável;
r3 = somar(4)

print(somar(3, 2, 5)) # Ou podemos usar um print para já imprimir e/ou usar da maneira que preferir;

# --------------------------------------------------------------

def par(n=0):
    if n % 2 == 0:
        return True # Verdadeiro se for PAR;
    else:
        return False # Falso se for IMPAR;


num = int(input("Digite um Numero: "))
if (par(num)):
    print("É PAR!")
else:
    print("É IMPAR!")

###############################################################
