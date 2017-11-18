#include <iostream>
#include "fita.h"

int main () {
    fita teste ;
    std::cout << teste.getSimbulo() << std::endl;
    for(int i = 0; i<10; i++){
        teste.paraEsquerda();
        std::cout << teste.getTam() << "  " ;
        if(teste.getSimbulo() == "")
            std::cout << "NULL ";
        else
            std::cout << teste.getSimbulo();
        std::cout << std::endl;
    }
    return 0;
}
