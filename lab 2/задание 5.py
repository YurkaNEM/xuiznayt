def is_prime(a):
    for i in range(2, int(a**0.5) +1):
        if a % i:
            return print("число простое")
        else:
            return print("число не является простым")
is_prime(a = int(input("Введите число: ")))
