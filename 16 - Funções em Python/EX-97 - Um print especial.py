# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(txt):
    tamanho = len(txt)

    print(f"~"*tamanho)
    print(f"{txt:^{tamanho}}")
    print(f"~"*tamanho)


escreva(str(input("Mensagem: ")))
