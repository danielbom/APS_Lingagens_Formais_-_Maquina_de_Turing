#ifndef TURING_H
#define TURING_H
#include "fita/fita.h"
#include "FuncaoTransicao/FuncaoTransicao.h"
#include <set>

class MaquinaDeTuring{
private:
    fita *F;
    /// std::set< std::string > Conjunto_de_estados;
    // Conjunto de simbulos de entrada é um subconjunto do Conjunto_de_simbulos_da_fita
    /// std::set< std::string > Conjunto_de_simbulos_da_fita;
    std::set< std::string > Conjunto_de_simbulos_de_entrada; /// Nao tenho certeza do que colocar aki
    // Funcao_transicao mantem Conjunto_de_estados(Vertices) e Conjunto_de_simbulos_da_fita(Pesos) - Gerenciador destes conjuntos
    FuncoesTransicao Conjunto_de_transicoes;

    std::string Estado_inicial;

    std::set< std::string > Conjunto_de_estados_finais; // Subconjunto de Conjunto_de_Estados

    std::string Entrada;

protected:

public:
    // Constructor
    MaquinaDeTuring(){ }
    // Destructor
    ~MaquinaDeTuring(){ }

    // gets/sets
    void Definir_Estado_inicial(std::string E){
        Estado_inicial = E;
    }
    void Definir_Estado_final(std::string E){
        Conjunto_de_estados_finais.insert(E);
    }
    void Adicionar_Transicao(std::string EstadoAtual, std::string Condicao, std::string Alteracao, std::string ProximoEstado, Direcao direcao){
        Conjunto_de_transicoes.inserir(EstadoAtual, Condicao, Alteracao, ProximoEstado, direcao);
    }
    bool Executar(){
        std::list< std::string > LS;
        std::string x;
        for(std::string::iterator it = Entrada.begin(); it != Entrada.end(); it++){
            x.push_back(*it);
            LS.push_back(x);
            x.pop_back();
        }

        F = new fita(LS);

        bool executando = true;
        std::string EstadoAtual = Estado_inicial;
        std::pair< std::string, std::pair< std::string, Direcao > > retorno;

        while(executando){
            retorno = Conjunto_de_transicoes.BuscaTransicao( EstadoAtual , F->getSimbulo() ) ;
            //std::cout << EstadoAtual << std::endl;
            //std::cout << retorno.first << " " << retorno.second.first << std::endl << std::endl;
            if(retorno.second.first == ""){
                executando = false;
            }
            else { // Se existe transição, então
                // Altera o valor do estado atual para o valor da transição
                F->setFita(retorno.first);
                // Estado atual recebe proximo estado
                EstadoAtual = retorno.second.first;
                // Movimenta ponteiro da fita
                F->movimenta(retorno.second.second);
            }
        }

        delete F;


        if(Conjunto_de_estados_finais.find(EstadoAtual)==Conjunto_de_estados_finais.end())
            return false;
        return true;
    }
    void Definir_entrada(std::string E){
        Entrada = E;
    }
};

#endif // TURING_H
