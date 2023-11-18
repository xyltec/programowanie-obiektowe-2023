class Door:
    def open(self):
        pass

    def close(self):
        pass


class ElectricDoor(Door):
    def __init__(self):
        self.charge = 10
        self.opened = False

    def open(self):
        super().open()
        self.charge -= 1
        self.opened = True
