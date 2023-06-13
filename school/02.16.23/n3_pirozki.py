print('Стоимость пирожка:')
a,b=map(int,input().split())
n=int(input('Сколько пирожков: \n'))
s=(a*100+b)*n
print('К оплате:',s//100,'руб.',s%100,'коп.')
