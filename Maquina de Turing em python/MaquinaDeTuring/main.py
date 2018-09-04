from turing_machine import turing_machine as tm
from colorama import init, Fore, Back, Style

if __name__ == "__main__":

    with open("fix_a.txt", 'r') as reader:
        txt = reader.read()
        txt = txt.split("\n")

        transitions = [i.split() for i in txt[7:-1]]
        initial_state = '0'
        final_state = txt[5]
        blank_space = txt[2]

        for i in transitions:
            print(i)

        m = tm(transitions, initial_state,
               final_state, blank_space)

    init(convert=True)
    inp = input("\nType an entry or exit: ")
    while inp != "exit":
        print("\t", Fore.GREEN + "True" + Fore.WHITE
              if m.run(inp) else Fore.RED + "False" + Fore.WHITE)
        inp = input("\nType an entry or exit: ")
    print(Fore.WHITE)
