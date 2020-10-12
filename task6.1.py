'''1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
 третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
 (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.'''


class TrafficLight:
    __colors = ['red', 'yellow', 'green']

    def running(self):
        from itertools import cycle
        from time import sleep

        colors_cyc = cycle(TrafficLight.__colors)
        for color in colors_cyc:
            if color == TrafficLight.__colors[0]:
                sleep(7)
            elif color == TrafficLight.__colors[1]:
                sleep(2)
            else:
                sleep(9)
            print(color)


t = TrafficLight()
t.running()
