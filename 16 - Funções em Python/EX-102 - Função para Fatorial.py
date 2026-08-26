# fatorial() que receba dois parâmetros: o primeiro o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    --> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :param return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f" x ", end='' )
            else:
                print(f" = ", end='' )        
        f *= c
    
    return f


# Programa Principal;
print(fatorial(5, show=True)) # 5 x 4 x 3 x 2 x 1 = 120
print(fatorial(5, show=False)) # 120
print(fatorial(5)) # 120

help(fatorial)
# Help on function fatorial in module __main__:                                                                                                                                               

# fatorial(n, show=False)
#     --> Calcula o fatorial de um número.
#     :param n: O número a ser calculado.
#     :param show: (Opcional) Mostrar ou não a conta.
#     :param return: O valor do Fatorial de um número n.
