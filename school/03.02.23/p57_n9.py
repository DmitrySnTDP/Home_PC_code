n=int(input('Введите номер месяца:'))
if n==1 or n==2 or n==12:
    print('Зима')
elif n>2 and n<6:
    print('Весна')
elif n>5 and n<9:
    print('Лето')
elif n>8 and n<12:
    print('Осень')
else:
    print('Ошибка')
