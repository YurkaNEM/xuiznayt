x = 0
while x == 0:
    try:
        place = str(input('введите название файла: '))
        file = open(place + '.txt', encoding='utf-8')
        print(file.read())
        break
    except FileNotFoundError:
        print("произошла ошибка, повторите попытку")
