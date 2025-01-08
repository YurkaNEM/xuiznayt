import datetime
a = input('узнать время, введите "да" или "нет": ')
if a.lower() == 'да':
    print(str(datetime.datetime.now()))
elif a.lower() == "нет" :
    print("как хочешь")
else:
    print("непонятные символы")
