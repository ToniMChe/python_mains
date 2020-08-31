class Road:

    def __init__(self, width, length):
        self.width = int(width)
        self.length = int(length)
        self.__weight_asphalt = 25
        self.__fat_of_asphalt = 5
        self.__need_in_asphalt = 0

    def count_salary(self):
        self.__need_in_asphalt = self.width * self.length * self.__weight_asphalt * self.__fat_of_asphalt / 1000
        self.__need_in_asphalt = round(self.__need_in_asphalt)
        print("{}м * {}м * {}кг * {}см = {}т"
              .format(self.width, self.length, self.__weight_asphalt, self.__fat_of_asphalt, self.__need_in_asphalt))

    def display_road(self):
        print("Длина: {}, Ширина: {}".format(self.length, self.width))


road_66 = Road(5000, 20)
road_66.count_salary()
road_66.display_road()
