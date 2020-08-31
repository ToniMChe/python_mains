class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}

    def worker_character(self):
        print("Имя: {}, фамилия: {},должность: {}, зарплата: {}."
              .format(self.name, self.surname, self.position,
                      self.__income))

    def all_income(self):
        return self.__income.values()


class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        super().__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        print("{} {}".format(self.name, self.surname))

    def get_total_income(self):
        print("Доход с увётом премии: {}".format(self.Worker.all_income))
