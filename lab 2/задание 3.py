def max_two(a, b):
    if a > b:
        print("Большее:", a)
    elif a < b:
        print ("Большее:", b)
    elif a == b:
        print("числа одинаковы")
max_two(a = int(input("Введите число: ")), b = int(input("Введите число: ")))

