# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

# Solução do Professor;
# def leiaInt(msg):
#     ok = False
#     valor = 0

#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print("\033[0;31mERROR!Digite um número inteiro valido!\033[m")

#         if ok:
#             break

#     return valor

# Minha Solução;
def leiaInt(msg): # Recebe "Digite um numero: "

    while True: # Loop;
        n = input(msg) # Aqui o terminal pede pro usuario digitar com o input, pega o dado e armazena em N;

        if n.isnumeric(): # Verifica se é número;
            return int(n) # Retorna o valor em formato INT e encerra o LOOP;

        print("\033[0,31mERROR! Digite um número inteiro válido!\033[m") # Mensagem de erro caso a condição de isnumeric() não seja atentida;


n = leiaInt("Digite um numero: ") # Envia a mensagem "Digite um numero" para a função;

