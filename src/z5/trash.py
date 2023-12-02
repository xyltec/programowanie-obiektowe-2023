from collections.abc import Sized, Container


class Trash(Sized, Container):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.trash = {}
        self.__create_trash()

    def __create_trash(self):
        self.trash = [0 for _ in range(self.capacity)]

    def __getitem__(self, item):
        return self.trash[item]

    def __setitem__(self, key, value):
        self.trash[key] = value

    def __delitem__(self, key):
        del self.trash[key]
        #todo testme

    def __repr__(self):
        return str(self.trash)

    def __len__(self):
        return len(self.trash)

    def __contains__(self, __x):
        return __x in self.trash


trash = Trash(10)
trash[5] = 17
trash[9] = 5
print(trash)
print(5 in trash)
del trash[5]
print(trash)
