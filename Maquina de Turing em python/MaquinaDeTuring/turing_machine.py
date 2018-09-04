from transitions import transitions
from tape import tape

from collections import deque
from colorama import init, Fore, Back, Style
from tabulate import tabulate
import os


class turing_machine(object):
    def __init__(self, all_transitions, begin_state, final_state, blank_space):
        self.all_transitions = all_transitions
        self.begin_state = begin_state
        self.final_state = final_state
        self.blank_space = blank_space

    def do_transition(self, tape, transition):
        # Altera a cabeça da fita
        tape.set_head(transition.new_symbol)
        # Movimenta a cabeça da fita
        if transition.direction == 'E' or transition.direction == 'L':
            tape.left()
        elif transition.direction == 'D' or transition.direction == 'R':
            tape.right()
        # Retorna o novo estado e o valor atual da cabeça
        return (transition.new_state, tape.head.value)

    def run(self, _input):
        os.system("cls")
        # Criando as estruturas que serão usadas
        _tape = tape(_input, self.blank_space)
        _transitions = transitions(self.all_transitions)
        queue = deque()
        #table = deque()
        table = []
        # Definindo o estado inicial
        state = self.begin_state
        symbol = _tape.head.value
        # Obtendo as transições apartir do estado inicial
        transition = _transitions.search(state, symbol)
        # Armazenando as transições e o estado da fita em uma fila
        for t in transition:
            queue.append([_tape.dup(), [t]])
        # Variáveis para evitar loop infinito ou execuções muito longas
        i = 0
        lim = 1000
        # Rodando
        while True:
            # Montando uma tabela para imprimir depois
            table.append([str(_tape), str(_tape.head), Fore.GREEN + state
                          if state == self.final_state else state])
            # Verificando se acabaram as transições
            if not transition:
                print("No transition break")
                break
            # Removendo um elemento da fila
            dup_repr_tape, transition = queue.popleft()
            # Restaurando o estado da fita
            _tape.restore(dup_repr_tape)
            # Realizando a transição
            state, symbol = self.do_transition(_tape, transition[0])
            # Buscando transições
            transition = _transitions.search(state, symbol)
            # Armazenando as transições e o estado da fita em uma fila
            for t in transition:
                queue.append([_tape.dup(), [t]])
            # Evitando execuções muito grandes
            if i == lim:
                if input("%d executions. Continue (Y/N)?", lim).upper() == "N":
                    break
                else:
                    lim *= 2
        # Verificando se parou por uma execução muito grande. Se não, imprime.
        if i != lim:
            init(convert=True)
            print(tabulate(table, headers=['Tape', 'head', 'State']))
            print(Fore.WHITE)
        return state == self.final_state
