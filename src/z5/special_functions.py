from collections.abc import Container, Collection


class NiceNumbers():

    def __init__(self, numbers: Collection[int]):
        self.numbers = numbers

    def __getitem__(self, item):
        if item in self.numbers:
            return 1
        else:
            return 0


nn = NiceNumbers([1, 2, 3, 4, 5])
print(nn[3])

# nn[5] = 12 # needs __setitem__