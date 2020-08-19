types = ['1', 100.5, 'список', 1]

for index, item in enumerate(types):
    type_of_element = type(item)
    print("Тип элемента {}: {}" .format(index, type_of_element))
