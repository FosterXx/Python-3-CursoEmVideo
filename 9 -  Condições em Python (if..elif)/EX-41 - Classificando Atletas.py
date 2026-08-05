# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos (mirim)
# até 14 anos (infantil)
# até 19 anos (júnior)
# até 25 anos (sênior)
# acima (master).

from datetime import date

nasc = int(input("\nDigite o ano que nasceu: "))

anoAtual = date.today().year

idade = anoAtual - nasc

if idade > 0 and idade <= 9:
    print(f"\nIdade: {idade}\nCategoria: Mirin\n")

elif idade > 9 and idade <= 14:
    print(f"\nIdade: {idade}\nCategoria: Infantil\n")

elif idade > 14 and idade <= 19:
    print(f"\nIdade: {idade}\nCategoria: Júnior\n")

elif idade > 19 and idade <= 25:
    print(f"\nIdade: {idade}\nCategoria: Sênior\n")

elif idade > 25:
    print(f"\nIdade: {idade}\nCategoria: Master\n")

else:
    print("\nERROR\n")
