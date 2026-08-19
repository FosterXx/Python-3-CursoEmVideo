# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []

while True:
    valor = float(input("\nDigite um valor para adicionar a lista: "))

    if valor in valores:
        print("Valor já registrado! Tente novamente!\n")
    else:
        valores.append(valor)
        print("\nValor Registrado!\n")

        next = str(input("\nGostaria de continuar adicionando [Sim/Não]: ")).strip().upper()[0]
        if next not in 'Ss':
            break

valores.sort()
print(f"\nLista: {valores}")

print("\nPrograma Finalizado!\n")
