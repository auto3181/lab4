class Car:  # Машина, умеет ездить, каждые 10 клеток теряет единицу топлива, объем бака равен 20, число мест
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

    def refill(self, fuel):
        if self.fuel + fuel <= 20:
            self.fuel += fuel
        else:
            self.fuel = 20

    def getPosition(self):
        return self.pos

    def getFuel(self):
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
    occupPlaces = 0

    def __init__(self):
        super().__init__()
        self.money = 0
        self.cost = 2
        self.pos = 0
        self.places = 51
        self.fuel = 50
        self.consumption = 5

    def takePlaces(self, count):
        self.occupPlaces = count
        if self.occupPlaces > self.places:
            self.occupPlaces = self.places
            self.places = 0
        else:
            self.places -= self.occupPlaces

    def profit(self):
        self.money += self.cost * self.occupPlaces
        return self.money

    def getFreePlaces(self):
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

    def ultraSpeedMode(self, direction):
        self.pos += 7 * direction
        while direction >= 10:
            self.fuel -= 3 * self.consumption
            direction -= 10


def showInfo(input_obj):
    input_obj.profit()
    print('Информация о', input_obj.name, input_obj.__dict__)


# Вызов функций для примера работы программы


C = Car()
C.move(16)
print('Остаток топлива в автомобиле:', C.getFuel(), 'Выручка автомобиля: ', C.profit())
T = Taxi()
T.move(64)
print('Выручка такси:', T.profit())
B = Bus()
B.takePlaces(32)
print('Свободные места в автобусе:', B.getFreePlaces())
Tr = Tram()
Tr.move(128)
Tr.takePlaces(128)
print('Выручка трамвая:', Tr.profit(), ', Остаток топлива:', round(Tr.getFuel()))
A = Airbus()
A.takePlaces(256)
A.ultraSpeedMode(16)
print('Остаток топлива в самолете:', A.getFuel(),
      ', Свободные места в самолёте:', A.getFreePlaces(),
      ', Пройденное самолётом расстояние: ', A.getPosition())
showInfo(C)
showInfo(T)
showInfo(B)
showInfo(Tr)
showInfo(A)
