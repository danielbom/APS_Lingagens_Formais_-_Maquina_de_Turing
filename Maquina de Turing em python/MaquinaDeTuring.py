#from fita import fita

class MaquinaDeTuring(object):
    def __init__(self, numFitas = 1):
        self.Transicoes = []
        self.Entrada = ""
        self.qtdeFita = numFitas

    def setEntrada(self, entrada):
        self.Entrada = entrada

    # para Maquinas com mais de uma fita, (simbFita, ProxSimbFila, direcoes) é do tipo list
    def addTransicao(self, EstAtual, ProxEst, SimbFila, ProxSimbFila, direcoes):
        self.Transicoes.append([EstAtual, ProxEst, SimbFila, ProxSimbFila, direcoes])

    # retorna proxEst, (ProxSimbFila, direcoes)
    def buscaTransicao(self, EstAtual, SimbFita):
        for transicao in self.Transicoes:
            if transicao[0] == EstAtual and transicao[2] == SimbFita:
                return transicao
