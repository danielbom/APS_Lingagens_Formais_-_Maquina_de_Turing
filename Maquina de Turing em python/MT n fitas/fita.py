class fita(object):
    def __init__(self, entrada = "B", espB = "B") :
        self.F = []
        self.limite = 5000
        self.posFita = 0
        self.EspB = espB
        if len(entrada) > 1:
            for letra in entrada:
                self.F.append(letra)
        else:
            self.F.append(entrada)
            
    # Funcoes auxiliares e de debug
    def Desloque_a_Direita(self):
        if self.limite == len(self.F):
            print("Limite da fita alcancado!")
            pass

        self.posFita += 1
        if self.posFita == len(self.F): 
            self.F.append(self.EspB)
    def Desloque_a_Esquerda(self):
        if self.limite == len(self.F):
            print("Limite da fita alcancado!")
            pass

        if self.posFita == 0:
            self.F.insert(0, self.EspB) 
        else:
            self.posFita -= 1
            
    def printMe(self):
        print(self.F)
        
    def limiteAlcancado(self):
        if self.limite == len(self.F):
            return True
        return False
    
    def movimenta(self, direcao):
        if direcao.upper() == "D" or direcao.upper() == "R":
            self.Desloque_a_Direita()
        elif direcao.upper() == "E" or direcao.upper() == "L":
            self.Desloque_a_Esquerda()

    def getSimbulo(self):
        return self.F[self.posFita]
    
    # Funções úteis
    def exeTransicao(self, ProxSF, direcs):
        self.setSimbulo(ProxSF)
        self.movimenta(direcs)
    
    def getEstadoAtualFita(self):
        retorno = ""
        for i in self.F:
            retorno = retorno.__add__(i)
        return [retorno, self.posFita]

    def setEntradaEPos(self, entrada, pos):
        self.setEntrada(entrada)
        self.setPosFita(pos)
    
    def setEntrada(self, entrada):
        self.F.clear()
        for letra in entrada:
            self.F.append(letra)

    def setEspacoBranco(self, simbulo):
        if self.EspB != simbulo:
            tam = len(self.F)
            for i in range(tam):
                if self.F[i] == self.EspB:
                    self.F[i] = simbulo
            self.EspB = simbulo
            return True
        return False
            
    def getPosFita(self):
        return self.posFita
    
    def setPosFita(self, pos):
        if type(pos) == type(1):
            self.posFita = pos

    def setSimbulo(self, letra):
        if type(letra) == type(""):
            self.F[self.posFita] = letra
    

