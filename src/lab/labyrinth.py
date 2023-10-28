from uuid import uuid4


def get_random_id():
    return str(uuid4())[:4]


class Labyrinth:

    def __init__(self):
        self.entries = set()

    def mark_entry(self, room_id):
        pass



class Room:
    def __init__(self, room_id):
        if room_id is None:
            self.room_id = get_random_id()
        else:
            self.room_id = room_id

    def get_neighboring_rooms(self) -> list['Room']:
        """
        All rooms linked to self by a door.
        """
        pass


class Actor:

    def __init__(self, initial_position: Room):
        self.position = initial_position

    def go_to_room(self, room_id: str):
        # can go only to neighbors of self.position
        pass

if __name__ == '__main__':
    print(get_random_id())
