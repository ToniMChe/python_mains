rating = [7, 5, 3, 3, 2]

while True:
    element_of_rating = int(input("Введите новый элемент рейтинга\
     (0, чтобы прекратить):"))
    if element_of_rating == 0:
        break
    rating.append(element_of_rating)
    rating.sort(reverse=True)
    print(rating)
