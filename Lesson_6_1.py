from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = 'Красный'

    def running(self):
        print(self.__color)
        sleep(7)
        self.__color = 'Жёлтый'
        print(self.__color)
        sleep(2)
        self.__color = 'Зеленый'
        sleep(3)
        print(self.__color)


point = TrafficLight()
point.running()
