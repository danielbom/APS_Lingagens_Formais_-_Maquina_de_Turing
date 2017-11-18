#ifndef TRANSICAO
#define TRANSICAO
#include <map>
#include <list>
#include <set>
#include <string>



// Aplica��o semelhante a um grafo direcionado (d�grafo)
typedef std::map< std::string, std::set< std::pair< std::string , std::pair< std::string, std::pair< std::string, Direcao > > > > >::iterator itTransicao;
typedef std::set< std::pair< std::string , std::pair< std::string, std::pair< std::string, Direcao > > > >::iterator itListaTransicao;
class FuncoesTransicao{
private:
    std::set< std::string > Conjunto_de_estados; // Vertices;
    // Cada estado possui uma lista de transi��o
    // Cada transi��o possui condicao e a��o
    // Cada a��o � representada por estado, direcao e alteracao
    std::map< std::string, std::set< std::pair< std::string , std::pair< std::string, std::pair< std::string, Direcao > > > > > Transicoes; // Arestas

    std::set< std::string > Conjunto_de_simbulos_da_fita; // Pesos;
protected:

public:
    // Constructor
    FuncoesTransicao(){
        Conjunto_de_simbulos_da_fita.insert("");
    }
    // Destructor
    ~FuncoesTransicao(){ }
    // gets / sets
    std::set< std::string > &getConjunto_de_estados(){
        return Conjunto_de_estados;
    }
    std::set< std::string > &getConjunto_de_simbulos_da_fita(){
        return Conjunto_de_simbulos_da_fita;
    }
    // Funcoes
    void inserir(std::string EstadoAtual, std::string Condicao, std::string Alteracao, std::string ProximoEstado, Direcao direcao){
        // Condi��o � um simbulo da fita
        // Insere os estados no Conjunto_de_estados caso eles nao existam
        Conjunto_de_estados.insert(EstadoAtual);
        Conjunto_de_estados.insert(ProximoEstado);

        // Adiciona a transi��o
        Transicoes[EstadoAtual].insert(std::make_pair(Condicao, std::make_pair(Alteracao, std::make_pair(ProximoEstado, direcao))));

        // Insere simbulos no Conjunto_de_simbulos caso eles nao existam
        Conjunto_de_simbulos_da_fita.insert(Condicao);
    }

    std::pair< std::string , std::pair< std::string, Direcao > > BuscaTransicao(std::string EstadoAtual, std::string Condicao){
        itTransicao itT = Transicoes.find(EstadoAtual); // Lista de transi��es do EstadoAtual
        if(itT == Transicoes.end()) // Se o estado nao existe
            return std::make_pair("", std::make_pair("",Mantem));

        itListaTransicao itLT;
        // Busca na lista de transi��es a condi��o requerida
        for(itLT = itT->second.begin(); itLT != itT->second.end() && itLT->first != Condicao; itLT++) ;
        if(itLT == itT->second.end()) // Se n�o existe a condi��o
            return std::make_pair("", std::make_pair("",Mantem));

        return itLT->second;
    }

};
#endif // TRANSICAO
