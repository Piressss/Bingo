#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import permutations
from random import randint

# Esse classe gera as tabelas do bingo com uma referencia numerica

class GenRandBingoClass():
    def __init__(self,totalnum,linhas,colunas,numtabelas):
        self.__totalnum = totalnum
        self.__linhas   = linhas
        self.__colunas  = colunas
        self.__numtabelas  = numtabelas

    # divide o total de numeros em N grupos (N = linhas)
    def _DivTotalNum(self):
        grupos = []
        gruposize = self.__totalnum / self.__linhas

        # define os grupos
        for i in range(self.__linhas):
            grupos.append([(gruposize*i)+1,(gruposize*(i+1))])

        # como a divisao pode nao ser exata, substituo o ultimo numero pelo total de numeros
        grupos[self.__linhas -1][1] = self.__totalnum

        return grupos

    # gero todas as possibilidades de cada linha
    def _PermutLin(self):
        grupos = self._DivTotalNum()
        seqgrupos = []
        poslinhas = []

        for i in range(len(grupos)):
            seqgrupos.append(0)
            seqgrupos[i] = range(grupos[i][0],grupos[i][1]+1)

        for i in range(len(seqgrupos)):
            poslinhas.append([])
            for subset in permutations(seqgrupos[i],self.__colunas):
                poslinhas[i].append(subset)

        return poslinhas
        
    # gero as tabelas sorteando as linhas
    def _GenTables(self):
        poslinhas = self._PermutLin()
        tabelas=[]
        last_random = -1
        random = -1

        for i in range(self.__numtabelas):
            tabelas.append([])
            for j in range(self.__linhas):
                while random == last_random:
                    random = randint(0,len(poslinhas[j]))
                last_random = random
                tabelas[i].append(poslinhas[j][random])
        return tabelas

