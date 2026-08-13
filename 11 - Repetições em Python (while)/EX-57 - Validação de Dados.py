# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
print("="*35)

# while sexo != 'M' and sexo != 'F':
#     sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper() # Maneira que fiz;

# Usando 'not in':
while sexo not in ('M','F'): # Posso fazer 'MmFf' que ele testa todas as letras;
    sexo = str(input("Dados Invalidos!\nDigite seu sexo [M/F]: ")).strip().upper()[0] # [0] = Pega apenas a primeira letra;

    print("="*35)

print(f"\nSexo {sexo} Registrado com sucesso!\n")

