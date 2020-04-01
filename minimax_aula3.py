# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:18:40 2020
"""
import math

print('Jogo da Velha.')
print(' ___ ___ ___\n| 1 | 2 | 3 |\n|___|___|___|\n| 4 | 5 | 6 |\n|___|___|___|\n| 7 | 8 | 9 |\n|___|___|___|' )
print('O PC é o "x", o competidor (você) é o "o".')
print('O PC inicia o jogo.')

#Os prints acima servem para indicar as instruções

board=[['','',''],['','',''],['','','']] #criação do tabuleiro
vx,vo,jog,vr,k=0,0,0,1,0

def ver_board(board): #função que verificar se o tabuleiro está cheio
    i,j,check=0,0,0
    
    for i in range(3):
        for j in range (3):
            if board[i][j]!='':
                check=check+1
    if check == 9:
        return 0
    else:
        return 1
            
def ver_venc(board,jog): #função que verificar se há vencedor
    i,j,check,v=0,0,0,0
    
    for i in range(3):
        check=0
        for j in range (3):
            if board[i][j]==jog:
                check=check+1
                if check==3:
                    v=1
                                    
    for j in range(3):
        check=0
        for i in range (3):
            if board[i][j]==jog:
                check=check+1
                if check==3:
                     v=1
    check=0         
    for i in range(3):
            if board[i][i]==jog:
                check=check+1
                if check==3:
                     v=1
    check=0      
    if board[1][1]==jog:
        check=check+1
    if board[0][2]==jog:
        check=check+1    
    if board[2][0]==jog:
        check=check+1  
    if check==3:
        v=1
        
    return v
    
def move_x(board):
    #aqui temos a função que escolhe o melhor posicionamento de 'x'
    #a função retorna os valores dos índices da melhor posição para 'x' no tabuleiro
    aux,i,j,lin,col=0,0,0,0,0
    pont=-math.inf

    for i in range(3):
        for j in range (3):
            if board[i][j]=='':
                board[i][j]='x'
                #chamos o minimax para obter a heurística do estado final e maximizar 
                #o posiocnamento do 'x', o minimax se chama recursivamente para se
                #aprofundar na árvore até encontrar os estados finais
                #após isso, limpamos o tabuleiro e guardamos os índices que garantem
                #o melhor posicionamento
                aux=minimax(board,0,'o')
                board[i][j]=''
                if aux > pont:
                    pont=aux
                    lin,col=i,j
    
    return lin,col

def move_o (board):
    #aqui temos a função que posiciona o 'o' no tabuleiro
    #o valor é obtido pelo teclado
    #verificamos se são valores válidos (não é um espaço repetido ou valor fora do range de 1-9)
    i,j,aux=0,0,0
    
    while (aux==0):
        pos=input('Jogue! Insira, numericamente, a posição de jogo (1 até 9), desde que esteja vazia:')  
        pos=int(pos)
        if pos==1:
            i,j=0,0
        if pos==2:
            i,j=0,1
        if pos==3:
            i,j=0,2
        if pos==4:
            i,j=1,0
        if pos==5:
            i,j=1,1
        if pos==6:
            i,j=1,2
        if pos==7:
            i,j=2,0
        if pos==8:
            i,j=2,1
        if pos==9:
            i,j=2,2  
        if board[i][j]!='' or pos > 9 or pos <1:
            print('Posição iválida.')
            print('\n ==TABULEIRO Atual==\n')
            print(board[0])
            print(board[1])
            print(board[2])
        else:
            board[i][j]='o'
            aux=1

    return board

def ver_res(board): #função que verificar o resultado final
    
    #essa função é utilizada para retornar a heuristica atribuída
    # 1 : 'x' vence
    #-1 : 'o' vence
    # 0 : empate
    
    vr=ver_board(board)#chama função que verificar se o tabuleiro está cheio - empate
    vx=ver_venc(board,'x') #chama função que verifica vencedor 'x'
    vo=ver_venc(board,'o') #chama função que verifica vencedor 'o'
    
    if vx == 1:
        return 1
    if vo == 1:
        return -1
    if vr+vo+vx==0:
        return 0

def ver_final(board):
    #essa função chama a verificação de resultado após as jogadas e verifica expõe o resultad
    #a função para o jogo nas condições de derrota, empate e vitória
    c=0
    if ver_res(board) == 1:
        print('\n "x" Vencedor!!')
        print('\n ==TABULEIRO FINAL==\n')
        print(board[0])
        print(board[1])
        print(board[2])
        c=1
    if ver_res(board) == -1:
        print('\n "o" Vencedor!!')
        print('\n ==TABULEIRO FINAL==\n')
        print(board[0])
        print(board[1])
        print(board[2])
        c=1
    if ver_res(board) == 0:
        print('\n Empate!!')
        print('\n ==TABULEIRO FINAL==\n')
        print(board[0])
        print(board[1])
        print(board[2])
        c=1
    return c

def printaboard(board):#funçao que imprime a condição atual do tabuleiro
    print('\n ==TABULEIRO Atual==\n')
    print(board[0])
    print(board[1])
    print(board[2])
    return 1
        
def minimax(board, prof, jog):
    #aqui temos o algoritmo minimax
    #as três primeiras sentenças verificam as heurísticas dos estados finais
    #essa função retorna a heurística para indicar a melhor jogada ao jogador 'x', que é o PC no caso
    #ela maximiza as jogadas de 'x'  e miniza as jogadas de 'o', que é o adversário
    pont,i,j,=0,0,0
    
    if ver_res(board) == -1:
        return -1
    if ver_res(board) == 1:
        return 1
    if ver_res(board) == 0:
        return 0
    
    #aqui fazemos a minimização e recursivamente vamos nos aprofundando na árvore
    elif jog=='o':
        pont=math.inf
        for i in range(3):
            for j in range (3):
                if board[i][j]=='':
                    board[i][j]='o'
                    pont=min(pont,minimax(board, prof+1,'x'))
                    board[i][j]=''
        return pont
    
    #aqui fazemos a maximização e recursivamente vamos nos aprofundando na árvore
    elif jog=='x':
        pont=-math.inf
        for i in range(3):
            for j in range (3):
                if board[i][j]=='':
                    board[i][j]='x'
                    pont=max(pont,minimax(board, prof+1,'o'))
                    board[i][j]=''
        return pont
    
while (1):
    #aqui temos a função que inicia o jogo
    #chamos o função que retorna os índices de posicionamento do 'x'
    print('Processando Jogada do "x"...aguarde...')
    lin,col=move_x(board)
    #posicionamentos 'x' no tabueiro
    board[lin][col]='x'
    #verificamos se é o fim do jogo - vitória, empate ou derrota
    if ver_final(board)==1:
        break
    #imprimimos a situação do tabuleiro
    printaboard(board)
    #aqui temos a função que coleta o posicionamento do 'o' do teclado - adversário do PC
    move_o(board)
    #verificamos se é o fim do jogo - vitória, empate ou derrota
    if ver_final (board)==1:
        break
    #imprimimos a situação do tabuleiro
    printaboard(board)



