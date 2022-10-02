
from random import randint
from time import sleep

def printa_matriz(matriz, num_linhas, num_colunas, escolha_linha1, escolha_coluna1, escolha_linha2, escolha_coluna2):

    contador_linha = 0
    contador_coluna = 0

    # PRINTA GUIA DE CIMA:
    for x in range(num_colunas+1):
        if x != 0:
            print("\033[1;31m"+str(x)+"\033[0;0m", end="   ")
        else:
            print(" ",end="   ")

    # PULA PRA LINHA DE BAIXO
    for linha in matriz:
        print(" ") 
        contador_linha += 1
        contador_coluna = 0

        # PRINTA GUIA LATERAL
        if contador_linha != 10:
            print("\033[1;31m"+str(contador_linha)+"\033[0;0m", end="   ")
        else:
            print("\033[1;31m"+str(contador_linha)+"\033[0;0m", end="  ")
        
        # PRINTA VALORES DA MATRIZ
        for i in linha:
            contador_coluna += 1
            if ( ((contador_linha-1) == escolha_linha1) and ((contador_coluna-1) == escolha_coluna1) ) or ( ((contador_linha-1) == escolha_linha2) and ((contador_coluna-1) == escolha_coluna2) ):
                print("\033[0;32m"+i+"\033[0;0m", end="   ") 
            else:
                print(i , end="   ")
        
    print(" ")

def gerar_matriz_aparente(num_linhas, num_colunas): # Funçao para gerar matriz aparente que é aquela com as letra "escondidas" sendo mostrado as "#" no lugar

    matriz_aparente = []
    for l in range(num_linhas):
        linha_aparente = []
        for c in range(num_colunas): 
            valor = "#"
            linha_aparente.append(valor)

        matriz_aparente.append(linha_aparente)

    return matriz_aparente

def gerar_lista_letras(num_linhas, num_colunas):

    matriz_oculta = []
    valor_ascii = 65
    contador = 0
    letras_necessarias = int( (num_linhas * num_colunas) / 2 )
    tamanho_matriz = int( (num_linhas * num_colunas) )

    for v in range(tamanho_matriz):
        valor = chr(valor_ascii)
        matriz_oculta.append(valor)
        valor_ascii += 1
        contador += 1
        if (valor_ascii > 90):
            valor_ascii = 65
        if (contador == letras_necessarias):
            valor_ascii = 65
        
    return matriz_oculta

def embaralha_lista(lista, num_linhas, num_colunas):
    
    tam_lista = len(lista)

    for pos in range(tam_lista):

        num_aleatorio = randint(0, int((tam_lista-1)) )

        valor_temporario = lista[pos]
        lista[pos] = lista[num_aleatorio]
        lista[num_aleatorio] = valor_temporario

    return lista

def lista_para_matriz(lista, num_linhas, num_colunas):

    matriz = []
    cont = 0
    
    for x in range(num_linhas):
        linha = []
        for y in range(num_colunas):
            index_lista = cont + y
            valor = lista[index_lista]
            linha.append(valor)

        cont += num_colunas        
        matriz.append(linha)

    return matriz
            
print("\n========================= JOGO DA MEMÓRIA =========================\n")
print('''---> REGRAS:
Vire 2 valores por vez, se forem iguais eles ficam revelados.
Voce tera a opção de usar a DICA revelando todas as posições por 3 segundos, porém só pode ser usada 2 vezes por nível.
O jogo acaba ao revelar todas as posições ou sair do jogo.
Se o valor escolhido parear com uma posição já revelada, ele não contará como acerto.
''')
print("--> Escolha o nível de dificuldade para começar \n")

# Escolha do nível
nivel = 0
while nivel not in range (1,4):
    nivel = int(input("1 para nível 4x4\n2 para o nível 8x8\n3 para o nível 10x10\n--> "))

if nivel == 1:
    linhas = 4
    colunas = 4

elif nivel == 2:
    linhas = 8
    colunas = 8

elif nivel == 3:
    linhas = 10
    colunas = 10

#Jogo com o nivel selecionado
print(f"\n================================== NÍVEL {linhas}x{colunas} ==================================\n")

matriz_escolha = gerar_matriz_aparente(linhas,colunas)
matriz_em_lista = gerar_lista_letras(linhas,colunas)
matriz_em_lista = embaralha_lista(matriz_em_lista, linhas, colunas)
matriz_jogo = lista_para_matriz(matriz_em_lista, linhas, colunas)

fim_de_jogo = False
acertos = 0
exibir_respostas = 2 
pos_certas = [] # Precisei criar uma lista para guardas as posições ja acertadas para evitar de subistituir elas por # caso selecionadas denovo por engano

while fim_de_jogo == False: # LOOP EXECUTADO DURANTE O JOGO

# PRINTA TABULEIRO ATUAL
    printa_matriz(matriz_escolha, linhas, colunas, -1,-1,-1,-1)

# PERGUNTA SE DEJESA USAR "EXIBIR RESPOSTAS"
    if exibir_respostas > 0:
        escolha_exibir_respostas = str(input(f"\nDIGITE \'d\' para usar a DICA, \'s\' para SAIR, ou QUALQUER outro valor para ESCOLHER os valores \nUSOS DE DICA RESTANTES: {exibir_respostas}\n"))
        if escolha_exibir_respostas == "d":
            exibir_respostas -= 1
            printa_matriz(matriz_jogo, linhas, colunas, -1,-1,-1,-1)
            for x in range(3,-1,-1):
                sleep(1)
                print(x, end=" ")
            print("\n"*100)
            printa_matriz(matriz_escolha, linhas, colunas,-1,-1,-1,-1)
        elif escolha_exibir_respostas == "s":
            fim_de_jogo = True
            break

# ESCOLHA DAS POSIÇÃO 01
    print("\nEscolha a posição no tabuleiro inserindo a LINHA e depois a COLUNA da posição desejada.\n")
    print("=== PRIMEIRA ESCOLHA ===\n")
    escolha_linha01 = (int(input("LINHA --> ")) - 1)
    escolha_coluna01 = (int(input("COLUNA --> ")) - 1)
    if escolha_linha01 in range(linhas) and escolha_coluna01 in range(colunas): # Caso o input seja um valor fora do range de linhas e colunas da matriz
        pos01 = matriz_jogo[escolha_linha01][escolha_coluna01]
        valor_pos01 = (pos01+str(escolha_linha01+1)+str(escolha_coluna01+1)) # Como em matrizes maiores as letra começam a repetir, essa variavel guarda o a letra seguida dos numeros que equivalem a posiçao dela, por exemplo: A23 seria a letra A na linha 2 coluna 3
        print(valor_pos01)
        matriz_escolha[escolha_linha01][escolha_coluna01] = pos01
        printa_matriz(matriz_escolha,linhas,colunas,escolha_linha01,escolha_coluna01,-1,-1)
        
    else: 
        print("\nValor inválido ou já selecionado, nenhuma posição será revelada\n")
        pos01 = -1

# ESCOLHA DAS POSIÇÃO 02
    print("\n=== SEGUNDA ESCOLHA ===\n")
    escolha_linha02 = (int(input("LINHA --> ")) -1)
    escolha_coluna02 = (int(input("COLUNA --> ")) -1)
    if ( escolha_linha02 in range(linhas) and escolha_coluna02 in range(colunas) ) and (escolha_linha01 != escolha_linha02 or escolha_coluna01 != escolha_coluna02): # Caso o input seja um valor fora do range de linhas e colunas da matriz
        pos02 = matriz_jogo[escolha_linha02][escolha_coluna02]
        valor_pos02 = (pos02+str(escolha_linha02+1)+str(escolha_coluna02+1)) # Como em matrizes maiores as letra começam a repetir, essa variavel guarda o a letra seguida dos numeros que equivalem a posiçao dela, por exemplo: A23 seria a letra A na linha 2 coluna 3
        print(valor_pos02)
        matriz_escolha[escolha_linha02][escolha_coluna02] = pos02
        printa_matriz(matriz_escolha,linhas,colunas,escolha_linha01,escolha_coluna01,escolha_linha02,escolha_coluna02)
        
    else: 
        print("\nValor inválido ou já selecionado, nenhuma posição será revelada\n")
        pos02 = -2

# CASO ACERTOU:
    if (pos01 == pos02) and (valor_pos01 not in pos_certas and valor_pos02 not in pos_certas):
        acertos += 1
        pos_certas.append(valor_pos01)
        pos_certas.append(valor_pos02)
# CASO ERROU: 
    else:
        if valor_pos01 not in pos_certas and pos01 != -1:
            matriz_escolha[escolha_linha01][escolha_coluna01] = "#"
        if valor_pos02 not in pos_certas and pos02 != -2:
            matriz_escolha[escolha_linha02][escolha_coluna02] = "#"
        sleep(1.5)
        print("\n"*50)
        continue     
    sleep(1.5)
    print("\n"*50) # Printar linhas vazias para subir a resposta anterior no terminal

# VERIFICA FIM DE JOGO
    if acertos >= ( (linhas*colunas) / 2 ):
        fim_de_jogo = True 

print("\n===================FIM DE JOGO====================\n")
