m,d=map(int,input('Введите номер весяца и день:').split())
if m==3 or m==5 or m==7:
    n=365-(m//2)*31-(m//2-1)*30-d-28
    print(n)
elif m==2:
    n=365-31-d
    print(n)
elif m==4 or m==6:
    n=365-(d+((m//2-2)*30)+(m//2*31)+28)
    print(n)
elif m==1:
    n=365-d
    print(n)
elif m==8:
    n=365-d-m//2*31-(m//2-2)*30-28
    print(n)
elif m==9 or m==11:
    n=365-d-(m//2+1)*31-(m//2-2)*30-28
    print(n)
elif m==10 or m==12:
    n=365-d-28-(m//2)*31-(m//2-2)*30
    print(n)
else:
    print('Ошибка')
