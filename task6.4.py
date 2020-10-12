'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print('Машина повернула {}'.format(direction))

    def show_speed(self):
        print('Скорость автомобиля - {} км/ч'.format(self.speed))


class TownCar(Car):
    # def __init__(self, speed, color, name, is_police):
    #     super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            print('Внимание: ПРЕВЫШЕНИЕ СКОРОСТИ!')


class SportCar(Car):
    # def __init__(self, speed, color, name, is_police):
    #     super().__init__(speed, color, name, is_police)
    pass


class WorkCar(Car):
    # def __init__(self, speed, color, name, is_police):
    #     super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            print('Внимание: ПРЕВЫШЕНИЕ СКОРОСТИ!')


class PoliceCar(Car):
    # def __init__(self, speed, color, name, is_police):
    #     super().__init__(speed, color, name, is_police)
    pass


c = Car(10, 'black', 'BMW', False)
print(c.speed, c.color, c.name, c.is_police)
c.go()
c.stop()
c.turn('Left')
c.show_speed()
print('_'*30)
s = SportCar(250, 'red', 'Ferrari', False)
print(s.speed, s.color, s.name, s.is_police)
s.go()
s.stop()
s.turn(None)
s.show_speed()
print('_'*30)
t = TownCar(70, 'green', 'Fiat', False)
print(t.speed, t.color, t.name, t.is_police)
t.go()
t.stop()
t.turn(None)
t.show_speed()
print('_'*30)
w = WorkCar(55, 'yelloow', 'Scoda', False)
print(w.speed, w.color, w.name, w.is_police)
w.go()
w.stop()
w.turn(None)
w.show_speed()
print('_'*30)
p = PoliceCar(35, 'white', 'Reno', True)
print(p.speed, p.color, p.name, p.is_police)
p.go()
p.stop()
p.turn('Right')
p.show_speed()