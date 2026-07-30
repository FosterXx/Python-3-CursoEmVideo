# Faça um programa que leia algo do teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele:

valor = input("Digite algo: ")

print("\n")
print(f"É numerico: {valor.isnumeric()}")
print(f"É alfabetico: {valor.isalpha()}")
print(f"É espaço: {valor.isspace()}")
print(f"É alfa-numerico: {valor.isalnum()}")
print(f"É maiusculo: {valor.isupper()}")
print(f"É minusculo: {valor.islower()}")
print(f"É decimal: {valor.isdecimal()}") # IsDecimal reconhece se a string contém apenas caracteres de BASE 10 (0 a 9).
print(f"É digito: {valor.isdigit()}") # IsDigit reconhece se a string contém apenas caracteres numericos como 1,2,3 e ¹,²,³ (2²,4³,1¹).
print(f"É codigo ASCII: {valor.isascii()}") # IsAscii reconhece se a string contém apenas numeros do código ASCII (de 0 a 127 - que inclui as letras de A-Z, números de 0-9 e pontuações básicas).
print(f"É Imprimivel: {valor.isprintable()}") # IsPrintTable reconhece se a string contém apenas caracteres imprimives como letras, números, símbolos, pontuações e espaços ou False se conter apenas caracteres de controle como tabulações \t ou quebras de linha \n.
print(f"É valido para variavel/função/classe: {valor.isidentifier()}") # IsIdentifier reconhece se a string é um nome válido para variaveis, funções ou classes.
print(f"É titulo: {valor.istitle()}") # IsTitle reconhece se a string é um titulo (primeira letra de cada palavra em maiusculo e as demais minusculas).
