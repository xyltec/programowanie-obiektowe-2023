from uuid import uuid4, UUID

from loguru import logger


class Room:

    def __init__(self):
        logger.info('Creating a room')
        self.occupants = []
        self.room_id = uuid4()

    def get_id(self) -> UUID:
        return self.room_id

    def enter(self, actor: str):
        logger.info(f'Entering room {actor=}')
        self.occupants.append(actor)

    def leave(self, actor: str):
        logger.info('Leaving room')

    def get_occupants(self) -> list[str]:
        return []


class FixedCapacityRoom(Room):

    def __init__(self, capacity: int = 10):
        super().__init__()
        self.capacity = capacity

    def enter(self, actor: str):
        logger.info(f'Enterning fixed capacity room; current actor count: {len(self.occupants)}')
        if self.capacity == len(self.occupants):
            raise RuntimeError('Cannot enter; room full')


class TemperatureStabilizedRoom(Room):

    def __init__(self, expected_temperature: int):
        self.expected_temperature = expected_temperature
        super().__init__()

    def get_temperature(self):
        return self.expected_temperature

    def set_temperature(self, new_temperature: int):
        pass


class FreezerRoom(TemperatureStabilizedRoom, FixedCapacityRoom):

    def __init__(self, capacity: int, expected_temperature: int):
        FixedCapacityRoom.__init__(self, capacity=capacity)
        TemperatureStabilizedRoom.__init__(self, expected_temperature=expected_temperature)


#  -------------------------

class Item:
    def __init__(self, name: str):
        self.name = name
        self.item_id = uuid4()

    def __repr__(self):
        return f'[Item: {self.name}, {self.item_id}]'


class Inventory:

    def __init__(self):
        self.items: list[Item] = []

    def get_items(self) -> list[Item]:
        return self.items

    def get_item_by_id(self, item_id: UUID) -> Item | None:
        for it in self.items:
            if it.item_id == item_id:
                return it
        return None

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.append(item)


class ClassRoom(FixedCapacityRoom, Inventory):

    def __init__(self, capacity: int = 10):
        FixedCapacityRoom.__init__(self, capacity)
        Inventory.__init__(self)


def gg_freezer():
    r = FreezerRoom(capacity=2, expected_temperature=-10)
    r.enter('gg')
    logger.info(r.get_temperature())
    r.set_temperature(-20)
    logger.info(r.get_temperature())
    logger.info(r.get_id())


if __name__ == '__main__':
    # testujemy inventory
    krzeslo1 = Item('Krzesło1')
    krzeslo2 = Item('Krzesło2')

    croom = ClassRoom(10)
    croom.add_item(krzeslo1)
    croom.add_item(krzeslo2)

    print(croom.get_item_by_id(krzeslo1.item_id))
    print(croom.get_items())
    print(croom)

