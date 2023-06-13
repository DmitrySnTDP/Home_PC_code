# Задание 1


questions = [
    {'question':'Сколько было колец Всевдастия?',
    'answers':['13','74','20','1'],
    'right_answer': 3},
    {'question':'Как звали друга Фродо?',
    'answers':['Бэн','Сэм','Гвэн','Саурон'],
    'right_answer': 2},
    {'question':'Сколько гномов учавствовало в походе в фильме Хоббит?',
    'answers':['43','5','17','13'],
    'right_answer': 4},
    {'question':'В каком году вышел фильм Властелин колец?',
    'answers':['1998','2000','2002','2004'],
    'right_answer': 3},
    {'question':'Кто главный герой властелина колец?',
    'answers':['Фродо',"Саурон","Голлум","Элронд"],
    'right_answer': 1}
    ]
true_q = 0
for q in questions:
    num = 0
    print(q.get('question'))
    for a in q['answers']:
        num =num+1
        print(num, ')', a)
    user_answer = int(input('Введи вариант ответа: '))
    if user_answer == q.get('right_answer'):
        print('Верно')
        true_q = true_q+1
    else:
        print('Не верно')
    print('-'*20)

print('Верных ответов: ',true_q)

if true_q>= 3:
    print("Ты победил")
else:
    print('Ты проиграл')


# Задание 2


music = {
    'world in my eyes': 4.86 ,
    'sweetest perfection': 4.43 ,
    'personal jesus': 4.56 ,
    'halo': 4.90 ,
    'waiting for the night': 6.07 ,
    'enjoy the silence': 4.20 ,
    'policy of truth': 4.76 ,
    'blue dress': 4.29 ,
    'clean': 5.83 }

quantity = int(input("Введите количество песен: "))
all_long = 0
m = []
for a in range(quantity):
    n = input('Введите название песни: ')
    n = n.lower()
    m.append(n)

num=0
for i in m:
    l = 0
    l = music.get(m[num])
    all_long = all_long + l
    num=num+1
        
print(round(all_long, 2), 'минуты')


# Задание 3


name = {
    1:'молоко',
    2:'сметана',
    3:'кефир',
    4:'хлеб',
    5:'кетчуп',
    6:'сыр',
    7:'томаты',
    8:'масло',
    9:'шоколад'}

price_quantity ={
    1: [49,40],
    2: [57,25],
    3: [43,20],
    4: [25,50],
    5: [115,15],
    6: [195,30],
    7: [79,10],
    8: [150,20],
    9:[150,15]}
    
num = 1

for i in name:
    print(num,')', name.get(num),'-',price_quantity.get(num)[1],'штук, стоимость ', price_quantity.get(num)[0]*price_quantity.get(num)[1],'руб.')
    num = num+1