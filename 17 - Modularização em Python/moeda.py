def aumentar(valor, taxa):
    res = valor + (valor * taxa/100)
    return res

def diminuir(valor, taxa):
    res = valor - (valor * taxa/100)
    return res

def dobro(valor):
    res = valor * 2
    return res

def metade(valor):
    res = valor / 2
    return res

def formatacao(valor):
    valorFormatado = "R$ " + str(round(valor,2)).replace(".",",")
    return valorFormatado
