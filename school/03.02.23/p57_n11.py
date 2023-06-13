n=int(input('введите номер месяца:'))
if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print(31)
elif n==2:
    print(28)
elif n>12 or n<1:
    print('ошибка')
else:
    print(30)

    
