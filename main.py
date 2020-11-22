import classes  # файл с классами


# Вызов функций для примера работы программы


C = classes.Car()
C.move(16)
C.refill()
print('Остаток топлива в автомобиле:', C.getFuel(), 'Выручка автомобиля: ', C.profit())
T = classes.Taxi()
T.move(64)
print('Выручка такси:', T.profit())
B = classes.Bus()
B.takePlaces(32)
print('Свободные места в автобусе:', B.getFreePlaces())
Tr = classes.Tram()
Tr.move(128)
Tr.takePlaces(128)
print('Выручка трамвая:', Tr.profit(), ', Остаток топлива:', round(Tr.getFuel()))
A = classes.Airbus()
A.takePlaces(256)
A.ultraSpeedMode(16)
print('Остаток топлива в самолете:', A.getFuel(),
      ', Свободные места в самолёте:', A.getFreePlaces(),
      ', Пройденное самолётом расстояние: ', A.getPosition())
classes.showInfo(C)
classes.showInfo(T)
classes.showInfo(B)
classes.showInfo(Tr)
classes.showInfo(A)
