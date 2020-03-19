# -*- coding: utf-8 -*-

"""
Objetivo: Obter 2 litros no jarro de 4 litros
Dados um jarro de 3 e outro de 4 litros, inicialmente vazios

"""

#importado Pandas e Numpy para auxíio na manipulação de dados
import pandas as pd 
import numpy as np

"""
Foram criadas 3 funções: encher, esvaziar e transferir
Elas se tornam 6 funções, sendo 3 realizadas em cada jarro

"""

#enche o jarro com a capacidade máxima
def encher(j,mx): 
    return mx

#esvazia o jarro
def esvaziar(j):
    return 0

#transfere o conteúdo de um jarro para outro
def t1 (j1,j2,mx2): 

#aqui transferimos todo o conteúdo e esvaziamos o jarro de origem    
    if j1 + j2 <= mx2:
        j2=j1+j2
        j1=0
    else:
#aqui transferimos parte do conteúdo, até o limite do jarro alvo
        aux = mx2-j2
        j2=mx2
        j1=j1-aux
    return j1,j2

#aqui utilizamos regras para as operações
#basicamente temos um arquivo txt com os estados possíveis e consultamos nessa base
#se o valor for contido nesse arquivo, é possível considerá-lo
#também consultamos na lista de estados construída se o novo estado a ser criado é repetido
#se o estado for repetido, ele nem é criado
#portanto nenhum estado repetido será criado
    
def regras(s,est,i):
    
    if s[i+1] in est:
        if s.count(s[i+1]) == 1:
            return 1
        else:
            s[i+1]=[0,0]
            return 0
    else:
        return 0

#leitura do arquivo txt com os estados possíveis
estados = pd.read_csv('estados.txt', delimiter=' ', names =['j3','j4', 'estado'])
est_val= estados[['j3','j4']]
est_name = estados[['estado']]
est_val = np.array(est_val)
est_name = np.array(est_name)


#Busca em Profundidade

#lista s de estados é inicializada
s = [[0,0],[0,0]]
#como temos 3 operações em 2 jarros, limitamos a 6 operações em um mesmo estado
n_op = 6
#contadores - i de índice de lista, c de operações, k limita a busca
i, c, k = 0, 0, 0
#conteúdo máximo dos jarros
mx1, mx2 = 4, 3

#no while abaixo executamos as operações na ordem expressa
#se for um estado permitido e não repetido, ele é agregado a lista de estados
#a busca executada e em profundidade, portando descemos a lista partindo sempre do estado anterior
#o estado alvo é [2,0]

while(k<1000):
    while (c<n_op):
        s[i+1][0]=encher(s[i][0],4)
        s[i+1][1]=s[i][1]
        if (regras(s,est_val.tolist(),i)) == 1:
            print('\n Lista atualizada: \n',s)
            s.append([0,0])
            i=i+1
            c=0
            break
        c=c+1
        s[i+1][1]=encher(s[i][1],3)
        s[i+1][0]=s[i][0]
        if (regras(s,est_val.tolist(),i)) == 1:
            print('\n Lista atualizada: \n',s)
            s.append([0,0])
            i=i+1
            c=0
            break
        c=c+1
        s[i+1][0]=esvaziar(s[i][0])
        s[i+1][1]=s[i][1]
        if (regras(s,est_val.tolist(),i)) == 1:
            print('\n Lista atualizada: \n',s)
            s.append([0,0])
            i=i+1
            c=0
            break
        c=c+1        
        s[i+1][1]=esvaziar(s[i][1])
        s[i+1][0]=s[i][0]
        if (regras(s,est_val.tolist(),i)) == 1:
            print('\n Lista atualizada: \n',s)
            s.append([0,0])
            i=i+1
            c=0
            break
        c=c+1
        s[i+1][0],s[i+1][1]=t1(s[i][0],s[i][1],mx2)
        if (regras(s,est_val.tolist(),i)) == 1:
            print('\n Lista atualizada: \n',s)
            s.append([0,0])
            i=i+1
            c=0
            break
        c=c+1        
        s[i+1][1],s[i+1][0]=t1(s[i][1],s[i][0],mx1)
        if (regras(s,est_val.tolist(),i)) == 1:
            print('\n Lista atualizada: \n',s)
            s.append([0,0])
            i=i+1
            c=0
            break
        c=c+1              
    if (c==n_op):
        c=0
        k=k+1
    if ([2,0] in s):
        print('\n Estado alvo encontrado!')
        break
s.pop()
print('\n Estados percorridos - lista final: \n',s)