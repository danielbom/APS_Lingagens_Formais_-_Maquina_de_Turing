#include <iostream>
#include "FuncaoTransicao.h"

int main (){
    FuncaoTransicao FT;
    FT.addTransicao("Q0", "R", "Q1", Direita);
    std::pair< std::string, Direcao > retorno = FT.BuscaTransicao("Q0", "R");
    std::cout << retorno.first << " " << retorno.second << std::endl;

    return 0;
}
