# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia():
    lista = []

    for cont in range(0,5):
        lista.append(randint(0,99))

    return lista

def somaPar(lista):
    soma = 0

    for n in lista:
        if n % 2 == 0:
            soma += n

    return soma


#Programa Principal
numeros = sorteia() # Já inicia e sorteia uma lista com 5 numeros;

print(f"\nLista: {numeros}\nSoma dos Pares: {somaPar(numeros)}\n") # Imprimi a Lista e a Soma dos Pares já chamando a função de soma, que retorna o resultado;
