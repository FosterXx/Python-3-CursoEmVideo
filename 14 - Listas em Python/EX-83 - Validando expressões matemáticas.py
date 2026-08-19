# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# expressao = []
# expressao.append(str(input("Digite a Expressão: ")).strip().upper())

# contAbre = 0
# contFecha = 0

# for v in expressao:
#     if v == '(':
#         contAbre += 1
#     elif v == ')':
#         contFecha += 1

# if contAbre == contFecha:
#     print("Expressão Valida!")
# else:
#     print("Expressão Inválida!")

###############################################################

# Professor;

expr = str(input("Digite a expressão: ")).strip()

pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print("Expressão Válida!")
else:
    print("Expressão Inválida!")
