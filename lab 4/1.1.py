import math
num = int(input("введите число: "))
if num > 0:
    print ("квадратный корень числа: " + str(math.sqrt(num)))
else:
    print ("число меньше нуля и корень нельзя найти")
