from duo_deque import duo_deque
from colorama import init, Fore, Back, Style


class tape(object):
    def __init__(self, input=' ', blank_space=' '):
        self.blank_space = blank_space
        self._list = duo_deque()
        self.set_input(input)
        self.head = self._list.begin()

    def set_input(self, input):
        for i in list(input):
            self._list.append(i)

    def left(self):
        if not self.head.prev:
            self._list.appendleft(self.blank_space)
        self.head = self.head.prev

    def right(self):
        if not self.head.next:
            self._list.append(self.blank_space)
        self.head = self.head.next

    def set_head(self, symbol):
        self.head.value = symbol

    def print(self):
        init(convert=True)
        print(end='\t')
        for i in self._list:
            print(Fore.BLUE + str(i)
                  if i is not self.head
                  else Fore.RED + str(i), end='')
        print(Fore.WHITE, end='')

    def __repr__(self):
        return ''.join([i.value for i in self._list])

    def __str__(self):
        return ''.join([Fore.WHITE] + [Fore.BLUE + str(i)
                                       if i is not self.head
                                       else Fore.RED + str(i) for i in self._list] + [Fore.WHITE])

    ''' Stranges functions below '''

    def dup(self):
        return [self._list.copy(), self.head]

    def restore(self, dup_repr):
        self._list = dup_repr[0]
        self.head = dup_repr[1]
