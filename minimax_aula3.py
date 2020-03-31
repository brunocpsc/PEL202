# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:18:40 2020
"""
import math

print('\nJogo da Velha.')
print(' ___ ___ ___\n| 1 | 2 | 3 |\n|___|___|___|\n| 4 | 5 | 6 |\n|___|___|___|\n| 7 | 8 | 9 |\n|___|___|___|' )
print('O PC é o "x", o competidor (você) é o "o".')
print('O PC inicia o jogo.')
print('Processando....aguarde....\n')

board=[['','',''],['','',''],['','','']]
vx,vo,jog,vr,k=0,0,0,1,0
lin,col=0,0

def ver_board(board):
    i,j,check=0,0,0
    
    for i in range(3):
        for j in range (3):
            if board[i][j]!='':
                check=check+1
    if check == 9:
        return 0
    else:
        return 1
            
def ver_venc(board,jog):
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
    aux,i,j,lin,col=0,0,0,0,0
    pont=-math.inf

    for i in range(3):
        for j in range (3):
            if board[i][j]=='':
                board[i][j]='x'
                aux=minimax(board,0,'o')
                board[i][j]=''
                if aux > pont:
                    pont=aux
                    lin,col=i,j
    
    return lin,col

def move_o (board):
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

def ver_res(board):
    
    vr=ver_board(board)
    vx=ver_venc(board,'x')
    vo=ver_venc(board,'o')
    
    if vx == 1:
        return 1
    if vo == 1:
        return -1
    if vr+vo+vx==0:
        return 0

def ver_final(board):
    c=0
    if ver_res(board) == 1:
        print('\n "x" Vencedor!\n')
        print('\n ==TABULEIRO FINAL==\n')
        print(board[0])
        print(board[1])
        print(board[2])
        c=1
    if ver_res(board) == -1:
        print('\n "o" Vencedor!\n')
        print('\n ==TABULEIRO FINAL==\n')
        print(board[0])
        print(board[1])
        print(board[2])
        c=1
    if ver_res(board) == 0:
        print('\n Empate!\n')
        print('\n ==TABULEIRO FINAL==\n')
        print(board[0])
        print(board[1])
        print(board[2])
        c=1
    return c

def printaboard(board):
    print('\n ==TABULEIRO Atual==\n')
    print(board[0])
    print(board[1])
    print(board[2])
    return 1
        
def minimax(board, prof, jog):
    pont,i,j,=0,0,0
    
    if ver_res(board) == -1:
        return -1
    if ver_res(board) == 1:
        return 1
    if ver_res(board) == 0:
        return 0
    
    elif jog=='o':
        pont=math.inf
        for i in range(3):
            for j in range (3):
                if board[i][j]=='':
                    board[i][j]='o'
                    pont=min(pont,minimax(board, prof+1,'x'))
                    board[i][j]=''
        return pont
    
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
    lin,col=move_x(board)
    board[lin][col]='x'
    if ver_final(board)==1:
        break
    printaboard(board)
    move_o(board)
    if ver_final (board)==1:
        break
    printaboard(board)



