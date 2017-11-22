#include <iostream>
#include "MaquinaDeTuring.h"

int main() {
    MaquinaDeTuring MT;
    // Automato para a^(2^n)... isto é, quantidade de a em potencia de 2; a(0), aa(1), aaaa(2), aaaaaaaa(3), ...
    //MT.Adicionar_Transicao(Atual , Condicao , Alter , Prox , Direcao);
    MT.Adicionar_Transicao("q0" , "#" , "#" , "q0" , Direita);
    MT.Adicionar_Transicao("q0" , "a" , "#" , "q1" , Direita);

    MT.Adicionar_Transicao("q1" , "#" , "#" , "q1" , Direita);
    MT.Adicionar_Transicao("q1" , "a" , "a" , "q3" , Direita);
    MT.Adicionar_Transicao("q1" , "" , "" , "q2" , Esquerda);

    MT.Adicionar_Transicao("q3" , "#" , "#" , "q3" , Direita);
    MT.Adicionar_Transicao("q3" , "a" , "#" , "q4" , Direita);
    MT.Adicionar_Transicao("q3" , "" , "" , "q5" , Esquerda);

    MT.Adicionar_Transicao("q4" , "#" , "#" , "q4" , Direita);
    MT.Adicionar_Transicao("q4" , "a" , "a" , "q3" , Direita);

    MT.Adicionar_Transicao("q5" , "a" , "a" , "q5" , Esquerda);
    MT.Adicionar_Transicao("q5" , "#" , "#" , "q5" , Esquerda);
    MT.Adicionar_Transicao("q5" , "" , "" , "q0" , Direita);

    MT.Definir_Estado_final("q2");
    MT.Definir_Estado_inicial("q0");
    MT.Definir_entrada("aaaa");
    if(MT.Executar()){
        std::cout << "Quantidade de 'a' igual a 2^n\n";
    }
    else {
        std::cout << "Quantidade de 'a' NAO eh igual a 2^n\n";
    }

    MT.Definir_entrada("aaa");
    if(MT.Executar()){
        std::cout << "Quantidade de 'a' igual a 2^n\n";
    }
    else {
        std::cout << "Quantidade de 'a' NAO eh igual a 2^n\n";
    }
    return 0;
}
