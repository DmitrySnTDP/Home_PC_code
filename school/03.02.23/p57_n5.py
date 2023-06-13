a,b=map(int,input('Введите трёхзначное и десятичное число:').split())
print('Входит') if a%10==b or a//10%10==b or a//100==b else print('Не входит')
