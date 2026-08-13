# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print("<>"*30) # Fluflu
print("\nGerador de PA\n") # Fluflu
print("<>"*30) # Fluflu

primeiro = int(input("\nDigite o primeiro termo: ")) # Recebe o primeiro termo;
razao = int(input("\nDigite a razão: ")) # Recebe a razão da PA;

termo = primeiro # Como a variavel termo vai ser alterada constantemente, melhor manter registro do 1° termo;
cont = 1 # Controle de repetições;
termoF = 10 # Defini qual o ultimo termo, começamos com 10 termos;
total = 0 # Armazenar todos os termos feitos;

while termoF != 0: # Enquanto o ultimo termo ser diferente de 0, o ciclo se repete;
    total = total + termoF # A cada ciclo é acrescentado X termos no total;

    while cont <= termoF: # Enquanto contador = cont(1) for menor ou igual ao ultimo termo = termoF(10)

        print(termo, end=' > ') # Imprimi na tela o termo atual;

        termo += razao # adiciona a razão ao termo atual;
        cont += 1 # aumenta o contador até chegar no cont(10);

    print("PAUSA\n") # Imprimi na tela para simbolizar uma pausa;

    cont = 1 # Redefine a variavel cont para 1 novamente;

    termoF = int(input("Quantos termos você quer mostrar a mais: ")) # Redefine o ultimo termo para o valor escolhido pelo usuario;

print(f"\nTermos Totais: {total}\n") # Após o usuario digitar 0, os ciclos se encerram e é mostrado o total de termos realizados;

print("<>"*30) # Fluflu
