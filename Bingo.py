#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
from GenRandBingoClass import *
from NameListClass import *

linhas = 3
colunas = 5
cartelas = 80

# Lista de nomes
lista = NameListClass()
lista_size = lista._GetListSize()
lista_nomes = lista._GetList()

# Gerador de Tabelas
genTables = GenRandBingoClass(lista_size,linhas,colunas,cartelas)
tabelas   = genTables._GenTables()

# Vou transformar os valores da tabela em nome retirados da lista de nomes
for i in range(len(tabelas)):
    for j in range(linhas):
        tabelas[i][j] = list(tabelas[i][j])
        for k in range(len(tabelas[i][j])):
            tabelas[i][j][k] = lista_nomes[tabelas[i][j][k]-1]

# Vamos criar o arquivo CSV
with open('bingo.csv', 'w') as csvfile:
    bingo = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_ALL)

    for i in range(cartelas):
        bingo.writerow(['Cartela %i' %(i+1)])
        for j in range(len(tabelas[i])):
            bingo.writerow(tabelas[i][j])
        bingo.writerow([' '])
