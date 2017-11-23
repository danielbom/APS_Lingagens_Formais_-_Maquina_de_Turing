#   0 Linha 1: alfabeto de entrada
#   1 Linha 2: alfabeto da fita
#   2 Linha 3: simbolo que representa um espaco em branco na fita
#   3 Linha 4: estado inicial
#   4 Linha 5, coloquem uma linha indicando o conjunto de estados de aceitacao
#   5 Linhas 6 em diante: transicoes, uma por linha, no formato
#   estado atual, simbolo atual,  novo estado, novo simbolo, direcao para mover a cabeca
class LeitorArquivo(object):
    def __init__(self, nomeArq):
        self.arq = open("{}".format(nomeArq), "r")
        buff = self.arq.read()
        linhas = buff.splitlines()

        self.AlfabetoEntrada = linhas[0]
        self.AlfabetoFita = linhas[1]
        self.EspacoBrancoFita = linhas[2]
        self.EstadosIniciais = linhas[3].split(" ")
        self.EstadoAceitacao = linhas[4]

        transicoes = linhas[5:]
        self.Transicoes = []
        for t in transicoes:
            self.Transicoes.append(t.split(" "))

        transicoes = linhas[5]

        # Necessita testes
        self.QuantidadeDeFitas = (len(transições)-2) / 3

    def getAlfabetoEntrada(self):
        return self.AlfabetoEntrada

    def getAlfabetoFita(self):
        return self.AlfabetoFita

    def getEspacoBrancoFita(self):
        return self.EspacoBrancoFita

    def getEstadosIniciais(self):
        return self.EstadosIniciais

    def getEstadoAceitacao(self):
        return self.EstadoAceitacao

    def getTransicoes(self):
        return self.Transicoes

    # Necessita testes
    def getQuantidadeDeFitas(self):
        return self.QuantidadeDeFitas


la = LeitorArquivo("testeSimples.txt")


print(la.getAlfabetoEntrada())

print(la.getAlfabetoFita())

print(la.getEspacoBrancoFita())

print(la.getEstadosIniciais())

print(la.getEstadoAceitacao())

print(la.getTransicoes())

print(la.getQuantidadeDeFitas())

