                                                                    #  Дз 1
 
# first_animal = ("Заяц")
# second_anival = ("Черепаха")

# print(first_animal, 'спит', ',', second_anival, "идёт")


# number1 = float(input("Введите первое число "))
# sign = input("Укажите знак ")
# number2 = float(input("Введите второе число "))

# if sign == "+": 
#   c = number1 + number2
# elif sign == "-":
#   c = number1 - number2
# elif sign == "*":
#   c = number1 * number2
# elif sign == "/":
#   c = number1 / number2

# print("Ответ:", c)


                                                                    #  Урок 2
# список

# numbers = [5,8,1,3,12]

# print(numbers[-3])

# numbers = [5,8,1,3,12]
# print(numbers)

# numbers.append(int(input("Введи число: ")))

# print(numbers)

# мин макс длина

# numbers = [5,8,1,3,12]

# print('Минимальный элемент списка = ', min(numbers))

# print('Максимальный элемент списка = ', max(numbers))


# Удаление элемента

# numbers = [5,8,1,3,12,8,4,3]

# numbers.remove(8)
# print(numbers)

# numbers = [5,8,1,3,12,8,4,3]

# print(numbers)
# del numbers[1]
# print(numbers)

# numbers = [5,8,1,3,12,8,4,3]

# num = int(input("Введите число для удаления: "))
# numbers.remove(num)
# rint(numbers)

# Длина

# numbers = [5,8,1,3,12,8,4,3]

# print('Длина :', len(numbers))

# Подсчёт кол-ва элементов

# numbers = [5,8,1,3,12,8,4,3]
# num = int(input("Искать число?"))

# print('Число встретилось раз: ', numbers.count(num))

# numbers = [5,8,1,3,12,8,4,3]
# numbers.sort()
# print(numbers)
# # или же
# print(sorted(numbers))
# # по убыванию
# numbers.sort(reverse = True)

#                                                                      Урок 3

# Задание 1

# facts = ["Земля - 3 планета", "Тихий океан - Самый большой", "Попугай-Жако может выучить до 1500 слов", "Существует високосная секунда"]

# number_of_fact = int(input("Какой факт нужно вывести? "))

# print(facts[number_of_fact-1])

# Рандом

# import random

# facts = ["Земля - 3 планета", "Тихий океан - Самый большой", "Попугай-Жако может выучить до 1500 слов", "Существует високосная секунда"]


# print("Случайный факт: ", random.choice(facts))



# Урок 3

# Библиотеки

# import emoji

# print(emoji.emojize(":snake: "))


#                     Циклы

# for i in range(5,10):
#     print(i)

# for i in range(5,0,-1):
#     print(i)

# for i in range(0,10, 2):
#     print(i)


#Добавление 3х элементов в список

# facts = []
# for i in range(3):
#     new_fact = input("Введите факт:")
#     facts.append(new_fact)
#     print(facts)

# cashe = []
# for i in range(6):
#     b = int(input("введите доход за месяц: "))
#     cashe.append(b*0.3)
# print("Накопления: ", sum(cashe))

#                                                                      Урок 4


# temp = []

# for i in range(7):
#   t = int(input("Введите температуру: "))
#   temp.append(t)

# print(round(sum(temp)/len(temp), 2))

#          round   это округлить



# num = int(input())
# if num > 0:
#   print("Число положительное ")

# elif num == 0:
#   print("Ноль")

# else:
#   print("Число отрицательное ")


# favourite_actor = "Леонардо Ди Каприо"

# actor = input("Какой ваш любимый актёр?")

# if favourite_actor == actor:
#   print("Смотри!")

# elif actor == "Джонни Депп":
#   print("Ну более менее")
# else:
#   print("Фу")



# import random

# a = random.randint(1,10)
# for i in range(3):
#   b = int(input("Введите число: "))
# 
#   if a == b:
#     print("Угадал")
#     break
#   elif a-b==1 or b-a==1:
#     print("Почти угадал")
#     b = int(input("Ещё попытка: "))
#   else:
#     print("Увы, не угадал")

#                                                                      Урок 5



# eng_dict = {
#     'яблоко': 'apple',
#     'молоко': 'milk',
#     'собака': 'dog'
# }

# word = input()

# print(eng_dict.get(word))

# если надо сделать возможнось спрашивать что угожно без вывода ошибки

#              или

# print(eng_dict[word])



# films = {
#     'начало': 'Леонардо ди Каприо',
#     'пираты карибского моря': 'Джонни Депп',
#     'миссия невыполнима': "Том Круз"
# }
# f_actor = 'Джонни Депп'
# film = input('Введите фильм')
# film = film.lower()
# actor = films.get(film)
# if actor == f_actor:
#     print('Точно посмотрю')
# else:
#     print('Не буду смотреть')



# questions = [
#     {'question':'Сколько было колец Всевдастия?',
#     'answers':['13','74','20','1'],
#     'right_answer': 3
#     },
#     {'question':'Как звали друга Фродо?',
#     'answers':['Бэн','Сэм','Гвэн','Саурон'],
#     'right_answer': 2
#     },
#     {'question':'Сколько гномов учавствовало в походе в фильме Хоббит?',
#     'answers':['43','5','17','13'],
#     'right_answer': 4
#     }
#     ]

# for q in questions:
#     num = 0
#     print(q.get('question'))
#     for a in q['answers']:
#         num = num+1
#         print(num, ')', a)
#     user_answer = int(input('Введи вариант ответа: '))
#     if user_answer == q.get('right_answer'):
#         print('Верно')
#     else:
#         print('Не верно')
#     print('-'*20)


#                                                                      Урок 6


# f = open('test.txt')
# print(f.read())

# read сохраняет данные в виде 1й строки

# print(f.readline())
# print(f.readline())

# readline сохраняет одну строку из файла

# print(f.readlines())

# readlines возвращает все данные в виде списка строк

# data = f.readlines()
# print(data)

# for line in f:
#     print(int(line))
# прочитать весь файл построчно

# f = open('test.txt') 
# если ничего не указано то по умолчанию файл открыт только для чтения

# f = open('test.txt','w')
# f.write(str(123))                     
# f.close()
# перезапись

# f = open('test.txt','a')
# # Дозапись
# f.write('9999')
# f.close()

# f = open('test.txt','a')
# # Дозапись след строчкой
# f.write('\n9999')
# f.close()

# 27задание егэ
# import random

# f = open('27_B.txt', 'w')
# num = int(input("Сколько чисел в файле?"))
# for i in range(num):
#     n = random.randint(1,10000)
#     f.write(str(n) + '\n')
# f.close()
# # следующие 2 строки не запускать!
# f = open('27_B.txt')
# print(f.read())

#                                                                      Функции

# калькулятор из функций

# def summa_2(x,y):
#     s=x+y
#     return s

# def minus_2(x,y):
#     s=x-y
#     return s

# def umn_2(x,y):
#     s=x*y
#     return s

# def delit_2(x,y):
#     s=x/y
#     return s

# summa = summa_2(20, 35)
# print(summa)

# num1 = int(input('Введи первое число: '))
# num2 = int(input("Введи второе число: "))
# oper = input('введи +,-,* или /  ')

# if oper == '+':
#     print(summa_2(num1, num2))
# elif oper == '-':
#     print(minus_2(num1, num2))
# elif oper == '*':
#     print(umn_2(num1, num2))
# elif oper == '/':
#     print(delit_2(num1,num2))


#                                                         урок 7


# from tkinter import*
# добавить из tkinter  только необходимые функции ('*')- все функции


# from tkinter import*

# window =Tk()

# window.geometry('720x480')
# window.title('Quiz')


# facts = [
#     {'text':'На Земле деревьев больше чем звёзд на небе','right':1},
# {'text':'Средняя зарплата в РФ - 100000', 'right': 0},
# {'text': 'Метро Санкт-Петербурга - самое глубокое в мире', 'right': 1},
# {'text': 'В течение жизни человек проходит около 15 экваторов Земли', 'right': 0}
# ]

# num = 0
# # Счётчик фактов
# points = 0

# def check():
#     global num, points
#     answer = var.get()
#     if bool(answer) == facts[num]['right']:
#         points+=1
#     if num<len(facts)-1:
#         num+=1
#         fact['text']=facts[num]['text']
#     else:
#         points_lable = Label(text =str(points),font=('Arial', 20), fg='green', bg= 'yellow')
#         points_lable.place(width=720,height=275,x=0,y=0)


# label_title = Label(text ='Тест',font=('Arial', 20), fg='green', bg= 'yellow')
# label_title.place(width=720, height = 50, x=0, y=0)


# fact = Message(text=facts[num]['text'],font=('Arial', 20), fg='green', bg= 'yellow')
# fact.place(width=550,x=125, y=100)

# var = IntVar()
# true_btn = Radiobutton(text='Правда', variable = var, value =1)
# false_btn = Radiobutton(text='Ложь', variable = var, value =0)
# true_btn.place(x=10,y=170)
# false_btn.place(x=10,y=190)

# button = Button(text ='Отправить',font=('Arial', 20), fg='green', bg= 'yellow', command = check)
# button.place(x=300, y=275 )


# window.mainloop()


#                                                         Урок 8


# вирус
# from tkinter import *

# window = Tk()
# window.geometry('900x300')
# window.title('Virus')
# window.config(bg='black')
# window.resizable(width=False,height=False)

# def on_close():
#     if int(timer['text'])>0:
#         timer['text'] = int(timer['text'])-1
#         window.after(1000, on_close)
#         timer.place(x=440,y = 70)
#     else:
#         width = window.winfo_screenwidth()
#         height= window.winfo_screenheight()
#         window.geometry(str(width) + 'x' + str(height))
#         photo = PhotoImage(file="fone.png")
#         label = Label(image = photo, bg='black')
#         label.image = photo
#         label.place(width=width,height=height)
# text = Label(text = 'ВАШ КОМПЬТЕР ЗАРАЖЁН!!!!!', bg='black', fg= 'green', font= ('Courier New',34))
# text.place(width=900,height=100,x=30,y=100)

# timer = Label(text='6', bg='black', fg='green', font= ('Courier New',34))

# window.protocol('WM_DELETE_WINDOW', on_close)
# window.mainloop()

                                                    # Урок 9

# import requests
# from bs4 import BeautifulSoup
# import random
# def get_facts():
#     response = requests.get('https://i-fakt.ru')
#     response = response.content

#     html = BeautifulSoup(response, 'html.parser')
#     fact = random.choice(html.find_all(class_='p-2 clearfix'))
#     print(fact.text)
#     print(fact.a.attrs['href'])

# def get_festival():
#     response = requests.get('https://kudago.com/msk/festival')
#     response = response.content

#     html = BeautifulSoup(response, 'html.parser')
#     fact = random.choice(html.find_all(class_='post-header'))
#     print(fact.text)
#     print(fact.a.attrs['href'])

# def get_concert():
#     response = requests.get('https://kudago.com/msk/concerts/')
#     response = response.content

#     html = BeautifulSoup(response, 'html.parser')
#     fact = random.choice(html.find_all(class_='post-header'))
#     print(fact.text)
#     print(fact.a.attrs['href'])

# while True:
#     a = ['0 - выход, 1-Факт, 2 - фестиваль, 3 - концерт']
#     print(*a)
#     num = int(input())
#     if num == 0:
#         break
#     elif num == 1:
#         get_facts()
#     elif num == 2:
#         get_festival()
#     else:
#         get_concert()
#     print('*'*20)



# убрать лишние строки и пробелы
# 1) replace('\n', '')
# 2) trim()

#                                                         Урок 10


# цикл с условием "while"

# i =1
# while i>=0:
#     print(i)
#     i +=1


# n = int(input())
# leng = 0
# while n>0:
#     n=n//10
#     # / это обычное деление, а // это целочисленное деление
#     leng+=1
# print(leng)


# password = 1234
# a = 3

# while a>0:
#     a-=1
#     P = int(input('Введите пин-код: '))
#     if P == password:
#         print('Добро пожаловать!')
#         break
#     elif a==0:
#         print('Доступ к аккаунту ограничен') 
#     else:
#         print('Неверный пароль, осталость попыток: ', a)


# from fpdf import FPDF

# pdf = FPDF('P', 'cm', (12,20))
# pdf.add_page()
# pdf.add_font('courier','','C:/WINDOWS/FONTS/COUR.TTF', uni = True)
# pdf.set_font('courier', size=16)
# pdf.set_fill_color(255,0,0)
# pdf.set_text_color(0,255,0)
# pdf.cell(10,5, txt='Hello yopt', align='C', fill=True)

# pdf.image('pic.jpg', h=0,w=10, x=0,y=5)

# pdf.output('test_pdf.pdf')





#                                                         Exel

# import xlrd, xlwt
# #открываем файл
# rb = xlrd.open_workbook('../ArticleScripts/ExcelPython/xl.xls',formatting_info=True)

# #выбираем активный лист
# sheet = rb.sheet_by_index(0)

# #получаем значение первой ячейки A1
# val = sheet.row_values(0)[0]

# #получаем список значений из всех записей
# vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

# wb = xlwt.Workbook()
# ws = wb.add_sheet('Test')

# #в A1 записываем значение из ячейки A1 прошлого файла
# ws.write(0, 0, val[0])

# #в столбец B запишем нашу последовательность из столбца A исходного файла
# i = 0
# for rec in vals:
#     ws.write(i,1,rec[0])
#     i =+ i

# #сохраняем рабочую книгу
# wb.save('../ArticleScripts/ExcelPython/xl_rec.xls')

# #                                                         openpyxl


# import openpyxl
# wb = openpyxl.load_workbook(filename = '../ArticleScripts/ExcelPython/openpyxl.xlsx')
# sheet = wb['test']

# #считываем значение определенной ячейки
# val = sheet['A1'].value

# #считываем заданный диапазон
# vals = [v[0].value for v in sheet.range('A1:A2')]

# #записываем значение в определенную ячейку
# sheet['B1'] = val

# #записываем последовательность
# i = 0
# for rec in vals:
#     sheet.cell(row=i, column=2).value = rec
#     i =+ 1

# # сохраняем данные
# wb.save('../ArticleScripts/ExcelPython/openpyxl.xlsx')


# #                                                         Работа с com-объектом

# import win32com.client
# Excel = win32com.client.Dispatch("Excel.Application")

# wb = Excel.Workbooks.Open(u'D:\\Scripts\\DataScience\\ArticleScripts\\ExcelPython\\xl.xls')
# sheet = wb.ActiveSheet

# #получаем значение первой ячейки
# val = sheet.Cells(1,1).value

# #получаем значения цепочки A1:A2
# vals = [r[0].value for r in sheet.Range("A1:A2")]

# #записываем значение в определенную ячейку
# sheet.Cells(1,2).value = val

# #записываем последовательность
# i = 1
# for rec in vals:
#     sheet.Cells(i,3).value = rec
#     i = i + 1

# #сохраняем рабочую книгу
# wb.Save()

# #закрываем ее
# wb.Close()

# #закрываем COM объект
# Excel.Quit()

# #                                                         Вызываем функции Python из MS Excel

# def get_unique(lists):
#     sm = 0
#     for i in lists:
#         sm = sm + int(i.pop()) 
#     return sm


#          обёртка для модуля пайтон
# Function sr(lists As Range)
#     On Error GoTo do_error
#         Set plugin = PyModule("plugin", AddPath:=ThisWorkbook.Path)
#         Set result = PyCall(plugin, "get_unique", PyTuple(lists.Value2))
#         sr = WorksheetFunction.Transpose(PyVar(result))
#         Exit Function
# do_error:
#         sr = Err.Description
# End Function

#                                                          урок 11

# from fpdf import FPDF
# from datetime import datetime

# pdf =FPDF('P','mm','A4')

# pdf.add_page()

# pdf.image('bg.jpg',h=297,w=210,x=0,y=0)
# pdf.add_font('courier','','C:\WINDOWS\FONTS\COUR.TTF', uni=True)
# pdf.set_font('courier',size=36)
# pdf.set_text_color(0,0,0)

# name_friend = input('Введи имя друга: \n')
# pdf.cell(0,95,ln=1)
# pdf.cell(0,20, txt='Дорогой ' + name_friend, align='C', ln=1)

# pdf.set_font('courier', size=18)
# pdf.set_text_color(0,0,0)
# text =input('Введи текст поздравления: \n')


# pdf.set_left_margin(50)
# pdf.set_right_margin(50)
# pdf.multi_cell(0,20, txt=text, align='C')

# today = datetime.today().strftime('%d.%m.%y')
# pdf.set_text_color(124,89,147)
# pdf.cell(0,10, txt=today, align='R', ln=1)

# pdf.output('bday_blank.pdf')

#                                                          урок 12 

# декораторы - видоизменение функции(функция в функции)

# def my_decorator(Func_to_decorate):
#     # функция-обёртка
#     def decorated_func():
#         print('Я начал работать')
#         Func_to_decorate()
#         print('Я закончиль')
#     return decorated_func

# @my_decorator
# def my_func():
#     print('Я работаю!')

# my_func()