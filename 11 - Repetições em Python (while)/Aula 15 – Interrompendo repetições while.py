num = soma = 0

while True:
    num = int(input("Digite um numero: "))    
    if num == 999:
        break # Flag
    soma += num


print(f"\nSoma: {soma}\n") # Usar esse F na string chama Fstring e é atual a partir do Python 3.6+;

# Obs - O .format é também mas do Python 3+;

#############################################################################################