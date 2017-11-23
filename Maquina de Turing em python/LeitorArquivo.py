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
        self.EstadosIniciais = linhas[3]
        self.EstadoAceitacao = linhas[4].split(" ")

        transicoes = linhas[5].split(" ")
        n = self.QF = (len(transicoes)-2) // 3
        transicoes = linhas[5:]
        
        print(n)
        self.Transicoes = []
        if n == 1:
            for t in transicoes:
                self.Transicoes.append(t.split(" "))
        else:
            # 1, n... , 1 , n... , n...
            for t in transicoes:
                ax = t.split(" ")
                print (ax)
                unit = [ ax[0], ax[1+n] ]
                sf = []
                psf = []
                dire = []
                for i in range(n):
                    sf.append(ax[ 1+i ])
                    psf.append(ax[ 2+n+i ])
                    dire.append(ax[ 2+(2*n)+i ])
                self.Transicoes.append( [unit[0], sf, unit[1], psf, dire] )
                    

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
        return self.QF


la = LeitorArquivo("testeSimples.txt")

print(la.getAlfabetoEntrada())

print(la.getAlfabetoFita())

print(la.getEspacoBrancoFita())

print(la.getEstadosIniciais())

print(la.getEstadoAceitacao())

ts = la.getTransicoes()
for i in ts:
    print(i)

print(la.getQuantidadeDeFitas())

