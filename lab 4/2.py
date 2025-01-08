import modul
import mod
a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
c = input('выберите операцию "сложение", "вычитание", "умножение", "деление": ')
if c.lower() == 'сложение':
    print(modul.sum(a,b))
elif c.lower() == "вычитание":
    print( modul.sub(a,b))
elif c.lower() == "умножение":
    print(mod.ymn(a,b))
elif c.lower() == "деление":
    print(mod.dil(a,b))
else:
    print('нет данной операции')



