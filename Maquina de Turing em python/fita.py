
class fita(object):
    def __init__(self, entrada = "", espB = "") :
        self.F = []
        self.limite = 500
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
            self.F.append(self.EspB) # insere espaço branco no fim
    def Desloque_a_Esquerda(self):
        if self.limite == len(self.F):
            print("Limite da fita alcancado!")
            pass

        if self.posFita == 0:
            self.F.insert(0, self.EspB) # insere espaço branco no inicio
        else:
            self.posFita -= 1
    def imprimirFita(self):
        print(self.F)
    def getTam(self):
        return len(self.F)

    # Funções úteis
    def definirEntrada(self, entrada):
        self.F.clear()
        for letra in entrada:
            self.F.append(letra)
    def getSimbulo(self):
        return self.F[self.posFita]
    def setSimbulo(self, letra):
        if type(letra) == type(""):
            self.F[self.posFita] = letra
    def movimenta(self, direcao):
        if direcao == "D":
            self.Desloque_a_Direita()
        elif direcao == "E":
            self.Desloque_a_Esquerda()
