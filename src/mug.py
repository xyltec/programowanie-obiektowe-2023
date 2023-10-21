class Mug:

    def __init__(self, color: str, capacity: float) -> None:
        self.capacity = capacity
        self.color = color
        self.NOTHING = 'NOTHING'
        self.__content_type = self.NOTHING
        self.__content_amount = 0

    def get_content_type(self):
        # funkcje zwracające wartości pól często nazywane są "getterami"
        return self.__content_type

    def get_content_amount(self):
        return self.__content_amount

    def fill(self, content_type: str, content_amount: float):
        """
        Fills mug some fluid.

        :param content_type:
        :param content_amount:
        :return:
        """
        if content_type != self.__content_type and self.__content_type != self.NOTHING:
            raise RuntimeError('Cannot fill the mug with a different type of fluid than already present')

        if content_amount < 0:
            raise RuntimeError('Cannot fill with negative amout of fluid')

        transferred = min(self.capacity - self.__content_amount, content_amount)
        self.__content_amount += transferred
        if transferred > 0:
            self.__content_type = content_type
        if transferred != content_amount:
            raise RuntimeError('Mug overflow')

    def pour_out_liquid(self, requested_amount: float):
        transferred = min(requested_amount, self.__content_amount)
        self.__content_amount -= transferred
        transferred_type = self.__content_type

        if self.__content_amount==0:
            self.__content_type = self.NOTHING

        return transferred_type, transferred


