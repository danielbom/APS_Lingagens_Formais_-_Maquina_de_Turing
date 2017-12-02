#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fita as ft

class nfitas(object):
    def __init__(self, entrada = "B", espB = "B", n=1):
        self.limite = 5000
        self.FITAS = []
        self.posFitas = []
        if n >= 1:
            self.qtdeFitas = n
        else:
            self.qtdeFitas = 1
        for i in range(n):
            self.FITAS.append( ft.fita() )
            self.posFitas.append( 0 )
        
        self.EspB = espB
        self.FITAS[0].setEntrada( entrada )

    def setEspacoBranco(self, simbulo):
        if type(simbulo) == type(""):
            for i in range(self.qtdeFitas):
                self.FITAS[i].setEspacoBranco(simbulo)
            return True
        return False
    
    def setEntradaInicial(self, entrada):
        if type(entrada) == type(""):
            self.FITAS[0].setEntrada(entrada)
            for i in range(1, self.qtdeFitas):
                self.FITAS[i].setEntrada(self.EspB)
            return True
        if type(entradas) == type([]) and len(entrada) == self.qtdeFitas:
            for i in range(self.qtdeFitas):
                self.FITAS[i].setEntrada(entrada[i])
            return True
        return False

    # testa o limite de todas as fitas e retorna(T/F) se aconteceu algum problema
    # e as prolongou demais
    def limiteFitasAlcancado(self):
        for i in range(self.qtdeFitas):
            if self.FITAS[i].limiteAlcancado():
                return True
        return False
    
    # retorna todas as strings das fitas e as posicoes delas
    def getEstadoAtualFitas(self):
        estados = []
        for i in range(self.qtdeFitas):
            estados.append(self.FITAS[i].getEstadoAtualFita())
        return estados
    
    # retorna a um momento anterior
    def setEntradasEPoss(self, eEp):
        if len(eEp) == self.qtdeFitas:
            for i in range(self.qtdeFitas):
                self.FITAS[i].setEntrada(eEp[i][0])
                self.FITAS[i].setPosFita(eEp[i][1])
            return True
        return False

    # set simbulos das fitas e movimenta todas elas
    def exeTransicao(self, ProxSF, direcoes):
        if len(ProxSF)==self.qtdeFitas and len(direcoes) == self.qtdeFitas:
            for i in range(self.qtdeFitas):
                self.FITAS[i].exeTransicao(ProxSF[i], direcoes[i])
            return True
        return False

    # getEstadoAtualFitas
    def getSimbulos(self):
        simbulos = []
        for i in range(self.qtdeFitas):
            simbulos.append(self.FITAS[i].getSimbulo())
        return simbulos

    def setPosFitas(self, poss=0):
        if type(poss) == type([]):
            if len(poss) == self.qtdeFitas:
                for i in range(self.qtdeFitas):
                    self.FITAS[i].setPosFita(poss[i])
                return True
        if type(poss) == type(1):
            for i in range(self.qtdeFitas):
                self.FITAS[i].setPosFita(poss)
            return True
        return False
    ############################################################
    ##### Somenta para testes. Extremamente custosos 1 a 1 #####
    def printMe(self):
        for i in range(self.qtdeFitas):
            self.FITAS[i].printMe()
    
    def getPosFitas(self):
        poss = []
        for i in range(self.qtdeFitas):
            poss.append(self.FITAS[i].getPosFita())
        return poss
    ###
    # exeTransicao
    def setSimbulos(self, simbulos):
        if len(simbulos) == self.qtdeFitas:
            for i in range(self.qtdeFitas):
                self.FITAS[i].setSimbulo(simbulos[i])
            return True
        return False

    def movimentos(self, direcoes):
        if len(direcoes) != self.qtdeFitas:
            return False
        for i in range(self.qtdeFitas):
            self.FITAS[i].movimenta(direcoes[i])    
    ############################################################
