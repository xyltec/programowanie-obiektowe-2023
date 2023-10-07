# Klasa --- ma "pola" (fields) i "metody/funkcje"
from random import randint


class Robot:

    def __init__(self, name: str):
        print('uruchamiam konstruktor klasy A')
        self.name = name  # pole
        self.robot_id = randint(0, 100000)  # pole, ale nie będące argumentem konstuktora

    def foo(self):  # metoda
        name = 'Kadabra'
        return f'my name is {self.name}'

    def fill(self, content_type: str, content_amount: float):  # metoda z argumentami
        pass

    def add(self, a: int, b: int):
        return a + b


# tworzenie instancji
a = Robot('Xiao')  # tworzenie instancji

b = Robot('Li')  # tworzenie drugiej instancji

print(a.foo())
print(b.foo())

a.fill('cola', 12.0)  # wywołanie  metody z argumentami
