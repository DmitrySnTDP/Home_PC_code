#                                                                       урок 1
# first_var = 5
# second_var = 3.14

# print(type(first_var),type(second_var))

# thir_var = 'Привет мир'
# sub_sting_hello = thir_var[0:6]

# sub_sting_world = thir_var[7:10]

# print(sub_sting_world+' '+sub_sting_hello)


# name = 'Роман'
# age = '20'

# hello = 'Привет, {}! Тебе {} лет?'.format(name,age)
# print(hello)

# valueError - ошибка при вводе символа вместо числа

# try:
#     # код который мы хотим сделать, но который может вызвать ошибку
#     one = int(input('Введите первое число: '))
#     two = int(input('Введите второе число: '))
# except ValueError:
#     print('Введено не число')
# else:
#     if one>two:
#         print(one, 'больше', two)
#     elif two>one:
#         print(two,'больше',one)
#     else:
#         print(one,'равно',two)



# def hello():
#     # это процедура т.к. не передаёт аргументы в код(return)
#     name = input('Введите имя')
#     print('Привет ',name)
#     hello()
#     # рекурсия это вызов функцией самой себя
# hello()


#                                                                       урок 3


# from tkinter import*

# window = Tk()

# window.geometry  ('800x600')

# canvas = Canvas(window, width=800, height=600, bg='white')

# canvas.pack()

# # # canvas.create_rectangle(10, 10, 110,110, fill='yellow', outline='')
# # # # canvas.create_polygon(10,180, 60,120, 110,180, fill='green', outline='')
# # # canvas.create_rectangle(150, 150, 300,300, fill='red4', outline='')
# # # canvas.create_rectangle(600, 100, 790,180, fill='khaki', outline='')

# # # домик
# # canvas.create_polygon(155,50, 75,100,   235,100, fill='red4', outline='')
# # canvas.create_rectangle(100, 100, 210,210, fill='gray', outline='')

# # ООП

# class House:
#     def __init__(self,roof_color, wall_color):
# # с-ва, которые мы хотим, чтобы ввёл пользователь при создании домика
#         self.roof_color = roof_color
#         self.wall_color = wall_color
#         # соотносим введенное пользователем значение со свойством домика
#         self.height = 130
#         self.width = 140
#         self.roof = None
#         self.wall = None
    
#     def build(self,x,y):
#         h = self.height
#         w = self.width
#         roof = canvas.create_polygon(x,y,x+w,y,x+w/2,h+100, fill=self.roof_color,outline='black')
#         wall = canvas.create_rectangle(x+20,y,x+120,y+100, fill=self.wall_color,outline='black')
    
#     def print_info(self):
#         print('Цвет крыши - ', self.roof_color)
#         print('Цвет стен - ', self.wall_color)
# house1 = House('green', 'blue')
# house2 = House('lavender','cyan')

# house1.build(100,300)
# house2.build(200,300)

# # print(house2.width) 

# house1.print_info()

# window.mainloop()


#                                                                       Урок 4

# from tkinter import *
# import random
# window = Tk()
# w = 600
# h = 600
# window.geometry(str(w)+"x"+ str(h))

# canvas = Canvas(window, width=w, height=h)
# canvas.place(in_=window, x=0,y=0 )

# bg_image = PhotoImage(file='media_f/bg_2.png')

# class Knight:
#     def __init__(self):
#         self.x=70
#         self.y=h/2
#         self.yv=0
#         self.xv=0

#         self.photo=PhotoImage(file='media_f/knight.png')

#     def up(self,event):
#         self.yv=-3
#     def down(self,event):
#         self.yv=3
#     def stop(self,event):
#         self.yv=0
#         self.xv=0
#     def left(self,event):
#         self.xv=-3
#     def right(self,event):
#         self.xv=3

# class Dragon:
#     def __init__(self):
#         self.x=750
#         self.y=random.randint(100,500)
#         self.v=random.randint(1,4)

#         self.photo=PhotoImage(file='media_f/dragon.png')

# knight=Knight()

# dragons=[]

# for i in range(3):
#     dragons.append(Dragon())


# def game ():
#     canvas.delete('all')
#     canvas.create_image(300,300, image=bg_image)
#     canvas.create_image(knight.x,knight.y, image = knight.photo)
#     knight.y+=knight.yv
#     knight.x+=knight.xv

#     current_dragon = 0
#     dragon_to_kill=-1

#     for dragon in dragons:
#         dragon.x-=dragon.v
#         canvas.create_image(dragon.x,dragon.y, image = dragon.photo)


#         if ((dragon.x-knight.x)**2)+((dragon.y-knight.y)**2)<=(96)**2:
#             dragon_to_kill=current_dragon

#         current_dragon+=1

#         if dragon.x <=0:
#             canvas.delete('all')
#             canvas.create_text(w//2,h//2, text='You lose!',font='Real 42', fill='red')
#             break

#     if dragon_to_kill!=-1:
#         del dragons[dragon_to_kill]

#     if len(dragons)==0:
#         canvas.delete('all')
#         canvas.create_text(w//2,h//2, text='You win!',font='Real 42', fill='red')
#     else:
#         window.after(10, game)

#     if knight.y<60:
#         knight.y=60
#     elif knight.y>540:
#         knight.y=540
#     elif knight.x<60:
#         knight.x=60
#     elif knight.x>540:
#         knight.x=540


# game()

# window.bind('<Key-Up>', knight.up)
# window.bind('<Key-Down>', knight.down)
# window.bind('<KeyRelease>', knight.stop)
# window.bind('<Key-Left>', knight.left)
# window.bind('<Key-Right>',knight.right)

# window.mainloop()

#                                                                       урок 5


# hour = int(input('Введи время в часах'))
# if hour>12 and hour<=16:
#     print('День')
# elif hour>16:
#     print('Вечер')

# Файл: web_scraping.py
#                                                                       урок6


# файл: api_CBR.py


#                                                                       урок 7

# import os
# from pygame import mixer
# from gtts import gTTS
# import time

# my_file=open('media_f/some.txt','r')
# my_text = my_file.read()
# my_file.close()

# print()

# mixer.init()
# tts=gTTS(text=my_text, lang='en')

# tts.save('audio.mp3')

# mixer.music.load('audio.mp3')
# mixer.music.play()
# while mixer.music.get_busy():
#     # пока аудио воспроизводится, программа будет ждать
#     time.sleep(1)

# mixer.music.unload()
# os.remove('audio.mp3')

# import pyaudio
# import speech_recognition as sr

# recognize =sr.Recognizer()
# #  объект класса Распознавалель
# while True:
#     with sr.Microphone() as source:
#         # with позволяет не закрывать файл вручную
#         print('Начинай говорить')
#         audio=recognize.listen(source)

#     speech = recognize.recognize_google(audio).lower()
#     print('Вы сказали', speech)
#     if speech=='hello':
#         print('Привет')


#                                                                       урок 8

# from tkinter import*

# window =Tk()
# window.title('My exe')
# window.geometry('500x500+1000+400')

# count=0
# def Chetchik():
#     global count
#     count+=1
#     label['text'] = count

# label = Label(window, text='Hello',bg='green',fg='blue',font='16')
# label.place(x=100,y=100)

# label['text']='Hi'
# label['fg']='black'

# btn=Button(window, text='Button', background='#45b3db', font='16', command=Chetchik)
# btn.place(x=200, y=200)

# window.mainloop()

# from tkinter import*
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime

# window=Tk()
# window.title('Деньгобанк')
# window.geometry('400x300+500+300')
# window.resizable(width=False,height=False)
# window.config(bg='#62e4e9')

# url='http://www.cbr.ru/scripts/XML_daily.asp?'

# today=datetime.today()
# today=today.strftime('%d/%m/%Y')

# payload={'date_req':today}

# responce=requests.get(url, params=payload)

# xml=BeautifulSoup(responce.content, 'html.parser')

# def getCourse(id):
#     return xml.find('valute', {'id':id}).value.text

# img_logo=PhotoImage(file='media_f/logo.png')
# logo= Label(window, image =img_logo,bg='#62e4e9')
# logo.place(x=0,y=0)

# course_info=Label(window, text='Курс рубля в банке \n составляет: ',bg='#62e4e9', font=('Arial 16'))
# course_info.place(x=150,y=90)

# dollar=Label(window, text='Доллар стоит: '+getCourse('R01235')+' рублей',bg='#62e4e9', font=('Arial 16'))
# dollar.place(x=15,y=150)

# eur=Label(window, text='Евро стоит: '+getCourse('R01239')+' рублей',bg='#62e4e9', font=('Arial 16'))
# eur.place(x=15,y=200)

# cny=Label(window, text='Китайский юань стоит: '+getCourse('R01375')+' рублей',bg='#62e4e9',font=('Arial 16'))
# cny.place(x=15,y=250)

# window.mainloop()

#                                                                       урок 9

# def func(a,b,c=3):
#     # c имеет значение по умолчанию
#     print(a,b,c)

# func(1,2)

# def func(a,b, *args, **kwargs):
#     c=kwargs.get('c',3) # 'c'это ключ из словаря , а если её нету то значение по умолчанию, т.е. 3
#     print(a,b,c)
#     print(args)
#     # args позволяет вводить любое колличество аргументов
#     print(kwargs)
#     # kwargs позволяет это создаёт именнованные аргументы (создаёт словари) func(one=1,two=2) one и two-ключи, 1 и 2 - значения

# func(1,2,7,123,4465,78979, True,one=1,two=2)

# score=int(input())
# if score>50:
#     res=True
# else:
#     res=False

# print(res)
# # или
# # тернарный оператор
# score=int(input())
# res=True if score>50  else False #значение если условие выполнится/условие/значение если усл. не выполнится
# print(res)

# score=int(input())
# res= score>50
# print(res)

# num=int(input())
# res= 'chocolate'if num>=4 else None
# print(res)

# работа с генератором списка

# arr=[]
# for x in range(100):
#     arr.append(x)
# print(arr)

# arr=[x for x in range(100) if x%5==0]
# # Что кладём\цикл(откуда берём)
# print(arr)

# x %5==0 # pascal: x mod 5 =0


# arr=[(x**3 if x>50 else x) for x in range(100) if x %5==0]
# print(arr)

# a={x:len(x) for x in ['orange', 'red', 'yellow','green']}
# print(a)

# a=[x for x in range(100) if (x %30==0)or(x %31==0)]
# print(a)

# картежи(неизменяемые списки)

# some_dict={
#     (1,2,3): 'Hello'
# }
# a= some_dict[(1,2,3)]
# print(a)

# some_tuple=(1,2,3) 
# # это картеж
# print(some_tuple, type(some_tuple))
# some_list=list(some_tuple)
# # превратили картеж в список
# print(some_list, type(some_list))

# some_tuple=([0,1,2,3], 'hello')
# print(some_tuple,type(some_tuple))
# some_tuple[0].append(4)
# print(some_tuple)

# дз

# a1=[]
# a2=[]
# for i in range(10):
#     n=int(input())
#     a2.append(n) if n%2==0 else a1.append(n)


# a = (5,3,2,1,4)
# a_list=list(a)
# a_list.sort()
# a = tuple(a_list)


#                                                                       урок 10
# class People:
#     def __init__(self,name,color,height,weight):
#         self.name=name
#         self.color=color
#         self.height=height
#         self.weight=weight
#         def breathe(self):
#             print(f'{self.name}дышит')

# man1= People('Роман', 'brown', 178, 67)
# man2= People('Андрей', 'рыжий', 175, 65)
# print(man1.name,man2.name)

# man3=People('Тим','чёрный',130,35)
# man3.height=178
# print(man3.name, man3.height)

# print(dir(People))



# from random import*
# class Tank:
#     def __init__(self,model,armor,min_damage,max_damage,health):
#         self.model=model
#         self.armor=armor
#         self.health=health
#         self.damage=randint(min_damage,max_damage)

#     def  print_info(self):
#         print(f'модель {self.model},броня {self.armor},здоровье {self.health},средний урон {self.damage}')
    
#     def health_down(self, enemy_damage):
#         self.health-=enemy_damage
#         print(f'\n{self.model}:')
#         print(f'командир, по экипажу {self.model} попали, осталось {self.health} единиц здоровья')
    
#     def shot(self,enemy):
#         if self.health>0 and enemy.health>0:
#             enemy.health_down(self.damage)
#             print(f'\n{self.model}:')
#             print(f'Есть пробитие У противника {enemy.model} осталось {enemy.health} единиц здоровья')
#         elif enemy.health<=0 and self.health>0:
#             print('Зачем боеприпасы тратишь, балбес?')
#         elif self.health<=0:
#             print('С того света стрелять нельзя, дружище')

# tank1=Tank('Т-34',90,20,30,100)
# tank0=Tank('рандомный чел в шутере',50,10,15,150)
# tank2=Tank('Pz.Kpfw. IV',50,10,20,120)

# tank1.print_info()
# tank2.print_info()
# tank1.shot(tank2)

# # наследование:
# class SuperTank(Tank):
#     def __init__(self, model, armor, min_damage, max_damage, health):
#         super().__init__(model, armor, min_damage, max_damage, health)

#     def health_down(self, enemy_damage):
#         super().health_down(self, enemy_damage/2)



# class A:
#     def one(self):
#         print(1)
#     def two(self):
#         print(2)

# class B(A):
#     def two(self):   # метод перзаписи(оверрайв?)
#         print('two')
#     def third(self):
#         print('third')
        
# a=A()
# a.one()
# b=B()
# b.two()


# class user:
#     def __init__(self,health,type_attack,damage):
#         self.health=health
#         self.type_attack=type_attack
#         self.damage=damage

# class magician(user):
#     def __init__(self, health, type_attack, damage):
#         super().__init__(health, type_attack, damage)

# class warrior(user):
#     def __init__(self, health, type_attack, damage):
#         super().__init__(health, type_attack, damage)

# class archer(user):
#     def __init__(self, health, type_attack, damage):
#         super().__init__(health, type_attack, damage)


#                                                                       урок 11
# полиморфизм
# a='hello'+' '+'world'+'!'

# print(id(1),type(1))
# print(id(id),type(id))
# print(id(type),type(type))

# инкапсуляция
# class A:
#     def public(self):
#         return 42
#     def _private(self):
#         return 'true'
#     def __protected(self):
#         return 'protected'
    
#     def wrapper_def(self):
#         return 'called'+ self.__protected()
# a=A()
# print(a.public())
# print(a._private())
# print(a.wrapper_def())

# print(a._A__protected()) #не рекомендуется использовать

# паттерны проектирования

# Singleton

# class Man:
#     pass

# m1=Man()
# m2=Man()
# print('Object created:', m1, id(m1))
# print('Object created:', m2, id(m2))

# class Singleton(object):
#     def __new__(cls):
#         if not hasattr(cls,'instance'):
#             cls.instance = super(Singleton,cls).__new__(cls)
#         return cls.instance

# s=Singleton()
# s2=Singleton()
# print('Object created: ', s,id(s))
# print('Object created: ', s2,id(s2))

# def f():
#     return 2+2
# q=f()
# print(q)


# def repair_func(func):
#     def wrapper(a,b):
#         return func(a,b)-1
    
#     return wrapper
    
# @repair_func
# def wrong_func(a,b):
#     return a+b+1

# print(wrong_func(2,2))
# from datetime import datetime

# def timeit(func):
#     def wrapper(val):
#         start=datetime.now()
#         res = func(val)
#         end= datetime.now()
#         print(f'time:{end-start}')
#         return res
#     return wrapper
# @timeit
# def get_list_1(val):
#     return[x for x in range(0,val) if x//2==0 ]

# @timeit
# def get_list_2(val):
#     new_list=[]
#     for x in range(0,val):
#         if x%2==0:
#             new_list.append(x)

# val=1000000
# a=get_list_1(val)
# b=get_list_2(val)

#                                                                       Урок 12

# from tkinter import*
# import time
# from random import*

# window=Tk()
# window.title('Арканоид')
# window.resizable(False,False)
# window.wm_attributes('-topmost',1)
# canvas=Canvas(window,width=500,height=400)
# canvas.pack()


# class Ball():
#     def __init__(self,canvas,platforma,color):
#         self.canvas=canvas
#         self.platforma=platforma
#         self.oval=canvas.create_oval(200,200,215,215,fill=color)
#         self.dir=[-4,-2,-1,1,2,4]
#         self.x=choice(self.dir)
#         self.y=-4
#         self.touch_bottom= False

#     def draw(self):
#         self.canvas.move(self.oval,self.x,self.y)
#         pos=self.canvas.coords(self.oval) #получение координат: coords

#         if pos[1]<=0:
#             self.y=4
#         if pos[3]>=400:
#             self.touch_bottom=True
#         if self.touch_platform(pos)==True:
#             self.y=-4
#         if  pos[0]<=1:
#             self.x=4
#         if pos[2]>=500:
#             self.x=-4

#     def touch_platform(self,ball_pos):
#         platform_pos=self.canvas.coords(self.platforma.rect)
#         if ball_pos[2]>=platform_pos[0] and ball_pos[0]<=platform_pos[2]:
#             if ball_pos[3]>=platform_pos[1] and ball_pos[1]<=platform_pos[3]:
#                 return True
#         return False

# class Platform():
#     def __init__(self,canvas,color):
#         self.canvas=canvas
#         self.rect=canvas.create_rectangle(230,300,330,310,fill=color)
#         self.x=0
#         self.canvas.bind_all(' <KeyPress-Left>',self.left)
#         self.canvas.bind_all(' <KeyPress-Right>',self.right)
#         self.canvas.bind_all(' <KeyRelease>',self.stop)

#     def left(self,event):
#         self.x=-6
#     def right(self,event):
#         self.x=6
#     def stop(self,event):
#         self.x=0
#     def draw(self):
#         self.canvas.move(self.rect,self.x,0)
#         pos=self.canvas.coords(self.rect)
        

#         if pos[2]>=500:
#             self.x=0
#             pos[2]=499
#             pos[0]=399
            
#         if pos[0]<=0:
#             self.x=0
#             pos[0]=1
#             pos[2]=101
    
        
# platforma=Platform(canvas,'black')
# ball=Ball(canvas,platforma,'#b90100')


# while True:
#     if ball.touch_bottom==False:
#         ball.draw()
#         platforma.draw()
#     else:
#         break
#     window.update()
#     time.sleep(0.015)
