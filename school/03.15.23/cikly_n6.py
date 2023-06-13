a=int(input('Введите натуральное число:'))
k=0
while a>9:
    if a%10==a%100//10:
        k=1
        break
    a=a//10

if k!=0:
    print('Да')
else:
    print('Нет')
