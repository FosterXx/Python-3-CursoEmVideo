# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    tabuada = int(input("\nDigite a Tabuada: "))

    if tabuada < 0:
        break
    else:
        for c in range(1,11):
            print(f"{tabuada} x {c} = {tabuada * c}") 

print("\nPrograma Finalizado\n")
