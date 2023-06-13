# from tkinter import*

# window = Tk()
# window.geometry('1280x720')
# window.title('ЛОТЕРЕЯ')
# window.config(bg='orange')

# def price ():
#     text = Label(text = "Чтобы забрать выйгрыш необходимо внести 1000 руб.",bg='orange',fg='red',font=('Arial', 35))
#     text.place(width=1280,height=720,x=0,y= 0)

# label = Label(text='ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!',bg='orange',fg='red',font=('Arial', 50))
# label.place(width=1280,x=0,y=150)

# money = Button(text = 'ПОЛУЧИТЬ ВЫЙГРЫШ!',bg='yellow',fg='red',font=('Arial', 50), command=price)
# money.place(x=225,y=400)
# window.protocol('WM_DELETE_WINDOW','on_close')
# window.mainloop()

# Задание 2

# dogs = {}

# N = int(input('Введите колличество собак: '))

# for i in range(N):
#     d = input('Введите название собаки: ')
#     n = int(input('Введите очки собаки: '))
#     dogs[d] = n

# Sort_dogs ={}
# sorted_keys = sorted(dogs, key = dogs.get, reverse=True)

# for w in sorted_keys:
#     Sort_dogs[w] = dogs[w]

# print(Sort_dogs)

# Задание 3

from tkinter import*

window = Tk()
window.title = 'Фотоальбом'
window.geometry('1280x720')

def menu():
    fon = Label(bg='white')
    fon.place(width=1280,height=720)
    label = Label(text='Выберите картинку', font=('Arial', 35),bg='white')
    label.place(width=1280,x=0,y=0)
    sun = Button(text = 'Солнце', font=('Arial', 35),command=image_sun)
    sun.place(x= 175,y=450)
    landscape = Button(text = 'Пейзаж',font=('Arial', 35),command=image_landscape)
    landscape.place(x=550,y=450)
    winter = Button(text='Зима',font=('Arial', 35),command=image_winter)
    winter.place(x=900,y=450)

def image_sun():
    fon = Label(bg='white')
    fon.place(width=1280,height=720)
    photo = PhotoImage(file="sun.png")
    label = Label(image = photo)
    label.image = photo
    label.place(x=400,y=250)
    back = Button(text='Назад',font=('Arial', 25),command=menu)
    back.place(x=15,y=30)

def image_landscape():
    fon = Label(bg='white')
    fon.place(width=1280,height=720)
    photo = PhotoImage(file="landscape.png")
    label = Label(image = photo)
    label.image = photo
    label.place(x=400,y=250)
    back = Button(text='Назад',font=('Arial', 25),command=menu)
    back.place(x=15,y=30)

def image_winter():
    fon = Label(bg='white')
    fon.place(width=1280,height=720)
    photo = PhotoImage(file="winter.png")
    label = Label(image = photo)
    label.image = photo
    label.place(x=400,y=200)
    back = Button(text='Назад',font=('Arial', 25),command=menu)
    back.place(x=15,y=30)
    
fon = Label(bg='white')
fon.place(width=1280,height=720)
label = Label(text='Выберите картинку', font=('Arial', 35),bg='white')
label.place(width=1280,x=0,y=0)
sun = Button(text = 'Солнце', font=('Arial', 35),command=image_sun)
sun.place(x= 175,y=450)
landscape = Button(text = 'Пейзаж',font=('Arial', 35),command=image_landscape)
landscape.place(x=550,y=450)
winter = Button(text='Зима',font=('Arial', 35),command=image_winter)
winter.place(x=900,y=450)

window.mainloop()