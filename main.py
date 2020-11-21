class Car:  # Машина, умеет ездить, каждые 10 клеток теряет единицу топлива, объем бака равен 20
    def __init__(self):
        Car.pos = 0
        Car.fuel = 20
    def move(self, direction):
        Car.pos += direction
        while direction >= 10:
            Car.fuel -= 1
            direction -= 10
    def refill(self, fuel):
        if Car.fuel+fuel <= 20:
            Car.fuel += fuel
        else:
            Car.fuel = 20
    def getPosition(self):
        print(Car.pos)
    def getFuel(self):
        print(Car.fuel)


car1 = Car()
car1.move(20)
car1.refill(4)
car1.getPosition()
car1.getFuel()