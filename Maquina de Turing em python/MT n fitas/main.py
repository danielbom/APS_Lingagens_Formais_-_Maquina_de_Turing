import MTnfitas as MT
import LeitorArquivo as LA
import sys

def main():
    if len(sys.argv) < 3:
        print("Parametros insuficientes. Informe o nome de arquivo de entrada (.txt)")
        sys.exit(1)
    la = LA.LeitorArquivo(sys.argv[1])
    m = MT.MTnfitas(la.getQuantidadeDeFitas())
    m.DefinirEspacoBranco(la.getEspacoBrancoFita())
    m.DefinirEstadoInicial(la.getEstadoInicial())
    m.addEstadoFinal(la.getEstadoAceitacao())
    ts = la.getTransicoes()
    for i in ts:
        m.addTransicao(i[0],i[1],i[2],i[3],i[4])
    m.DefinirEntrada(sys.argv[2])

    print(m.executar())














if __name__ == "__main__":
    main()





