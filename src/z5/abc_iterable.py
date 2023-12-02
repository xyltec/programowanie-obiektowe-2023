from collections.abc import Iterable


class IT(Iterable):

    def __init__(self, s: str):
        self.s = s

    def __iter__(self):
        self.at = 0  # jakaś informacja o tym gdzie jesteśmy w iteracji
        return self

    def __next__(self):
        if self.at >= len(self.s):
            raise StopIteration
        ret = self.s[self.at]
        self.at += 1
        return ret


z = IT('abcdef')

for c in z:
    print(c)

