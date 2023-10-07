# Klasa --- ma "pola" (fields) i "metody/funkcje"
class Robot:

    def __init__(self, name: str):
        print('uruchamiam konstruktor klasy A')
        self.name = name  # pole

    def foo(self):  # metoda
        name = 'Kadabra'
        return f'my name is {self.name}'

    def add(self, a: int, b: int):
        return a + b


# tworzenie instancji
a = Robot('Xiao')  # tworzenie instancji

b = Robot('Li')  # tworzenie drugiej instancji


print(a.foo())
print(b.foo())