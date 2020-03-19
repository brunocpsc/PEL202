# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:06:13 2020

@author: re91206z
"""

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

#Busca em Largura

#lista s de estados é inicializada
s = [[0,0],[0,0]]
#lista final a ser apresentada com os resultados nas sequências dos ramos
l = []
#lista que indica o nó pai é incializada
p = [[0,0]]

#como temos 3 operações em 2 jarros, limitamos a 6 operações em um mesmo estado
n_op = 6
#contadores - i de índice de lista, c de operações, k limita a busca
i, c, k, j = 0, 0, 0, 0
#conteúdo máximo dos jarros
mx1, mx2 = 4, 3

#no while abaixo executamos as operações na ordem expressa
#se for um estado permitido e não repetido, ele é agregado a lista de estados
#a busca executada é em largura, portando percorremos a lista abrindo todos os ramos em relação ao estado atual
#o estado alvo é [2,0]

while(k<1000):
    while (c<n_op):
        
        s[i+1][0]=encher(s[j][0],4)
        s[i+1][1]=s[j][1]
        if (regras(s,est_val.tolist(),i)) == 1:
            s.append([0,0])
            i=i+1
            p.append([i,j])
            c=0
        else:
            c=c+1
        if ([2,0] in s):
            break
        
        s[i+1][1]=encher(s[j][1],3)
        s[i+1][0]=s[j][0]
        if (regras(s,est_val.tolist(),i)) == 1:
            s.append([0,0])
            i=i+1
            p.append([i,j])
            c=0
        else:
            c=c+1
        if ([2,0] in s):
            break
        
        s[i+1][0]=esvaziar(s[j][0])
        s[i+1][1]=s[j][1]
        if (regras(s,est_val.tolist(),i)) == 1:
            s.append([0,0])
            i=i+1
            p.append([i,j])
            c=0
        else:
            c=c+1
        if ([2,0] in s):
            break               
        
        s[i+1][1]=esvaziar(s[j][0])
        s[i+1][0]=s[j][0]
        if (regras(s,est_val.tolist(),i)) == 1:
            s.append([0,0])
            i=i+1
            p.append([i,j])
            c=0
        else:
            c=c+1
        if ([2,0] in s):
            break                  

        s[i+1][0],s[i+1][1]=t1(s[j][0],s[j][1],mx2)
        if (regras(s,est_val.tolist(),i)) == 1:
            s.append([0,0])
            i=i+1
            p.append([i,j])
            c=0
        else:
            c=c+1
        if ([2,0] in s):
            break

        s[i+1][1],s[i+1][0]=t1(s[j][1],s[j][0],mx1)
        if (regras(s,est_val.tolist(),i)) == 1:
            s.append([0,0])
            i=i+1
            p.append([i,j])
            c=0
        else:
            c=c+1
        if ([2,0] in s):
            break   

        j=j+1
             
    if (c>=n_op):
        c=0
        k=k+1
    if ([2,0] in s):
        break       

s.pop()
print('\n Lista com estados percorridos, em ordem: \n', s)
print('\n Lista com estado percorrido na primeira coluna e endereço do "item pai" na segunda coluna: \n',p)

#Aqui criamos o vetor l utilizando o vetor pai auxiliar para saber a origem de cada nó
i = len(p)-1
l.append(s[i])
while ([0,0] not in l):
    l.append(s[p[i][1]])
    i=p[i][1]

print ('\n Ordem dos ramos até o estado alvo:\n',l)
