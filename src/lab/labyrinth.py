from enum import Enum
from uuid import uuid4


def get_random_id():
    return str(uuid4())[:4]


class RoomType(Enum):
    ENTRY = 1
    EXIT = 2
    BONUS = 3


class Room:
    def __init__(self, room_id):
        if room_id is None:
            self.room_id = get_random_id()
        else:
            self.room_id = room_id

        self.__neighbors: set[str] = set()

    def get_neighbors_ids(self) -> list[str]:
        """
        All rooms linked to self by a door.
        """
        pass

    def add_neighbor_id(self, neighbor: 'Room'):
        pass

    def remove_neighbor_id(self, neighbor: 'Room'):
        pass


class Actor:

    def __init__(self, start_room_id: str):
        self.position = start_room_id

    def go_to_room(self, room_id: str):
        # can go only to neighbors of self.position
        pass

    def get_current_room_id(self) -> str:
        pass


class Labyrinth:
    """
    Global set of rooms and actors with some global traits (which ones are "entry/exit" etc.)

    _also_ plays the role of the "engine" (rooms/actors should only change their attributes via methods
    of this class).

    Note:
        - an elaborate _wrapper_; does not expose objects of type Actor or Room or their functions (effectively
          filters their API)

    Also: https://en.wikipedia.org/wiki/Cube_(1997_film)
    " It consists of an outer cubical shell or sarcophagus, and the inner cube rooms.
    Each side of the outer shell is 434 feet (132 m) long. The inner cube consists of 263 = 17,576 cubical rooms
    (minus an unknown number of rooms to allow for movement), each having a side length of 15.5 feet (4.7 m).
    A space of 15.5 feet (4.7 m) is between the inner cube and the outer shell.
    Each room is labelled with three identification numbers such as "517 478 565".
    These numbers encode the starting coordinates of the room, and the X, Y, and Z coordinates
    are the sums of the digits of the first, second, and third number, respectively.
    The numbers also determine the movement of the room.
    The subsequent positions are obtained by cyclically subtracting the digits from one another,
    and the resulting numbers are then successively added to the starting numbers."
    """

    def __init__(self):
        self.__rooms: dict[str, Room] = dict()
        self.__actors: dict[str, Actor] = dict()

    # Room manipulation methods

    def add_room(self, room: Room):
        pass

    def remove_room(self, room_id: str):
        pass

    def add_room_connection(self, room_id_1: str, room_id_2: str):
        pass

    def remove_room_connection(self, room_id_1: str, room_id_2: str):
        pass

    def add_room_attribute(self, room_id: str, attribute: RoomType):
        pass

    def has_room_attribute(self, room_id: str, attribute: RoomType):
        pass

    def remove_room_attribute(self, room_id: str, attribte: RoomType):
        pass

    # Actor manipulation methods

    def add_actor(self, actor: Actor):
        pass

    def remove_actor(self, actor_id: str):
        pass

    def move_actor(self, actor_id: str, target_room_id: str):
        pass


if __name__ == '__main__':
    pass
