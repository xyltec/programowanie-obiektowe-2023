from dataclasses import dataclass
from random import randint
from uuid import UUID, uuid4


@dataclass
class Obywatel:
    name: str
    id: int = randint(0, 10 ** 2)


@dataclass
class Buerger:
    name: str
    id: UUID = uuid4()


def create_instance(name: str, selected_class: type) -> Obywatel | Buerger:
    print(type(selected_class))
    inst = selected_class(name)
    return inst


if __name__ == '__main__':
    a = create_instance('kadabra', Buerger)
    print(a)
    c = create_instance('abra', Obywatel)
    print(c)