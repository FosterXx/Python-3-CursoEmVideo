# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input("\nDigite seu ano de nascimento: "))

anoAtual = date.today().year

idade = anoAtual - nasc

if idade < 18:
    print(f"\nVocê pode se alistar no serviço militar em {18 - idade} anos.\n")

elif idade == 18:
    print("\nVocê precisa se alistar ao serviço militar neste ano!\n")

elif idade > 18:
    print(f"\nVocê deveria ter se alistado no serviço militar a {idade - 18} anos atras.\n")

else:
    print("\nERROR\n")
