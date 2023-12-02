class Door:
    # to jest "interface"
    def open(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class ElectricDoor(Door):
    # implementacje interfejsu
    def __init__(self):
        self.charge = 10
        self.opened = False

    def open(self):
        super().open()
        self.charge -= 1
        self.opened = True
