from abc import ABC, abstractmethod, abstractproperty

class Box(ABC):

    @abstractproperty
    def box(self):

        pass

    @abstractmethod
    def add_pomade(self):
        pass

    @abstractmethod
    def add_ink(self):
        pass

    @abstractmethod
    def add_eyeliner(self):
        pass

    @abstractmethod
    def add_blush(self):
        pass

class Box1(Box):
    """Конкретный строитель, строящий бокс первого типа."""
    def __init__(self):
        self.reset()

    def reset(self):
        self._box = Boxx()

    @property
    def box(self):
        box = self._box
        return box

    def add_pomade(self):
        self._box.add("Помада", 1200)

    def add_ink(self):
        self._box.add("Тушь", 1500)

    def add_eyeliner(self):
        self._box.add("Подводка", 1750)

    def add_blush(self):
        self._box.add("Пудра", 1300)

    def add_all(self):
        self.add_pomade()
        self.add_ink()
        self.add_eyeliner()
        self.add_blush()


class Box2(Box):
    """Конкретный строитель, строящий бокс второго типа."""
    def __init__(self):
        self.reset()

    def reset(self):
        self._box = Boxx()

    @property
    def box(self):
        box = self._box
        return box

    def add_pomade(self):
        self._box.add("Помада", 900)

    def add_ink(self):
        self._box.add("Тушь", 1050)

    def add_eyeliner(self):
        self._box.add("Подводка", 799)

    def add_blush(self):
        self._box.add("Пудра", 810)

    def add_all(self):
        self.add_pomade()
        self.add_ink()
        self.add_eyeliner()
        self.add_blush()


class Boxx():
    def __init__(self):
        self.box = []
        self.sum = 0

    def add(self, dish, price):
        self.box.append(dish)
        self.sum += price

    def list_box(self):
        return f"{', '.join(self.box)}"

    def get_sum(self):
        return self.sum


if __name__ == '__main__':
    print('Предложение №1 ')
    order = Box1()
    order.add_pomade()
    order.add_blush()
    print(order.box.list_box())
    print('_______________________________')

    print('\nПредложение №2 ')
    order.reset()
    order.add_ink()
    order.add_eyeliner()
    print(order.box.list_box())
    print('_______________________________')

    print('\nПредложение №3 ')
    order = Box2()
    order.add_all()
    print(order.box.list_box())
    print('_______________________________')


