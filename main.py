class Car:  # Машина, умеет ездить, каждые 10 клеток теряет единицу топлива, объем бака равен 20, число мест
    def __init__(self):
        self.pos = 0
        self.fuel = 20
        self.consumption = 1
        self.places = 5
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
    def __init__(self):
        self.money = 0
        self.kilometersCost = 20
        self.places = 4
        self.pos = 0
        self.fuel = 20
        self.consumption = 2
    def profit(self):
        self.money += self.kilometersCost * self.pos
        return self.money


class Bus(Car):
    occupPlaces = 0
    def __init__(self):
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
        self.money += self.cost*self.occupPlaces
        return self.money

    def getFreePlaces(self):
        return self.places


class Tram(Bus):
    def __init__(self):
        self.money = 0
        self.cost = 3
        self.pos = 0
        self.places = 150
        self.fuel = 10
        self.consumption = 0.5


class Airbus(Bus):
    def __init__(self):
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
    print('Информация об объекте:', input_obj.__dict__)


C = Car()
C.move(11)
print('Топливо =', C.getFuel())
A = Airbus()
A.move(20)
A.ultraSpeedMode(1)
A.takePlaces(200)
T = Tram()
T.takePlaces(300)
showInfo(A)
showInfo(T)
