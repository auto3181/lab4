class Car:
    """
    Машина, умеет ездить, каждые 10 клеток теряет единицу топлива,
    объем бака равен 20.
    """

    name = 'Авто'

    def __init__(self):
        self.money = 0
        self.pos = 0
        self.fuel = 20
        self.consumption = 1

    def move(self, direction):
        self.pos += direction
        while direction >= 10:
            self.fuel -= self.consumption
            direction -= 10

    def refill(self, fuel=20):
        if self.fuel + fuel <= 20:
            self.fuel += fuel
        else:
            self.fuel = 20

    def get_position(self):
        return self.pos

    def get_fuel(self):
        return self.fuel

    def profit(self):
        return 0


class Taxi(Car):
    name = 'Такси'

    def __init__(self):
        super().__init__()
        self.money = 0
        self.cost = 20
        self.pos = 0
        self.fuel = 20
        self.consumption = 2

    def profit(self):
        self.money += self.cost * self.pos
        return self.money


class Bus(Car):
    name = 'Автобус'
    occupied_places = 0

    def __init__(self):
        super().__init__()
        self.money = 0
        self.cost = 2
        self.pos = 0
        self.places = 51
        self.fuel = 50
        self.consumption = 5

    def take_places(self, count):
        self.occupied_places = count
        if self.occupied_places > self.places:
            self.occupied_places = self.places
            self.places = 0
        else:
            self.places -= self.occupied_places

    def profit(self):
        self.money += self.cost * self.occupied_places
        return self.money

    def get_free_places(self):
        return self.places


class Tram(Bus):
    name = 'Трамвай'

    def __init__(self):
        super().__init__()
        self.money = 0
        self.cost = 3
        self.pos = 0
        self.places = 150
        self.fuel = 10
        self.consumption = 0.5


class Airbus(Bus):
    name = 'Самолёт'

    def __init__(self):
        super().__init__()
        self.money = 0
        self.cost = 30
        self.pos = 0
        self.places = 300
        self.fuel = 10000
        self.consumption = 50

    def ultra_speed_mode(self, direction):
        self.pos += 7 * direction
        while direction >= 10:
            self.fuel -= 3 * self.consumption
            direction -= 10


def show_info(input_obj):
    input_obj.profit()
    print('Информация о', input_obj.name, input_obj.__dict__)
