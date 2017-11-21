
class fita(object):
    def __init__(self, entrada = "") :
        self.F = []
        self.limite = 500
        self.posFita = 0
        for letra in entrada:
            self.F.append(letra)

    def Desloque_a_Direita(self):
        if self.limite == len(self.F):
            print("Limite da fita alcancado!")
            pass

        self.posFita += 1
        if self.posFita == len(self.F):
            self.F.append("")
    def Desloque_a_Esquerda(self):
        if self.limite == len(self.F):
            print("Limite da fita alcancado!")
            pass

        if self.posFita == 0:
            self.F.insert(0, "")
    def imprimeFita(self):
        print(self.F)
    def getSimbulo(self):
        return self.F[self.posFita]
    def getTam(self):
        return len(self.F)

    def setSimbulo(self, letra):
        if type(letra) == type(""):
            self.F[self.posFita] = letra
    def movimenta(self, direcao):
        if direcao == "D":
            self.Desloque_a_Direita()
        elif direcao == "E":
            self.Desloque_a_Esquerda()
