class LeitorArquivo(object):
    
    def __init__(self, nomeArq):
        self.arq = open("{}".format(nomeArq), "r")
        self.buffer = arq.read()
        self.Transicoes = ""
        self.QuantidadeDeFitas = 0
    def getTransicoes(self):
        linhas = self.buffer.splitlines("\n")
    def getQuantidadeDeFitas(): pass
