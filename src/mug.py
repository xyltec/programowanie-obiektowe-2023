class Mug:

    def __init__(self, color: str, capacity: float) -> None:
        self.capacity = capacity
        self.color = color
        self.NOTHING = 'NOTHING'
        self.content_type = self.NOTHING
        self.content_amount = 0

    def get_content_type(self):
        # funkcje zwracające wartości pól często nazywane są "getterami"
        return self.content_type

    def get_content_amount(self):
        return self.content_amount

    def fill(self, content_type: str, content_amount: float):
        if content_type != self.content_type and self.content_type != self.NOTHING:
            raise RuntimeError('Cannot fill the mug with a different type of fluid than already present')

        if content_amount < 0:
            raise RuntimeError('Cannot fill with negative amout of fluid')

        transferred = min(self.capacity - self.content_amount, content_amount)
        self.content_amount += transferred
        if transferred != content_amount:
            raise RuntimeError('Mug overflow')

    def pour_out_liquid(self, requested_amount: float):
        transferred = min(requested_amount, self.content_amount)
        self.content_amount -= transferred
        transferred_type = self.content_type

        if self.content_amount==0:
            self.content_type = self.NOTHING

        return transferred_type, transferred


