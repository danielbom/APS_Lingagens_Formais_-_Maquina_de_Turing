import fita as ft

class MaquinaDeTuring(object):
    def __init__(self, numFitas = 1):
        self.f = ft.fita()
        self.Transicoes = []
        self.qtdeFita = numFitas
        self.EstadoInicial = ""
        self.EstadosFinais = []
        self.Entrada = ""
        self.EspB = ""

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
        for transicao in self.Transicoes:
            if transicao[0] == EstAtual and transicao[2] == SimbFita:
                return transicao
        return None

    def executar(self):
        EstadoAtual = self.EstadoInicial
        executando = True
        if self.Entrada == "":
            print("Entrada nao definida")
            executando = False
        self.f = ft.fita(self.Entrada, self.EspB)

        while executando:
            transicao = self.buscaTransicao( EstadoAtual, self.f.getSimbulo())
            if transicao == None:
                executando = False
            else:
                # Altera o valor do estadoAtual para o valor da transicao
                self.f.setSimbulo( transicao[3] )
                # Estado atual recebe proxEstado
                EstadoAtual = transicao[1]
                # Movimenta posicao da fita
                self.f.movimenta(transicao[4])
                
        if EstadoAtual in self.EstadosFinais:
            return True
        return False
        




# testes e debug
'''
m = MaquinaDeTuring()
m.addTransicao("0", "0", "#", "#", "D")
m.addTransicao("0", "1", "a", "#", "D")

m.addTransicao("1", "1", "#", "#", "D")
m.addTransicao("1", "3", "a", "a", "D")
m.addTransicao("1", "2", "", "", "E")

m.addTransicao("3", "3", "#", "#", "D")
m.addTransicao("3", "4", "a", "#", "D")
m.addTransicao("3", "5", "", "", "E")

m.addTransicao("4", "4", "#", "#", "D")
m.addTransicao("4", "3", "a", "a", "D")

m.addTransicao("5", "5", "a", "a", "E")
m.addTransicao("5", "5", "#", "#", "E")
m.addTransicao("5", "0", "", "", "D")

m.DefinirEntrada("aaaa")
m.DefinirEstadoInicial("0")
m.addEstadoFinal("2")

print(m.executar())
'''
# fim debug
