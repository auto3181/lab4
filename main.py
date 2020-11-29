import classes  # файл с классами


# Вызов функций для примера работы программы


obj_car = classes.Car()
obj_car.move(16)
obj_car.refill()
print('Остаток топлива в автомобиле:', obj_car.get_fuel(), 'Выручка автомобиля: ', obj_car.profit())
obj_taxi = classes.Taxi()
obj_taxi.move(64)
print('Выручка такси:', obj_taxi.profit())
obj_bus = classes.Bus()
obj_bus.take_places(32)
print('Свободные места в автобусе:', obj_bus.get_free_places())
obj_tram = classes.Tram()
obj_tram.move(128)
obj_tram.take_places(128)
print('Выручка трамвая:', obj_tram.profit(), ', Остаток топлива:', round(obj_tram.get_fuel()))
obj_airbus = classes.Airbus()
obj_airbus.take_places(256)
obj_airbus.ultra_speed_mode(16)
print('Остаток топлива в самолете:', obj_airbus.get_fuel(),
      ', Свободные места в самолёте:', obj_airbus.get_free_places(),
      ', Пройденное самолётом расстояние: ', obj_airbus.get_position())
classes.show_info(obj_car)
classes.show_info(obj_taxi)
classes.show_info(obj_bus)
classes.show_info(obj_tram)
classes.show_info(obj_airbus)
