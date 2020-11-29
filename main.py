import classes  # файл с классами


# Вызов функций для примера работы программы


obj_car = classes.Car()
obj_car.move(16)
obj_car.refill()
print('Остаток топлива в автомобиле:', obj_car.getFuel(), 'Выручка автомобиля: ', obj_car.profit())
obj_taxi= classes.Taxi()
obj_taxi.move(64)
print('Выручка такси:', obj_taxi.profit())
obj_bus = classes.Bus()
obj_bus.takePlaces(32)
print('Свободные места в автобусе:', obj_bus.getFreePlaces())
obj_tram = classes.Tram()
obj_tram.move(128)
obj_tram.takePlaces(128)
print('Выручка трамвая:', obj_tram.profit(), ', Остаток топлива:', round(obj_tram.getFuel()))
obj_airbus = classes.Airbus()
obj_airbus.takePlaces(256)
obj_airbus.ultraSpeedMode(16)
print('Остаток топлива в самолете:', obj_airbus.getFuel(),
      ', Свободные места в самолёте:', obj_airbus.getFreePlaces(),
      ', Пройденное самолётом расстояние: ', obj_airbus.getPosition())
classes.showInfo(obj_car)
classes.showInfo(obj_taxi)
classes.showInfo(obj_bus)
classes.showInfo(obj_tram)
classes.showInfo(obj_airbus)
