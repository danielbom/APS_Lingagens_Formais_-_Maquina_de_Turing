#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nfitas as fts
import fila as fl

class MTnfitas(object):
    def __init__(self, numFitas = 1):
        self.Transicoes = []
        self.qtdeFitas = numFitas
        self.EstadoInicial = ""
        self.EstadosFinais = []
        self.Entrada = ""
        self.EspB = "B"
        self.FITAS = fts.nfitas(n = numFitas)

    def DefinirEspacoBranco(self, simbulo):
        self.FITAS.setEspacoBranco(simbulo)
    
    def DefinirEntrada(self, entrada):
        if type(entrada) == type(""):
            self.Entrada = entrada
            return self.FITAS.setEntradaInicial(entrada)
        if type(entrada) == type([]):
            self.Entrada = entrada[0]
            return self.FITAS.setEntradaInicial(entrada)
        return False
    
    def DefinirEstadoInicial(self, estado):
        if type(estado) == type(""):
            self.EstadoInicial = estado
            return True
        return False

    def addEstadoFinal(self, estado):
        if type(estado) == type(""):
            self.EstadosFinais.append(estado)
            return True
        elif type(estado) == type([]):
            for i in estado:
                boolr = self.addEstadoFinal(i)
                if not boolr:
                    return False
            return True
        return False

    def addTransicao(self, EstA, ProxE, SimbF, ProxSF, direcs):
        if len(SimbF)==self.qtdeFitas and len(ProxSF)==self.qtdeFitas and len(direcs) == self.qtdeFitas:
            self.Transicoes.append([EstA, ProxE, SimbF, ProxSF, direcs])
            return True
        print("Atenção, lista de simbulos finas, proximos simbulos fitas, e direções devem ter o mesmo tamanho da quantidade de fitas!")
        return False
    
    def buscaTransicao(self, EstA, SimbF):
        if len(SimbF) == self.qtdeFitas:
            transicoes = []
            for t in self.Transicoes:
                if self.qtdeFitas > 1:
                    if t[0] == EstA and t[2] == SimbF:
                        transicoes.append(t)
                else:
                    if t[0] == EstA and t[2] == SimbF[0]:
                        transicoes.append(t)
            
            if len(transicoes) == 0:
                return None
            return transicoes
        return None

    def executar(self):
        EstadoAtual = self.EstadoInicial[0]

        if self.Entrada == "":
            print("Entrada nao definida")
            return None
        FILA = fl.fila()
        self.FITAS.setPosFitas()
        

        transicoes = self.buscaTransicao( EstadoAtual, self.FITAS.getSimbulos() )
        # transicoes == lista de transicao

        if transicoes != None:
            for i in transicoes:
                FILA.push([i, self.FITAS.getEstadoAtualFitas()])


        i = 0
        lim = 100
        TransicoesNulas = 0
        limTransicoesNulas = 10
        while i < lim:
            transicao = FILA.pop()
            # transicao == [ transicao normal, estado da fita ]
            # estado da fita == [ conteudo da fita, pos na fita ]
            # transicao normal == [EstA, ProxE, SimbF, ProxSF, direcs]
            if transicoes == None and EstadoAtual in self.EstadosFinais:
                #Se nao existe transicoes neste ponto e estou em um estado final
                return True
            elif transicao != None:
                self.FITAS.setEntradasEPoss( transicao[1] )

                self.FITAS.exeTransicao( transicao[0][3], transicao[0][4] )

                EstadoAtual = transicao[0][1]
                TransicoesNulas = 0
            else:
                TransicoesNulas += 1

            transicoes = self.buscaTransicao( EstadoAtual, self.FITAS.getSimbulos() )
            if transicoes == None and EstadoAtual in self.EstadosFinais:
                #Se nao existe transicoes neste ponto e estou em um estado final
                return True
            elif transicoes != None:
                FitaAltual = self.FITAS.getEstadoAtualFitas()
                for t in transicoes:
                    FILA.push([t, FitaAltual])
                
            
            if TransicoesNulas == limTransicoesNulas:
                return False

            i += 1
            if i == lim:
                resp = input("Quantidade de iterações igual a: {} - Deseja continuar? s/n: ".format(i))
                if resp.upper() == 'N':
                    break
                else:
                    lim = 2*i
                    
            if self.FITAS.limiteFitasAlcancado():
                print("Limite da(s) fita(s) alcançado")
                break
        return None
                
        
 
    def getEstadosFinais(self):
        return self.EstadosFinais

    def getTransicoes(self):
        return self.Transicoes

### DEBUG
'''
m = MTnfitas(2)

m.addTransicao("0", "0", ["#", "B"], ["#", "B"], ["D", "D"])
m.addTransicao("0", "1", ["a", "B"], ["#", "B"], ["D", "D"])
m.addTransicao("0", "0", ["#", "B"], ["a", "B"], ["E", "E"])

m.addTransicao("1", "1", ["#", "B"], ["#", "B"], ["D", "D"])
m.addTransicao("1", "3", ["a", "B"], ["a", "B"], ["D", "D"])
m.addTransicao("1", "2", ["B", "B"], ["B", "B"], ["E", "E"])

m.addTransicao("3", "3", ["#", "B"], ["#", "B"], ["D", "D"])
m.addTransicao("3", "4", ["a", "B"], ["#", "B"], ["D", "D"])
m.addTransicao("3", "5", ["B", "B"], ["B", "B"], ["E", "E"])

m.addTransicao("4", "4", ["#", "B"], ["#", "B"], ["D", "D"])
m.addTransicao("4", "3", ["a", "B"], ["a", "B"], ["D", "D"])

m.addTransicao("5", "5", ["a", "B"], ["a", "B"], ["E", "E"])
m.addTransicao("5", "5", ["#", "B"], ["#", "B"], ["E", "E"])
m.addTransicao("5", "0", ["B", "B"], ["B", "B"], ["D", "D"])

m.DefinirEntrada("aaaa")
m.DefinirEstadoInicial("0")
m.addEstadoFinal("2")

print(m.executar())

m.DefinirEntrada("aa")
print(m.executar())
m.DefinirEntrada("aaa")
print(m.executar())
'''
###


'''
b = m.buscaTransicao("0", ["#","#"])
for i in b:
    print(i)

print(m.getEstadosFinais())

for i in m.getTransicoes():
    print(i)
'''

