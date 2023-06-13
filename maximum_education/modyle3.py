#                                                                   Урок 1
# employee={'name':'Иван','salary':200000}

# print(f"У {employee.get('name')} зарплата в год составляет {employee.get('salary')*12} руб")

# print(employee)
# employee['age']=21
# print(employee)


# class Employee:
#     def __init__(self,name,salary,on_vacation,is_good_employee):
#         self.name=name
#         self.salary=salary
#         self.on_vacation=on_vacation
#         self.is_good_employee=is_good_employee
#     def get_info(self):
#         return [employee.name, employee.salary, employee.on_vacation, employee.is_good_employee]

# employee=Employee('Окунь', 100000)
# employee.on_rest=True
# print(f'У {employee.name} зарплата за год составляет {employee.salary*12} руб На отдыхе - {employee.on_rest}')

# employee_list=[
#    Employee('Окунь', 100000,True,True),
#    Employee('Вика', 300000,False,True),
#    Employee('Маша', 150000,True,True),
#    Employee('Коля', 250000,True,False),
#    Employee('Саша',75000,False,True)
# ]

# for employee in employee_list:
#     print(employee.get_info())

# for employee in employee_list:
#     if employee.is_good_employee==False:
#         print(employee.name,'уволен')
        
# for employee in employee_list:
#     if employee.is_good_employee==True:
#         print(employee.get_info())

#                                                                   Урок 2
# file: vk_bot_n1.py

#                                                                   Урок 3

# longpolling - это технология, которая позволяет получать данные о новых событиях с помощью "длинных запросов"

#                                                   pip freeze > requirements.txt


#                                                                   урок 4

# import time

# # list = (time.sleep(i) for i in range(1,3))
# # print(list)

# def my_lazy_func():
#     for i in range(1,11):
#         print(f'До {i}')
#         yield i 
#         print(f'После {i}')

# for i in my_lazy_func():
#     print(i)

# my_list = list(my_lazy_func())
# print(*my_list)


# def my_lazy_func(items):
#         yield from items

# items = ['Яблоко', 'Банан','Апельсин']

# for i in my_lazy_func(items):
#     print(i)

# f = open('file.txt','w') 
# f.write('Hello world!')
# f.close()

# with open('file.txt','w') as f: #контекст - открытый файл
#     f.write('Hello world!')

# import contextlib


# @contextlib.contextmanager
# def str_reverse(my_str):
#     print('Входим в контекст')
#     yield my_str[::-1]
#     print('Выходим из контекста')


# with str_reverse('Hello world') as reversed_str:
#     print(f'Выполненный код:{reversed_str}')

# import sys


# list = (i for i in range(1,1000000))

# list2 = [i for i in range(1,1000000)]

# print(sys.getsizeof(list))
# print(sys.getsizeof(list2))



# @contextlib.contextmanager
# def exc_handler(exc):
#     try:
#         yield True
#     except exc:
#         print('Предотвращено исключение')

# with exc_handler(IndexError):
#     my_list = [1,2]
#     print(my_list[3])



# def func_with_unlimited_args_kwargs(*args,**kwargs):
#     print(f'Арги:{args} Кварги{kwargs}')

# func_with_unlimited_args_kwargs(1,5,54,34, a=1,b=43, d = 53,c = 421)

#                                                             дз
# import sys



# A = [i**2 for i in range(1000001)]
# print(sys.getsizeof(A))
# print(*A)


# A1 = (i**2 for i in range(1000001))
# print(sys.getsizeof(A1))
# print(*A1)


# import contextlib
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime

# now = datetime.today()
# today = now.strftime('%d/%m/%Y')

# payload = {'date_req=': today}

# url = "https://www.cbr.ru/scripts/XML_daily.asp?"

# responce = requests.get(url, params=payload)

# xml = BeautifulSoup(responce.content, 'html.parser')        


# @contextlib.contextmanager
# def getCourse(id):
#         try:
#             yield xml.find('valute',{'id':id}).value.text
#         except:
#             print('Такая валюта не найдена')
        

# n = input()
# try:
#     with getCourse(n) as valut:
#         print(f'(1 шт.)Австралийский доллар стоит(ят) {valut} руб.')
# except:
#     None


#                                                                   урок 5


# class Year:
#     def __init__(self,days,season):
#         self.__days = days
#         self.__season = season
    
#     def get_days(self):
#         return self.__days #геттер
    
#     def get_season(self):
#         return self.__season
    
#     def set_days(self,days):
#         if days==365 or days==366:
#             self.__days = days
#         else:
#             raise Exception('Неккоректное значание')#Создаём свою собственную ошибку
    
#     def set_season(self,season):
#         self.__season = season

# year = Year(365,"зима")
# print(year.get_season())#Вызов геттера
# print(year.get_days())

# year.set_days(10)#Вызов Сеттера

# print(year.get_days())

# class Person:
#     def __init__ (self,name,age):
#         self.name = name
#         self.age = age

#     @property
#     def name(self):
#         return self.__name
        
#     @property
#     def age(self):
#         return self.__age
        
#     @name.setter
#     def name(self,name):
#         self.__name = name

#     @age.setter
#     def age(self,age):
#         if age<=0:
#             raise ValueError('Вы ещё не родились')
#         self.__age = age

# person = Person('Иван',10)
# print(person.name)
# print(person.age)

#                                                           урок 6


# with open('test.txt','w') as my_file:
#     my_file.write('Write something into the file')



# import time


# class RunningClassJudge:
#     def __init__(self):
#         self.start = None
    
#     def __enter__(self):
#         self.start = time.time()
#         return self
    
#     def __exit__(self,exc_type,exc_val,exc_tb):

#         t = time.time()-self.start
#         print(f'Время выполнения кода - {t} секунд')

#         if exc_type == TypeError:
#             return True

# with RunningClassJudge() as rcj:
#     my_list = [x for x in range(1,10_000_000)]
#     my_list-='s'
#     print(rcj)


# from random import randint

# my_list = [1,2,3,4,5]
# list_iterator = iter(my_list)
# # print(next(list_iterator))
# # print(next(list_iterator))
# # print(next(list_iterator))
# # print(next(list_iterator))
# # print(next(list_iterator))


# # for i in list_iterator:
# #     print(i)

# class RandomIter: #наш итератор
#     def __init__(self,limit):
#         self.limit = limit
#         self.__reload = limit
    
#     def __iter__(self): #метод для создания итератора
#         self.limit = self.__reload
#         return self # в основном коде получаем объект нашего итератора для перебора
    
#     def __next__(self):
#         if self.limit == 0:
#             raise StopIteration
#         self.limit-=1
#         return randint(1,100)
    

# rand_iter = RandomIter(10)
# for i in rand_iter:
#     print(i)



#                                                  Урок 7



# class Item:
#     def __init__(self,name,price,weight):
#         self.name = name
#         self.price = price
#         self.weight = weight

# item_1 = Item('Видеокарта',15000,0.8)
# item_2 = Item('Процессор',12000,0.3)

# total_price = item_1.price+item_2.price
# print(total_price)



# class Item:
#     def __init__(self,name,price,weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
    
#     def __add__(self,other): #self - ссылка на 1й объект, other - ссылка на объект после знака '+'
#         return self.price + other.price

# item_1 = Item('Видеокарта',15000,0.8)
# item_2 = Item('Процессор',12000,0.3)

# total_price = item_1+item_2
# print(total_price)



# class Item:
#     def __init__(self,name,price,weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
    
#     def __add__(self,other): #self - ссылка на 1й объект, other - ссылка на объект после знака '+'
#         if isinstance(other,Item):
#             return self.price + other.price
#         elif isinstance(other, int):
#             return self.price + other
# item_1 = Item('Видеокарта',15000,0.8)
# item_2 = Item('Процессор',12000,0.3)

# total_price = item_1+1000
# print(total_price)



# from tkinter import * 
# import random



# window = Tk()
# window.geometry('600x600')

# class Fire:
#     image = PhotoImage(file = 'maximum_education/media_3_7/fire.png').subsample(4,4)

#     def __add__(self,other):
#         if isinstance(other,Earth):
#             return Clay
# class Water:
#     image = PhotoImage(file = 'maximum_education/media_3_7/water.png').subsample(4,4)

# class Wind:
#     image = PhotoImage(file = 'maximum_education/media_3_7/wind.png').subsample(4,4)

# class Earth:
#     image = PhotoImage(file = 'maximum_education/media_3_7/ground.png').subsample(4,4)
#     def __add__(self,other):
#         if isinstance(other,Fire):
#             return Clay

# class Clay:
#     image = PhotoImage(file = 'maximum_education/media_3_7/pottery.png').subsample(4,4)

# canvas = Canvas(window,width=600,height=600)
# canvas.pack()

# elements = [Earth(),Water(),Fire(),Wind()]
# for element in elements:
#     canvas.create_image(random.randint(50,550),random.randint(50,550),image = element.image)

# def move(event):
#     images_id = canvas.find_overlapping(event.x,event.y,event.x+10,event.y+10)

#     if len(images_id)==2:
#         element_1 = elements[images_id[0]-1]
#         element_2 = elements[images_id[1]-1]

#         new_element = element_1+element_2
#         if new_element:
#             if new_element not in elements:
#                 canvas.create_image(random.randint(50,550),random.randint(50,550),image = new_element.image)
#                 elements.append(new_element)
#     canvas.coords(images_id,event.x,event.y)

# window.bind('<B1-Motion>',move)

# window.mainloop()



#                                урок 8



# from pprint import pprint
# from typing import Iterator

# # if __name__=='__main__':


# goods = [
#     {
#         'name':'Iphone 14',
#         'brand':'Apple',
#         'price':80000,
#         'os':'ios'
#     },
#     {
#         'name':'Redmi note 10',
#         'brand':'Xiaomi',
#         'price':11000,
#         'os':'Android'
#     },
#     {
#         'name':'Huawei P40',
#         'brand':'Huawei',
#         'price':40000,
#         'os':'Android'
#     }
# ]

# def item_price(item):
#     return item['price']

# print(sorted(goods,key=item_price))


# pprint(sorted(goods,key=lambda item : item['price'])) # Item это словарь

# android_list = list(filter(lambda item : item['os']=='Android',goods))

# print(android_list, Iterator)

# print(android_list)


# names_list = ['Тимофей','Окунь','Даниил','Вика']
# surname_list = ['Миляев','Обыкновенный','Волков','Соколова']

# fullnames_list = list(map(lambda name,surname : f'{name} {surname}',names_list,surname_list))
# for i in range(len(names_list)):
#     print(i,names_list[i])

# enumirated_list = []
# for i, item in enumerate(goods):
#     enumirated_list.append({i:item})

# pprint(enumirated_list)

# for name,surname in zip(names_list,surname_list): # если длины списков разные - кол-во итераций цикла равно длине меньшего из списков
#     print(name,surname)


# print(__name__)

# __main__ если это то файл открыт изнутри
# если открывать из др файла, то __name__ = название файла


#                               hw


# class Item:
#     def __init__(self,price,brand):
#         self.price = price
#         self.brand = brand
    
#     def __repr__(self):
#         return self.brand

# items_list = [
#     Item(1000,'Apple'),
#     Item(1200,'Apple'),
#     Item(900,'Samsung'),
#     Item(700,'Samsung'),
#     Item(660,'Xiaomi')
# ]
# result = list(filter(lambda item : repr(item)=='Apple',items_list))
# print(result)


# names_list = ['данил', 'артём', 'никита', 'влад']
# result = list(map(str.title, names_list))
# print(result)


#                                                урок 10
#                                                 SQL


# SELECT - выбрать
# SELECT (что) FROM (таблица) - конструкция SELECT выборки данных

# select model, speed, hd from pc where price<500

# select distinct maker from product where type = 'Printer'



# insert (into(необязательно в SQLite)) название таблицы (поля таблицы(необязательно)) values (значения)

# insert into Товар (id, name, price) values (4, 'Телефон', 3000);



# delete from название таблицы where условие;

# delete from pc where pc.hd = (select min(hd) from pc) or pc.ram = (select min(ram) from pc)



# update название таблицы set название столбца=новое значение where (условие)

# update товар set price=5000 where name='Телефон' and price=3000



#                                                       урок 11
# import sqlite3

# try:
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()
# except sqlite3.DatabaseError:
#     print('Ошибка подключения')

# finally:
#     connection.close()

# class User:
#     def __init__(self,name,surname,gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender


# def create_table_user(cursor):
#     command = """
#     CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,
#     name TEXT,
#     surname TEXT,
#     gender TEXT);"""
#     cursor.execute(command)

# def get_users(cursor):
#     command = """
#     SELECT * FROM users;
#     """
#     result = cursor.execute(command)
#     users = result.fetchall()
#     print(users)

# def get_user(cursor,user_id):
#     command = """
#     SELECT * FROM users WHERE id=?;
#     """
#     result = cursor.execute(command, (user_id))
#     user = result.fetchall()
#     print(user)


# def add_user(cursor,user):
#     command = """
#     INSERT INTO users(name,surname,gender) VALUES (?,?,?);"""
#     cursor.execute(command,(user.name,user.surname,user.gender))

# def update_user_name(cursor,value,user_id):
#     command = """
#     UPDATE users SET name = ? where id = ? ;"""
#     cursor.execute(command, (value, user_id))

# def delete_users(cursor):
#     command = """
#     DELETE FROM users;"""
#     cursor.execute(command)


# if __name__=='__main__':
#     with sqlite3.connect('data.db') as cursor:
#         create_table_user(cursor)
#         delete_users(cursor)
#         add_user(cursor, User('Иван', 'Тихненко', 'male'))
#         add_user(cursor, User('Иван', 'Тихненко', 'male'))
#         add_user(cursor, User('Иван', 'Тихненко', 'male'))
#         get_users(cursor)
#         get_user(cursor,"1")
#         update_user_name(cursor,'Аркадий',"1")
#         get_user(cursor,"1")



#                                                       урок 12


# import os


# current_path = os.path.abspath(__file__)
# parent_path = os.path.join(current_path,'..')


# # def recurs(count):
# #     print(count)
# #     if count==5:
# #         return
# #     recurs(count+1)
# #     print(count)

# # recurs(0)
# parent_path = 'путь к папке'
# def get_all_files(path):
#     for nameFile in os.listdir(path):
#         new_path = os.path.join(path,nameFile)
#         if os.path.isdir(new_path):
#             print('Папка',nameFile)
#             get_all_files(new_path)
#         print('-',nameFile)
# get_all_files(parent_path)