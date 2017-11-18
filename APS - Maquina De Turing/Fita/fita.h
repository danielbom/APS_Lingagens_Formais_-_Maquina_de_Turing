#ifndef FITA_H
#define FITA_H
#include <list>
#include <string>

enum Direcao{ Esquerda, Direita, Mantem };

class fita{
private:
    std::list< std::string > F;
    std::list< std::string >::iterator posFita ;
    int limiteFita = 500;
    void Desloque_a_Direita(){
        if(limiteFita == F.size()){
            std::cout << "Limite de fita alcançado ! \n";
            return;
        } // Só por precaução - caso exista um estado que gere transação infinita
        posFita++;
        if(posFita == F.end()){
            posFita--;
            F.push_back("");
            posFita++;
        }
    }
    void Desloque_a_Esquerda(){
        if(limiteFita == F.size()){
            std::cout << "Limite de fita alcançado ! \n";
            return;
        } // Só por precaução - caso exista um estado que gere transação infinita
        if(posFita == F.begin()){
            F.push_front("");
        }
        posFita--;
    }
protected:

public:
    // Constructor
    fita(){
        F.push_back(""); // Fita inicializada com uma palavra vazia [NULL]
        posFita = F.begin();
    }
    fita(std::list< std::string > inicializador){
        if (inicializador.size() == 0) {
            F.push_back("");
            posFita = F.begin();
            return ;
        }
        std::list< std::string >::iterator itLS;
        for(itLS = inicializador.begin(); itLS != inicializador.end(); itLS++)
            F.push_back(*itLS);

        posFita = F.begin();
    }

    // Destructor
    ~fita(){
        std::list< std::string >::iterator itLS;
        while(!F.empty())
            F.pop_back();
    }

    // gets / sets
    std::string getSimbulo(){
        return *posFita;
    }
    int getTam(){
        F.size();
    }
    void setFita(std::string E){
        *posFita = E;
    }

    // Funções
    void movimenta(Direcao direcao){
        if(direcao == Direita)
            Desloque_a_Direita();
        else if (direcao == Esquerda)
            Desloque_a_Esquerda();
    }
};

#endif // FITA_H
