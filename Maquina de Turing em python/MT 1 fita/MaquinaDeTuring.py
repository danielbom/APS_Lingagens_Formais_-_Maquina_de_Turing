#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fita as ft
import fila as fl

class MaquinaDeTuring(object):
    def __init__(self, numFitas = 1):
        #self.f = ft.fita()
        self.Transicoes = []
        self.qtdeFita = numFitas
        self.EstadoInicial = ""
        self.EstadosFinais = []
        self.Entrada = ""
        self.EspB = "B"

    def DefinirEntrada(self, entrada):
        self.Entrada = entrada

    def DefinirEspB(self, simbulo):
        self.EspB = simbulo

    def DefinirEstadoInicial(self, estado):
        self.EstadoInicial = estado

    def addEstadoFinal(self, estado):
        self.EstadosFinais.append(estado)

    # para Maquinas com mais de uma fita, (simbFita, ProxSimbFila, direcoes) é do tipo list
    def addTransicao(self, EstAtual, ProxEst, SimbFila, ProxSimbFila, direcoes):
        self.Transicoes.append([EstAtual, ProxEst, SimbFila, ProxSimbFila, direcoes])

    # retorna proxEst, (ProxSimbFila, direcoes)
    def buscaTransicao(self, EstAtual, SimbFita):
        retorno = []
        for transicao in self.Transicoes:
            if transicao[0] == EstAtual and transicao[2] == SimbFita:
                retorno.append(transicao)
        return retorno

    def executar(self):
        EstadoAtual = self.EstadoInicial
        if self.Entrada == "":
            print("Entrada nao definida")
            return None
        FITA = ft.fita(self.Entrada, self.EspB)

        FILA = fl.fila()
        transicoes = self.buscaTransicao( EstadoAtual, FITA.getSimbulo() )
        
        for i in transicoes:
                #FILA.push([i, [self.Entrada , 0]])
                FILA.push([i, FITA.getEstadoAtualFita()])
        
        i = 0
        lim = 100
        TransicoesNulas = 0
        limTransicoesNulas = 10
        while i < lim:
            i+=1
            transicao = FILA.pop()
            #print(transicao)
            if transicao != None:
                #FITA.setEntrada( transicao[1][0] )
                #FITA.setPosFita( transicao[1][1] )
                FITA.setEntradaEPos( transicao[1][0], transicao[1][1] )
                
                # print("Executando a transicao -- POSFITA [ {} ]\n".format(FITA.getPosFita()))
                FITA.exeTransicao( transicao[0][3], transicao[0][4] )
                # Estado atual recebe proxEstado
                EstadoAtual = transicao[0][1]
                TransicoesNulas = 0
            else:
                TransicoesNulas += 1
                
            transicoes = self.buscaTransicao( EstadoAtual, FITA.getSimbulo() )
            if len(transicoes) == 0 and EstadoAtual in self.EstadosFinais:
                #Se nao existe transicoes neste ponto e estou em um estado final
                return True
            
            FitaAtual = FITA.getEstadoAtualFita()
            for t in transicoes:
                FILA.push([t, FitaAtual])
            
            if TransicoesNulas == limTransicoesNulas:
                return False
            
            if i == lim:
                resp = input('Quantidade de iterações igual a: {}\nDeseja parar? s/n: '.format(i))
                if resp.upper() == 'S':
                    break
                else:
                    lim = 2*i
            
            if FITA.limiteAlcancado():
                break

        return None


# testes e debug

m = MaquinaDeTuring()
m.addTransicao("0", "0", "#", "#", "D")
m.addTransicao("0", "1", "a", "#", "D")
m.addTransicao("0", "0", "#", "a", "E")

m.addTransicao("1", "1", "#", "#", "D")
m.addTransicao("1", "3", "a", "a", "D")
m.addTransicao("1", "2", "B", "B", "E")

m.addTransicao("3", "3", "#", "#", "D")
m.addTransicao("3", "4", "a", "#", "D")
m.addTransicao("3", "5", "B", "B", "E")

m.addTransicao("4", "4", "#", "#", "D")
m.addTransicao("4", "3", "a", "a", "D")

m.addTransicao("5", "5", "a", "a", "E")
m.addTransicao("5", "5", "#", "#", "E")
m.addTransicao("5", "0", "B", "B", "D")

m.DefinirEntrada("aaaa")
m.DefinirEstadoInicial("0")
m.addEstadoFinal("2")

#print(m.buscaTransicao("0", "#"))

print(m.executar())
m.DefinirEntrada("aa")
print(m.executar())
m.DefinirEntrada("aaa")
print(m.executar())

# fim debug
