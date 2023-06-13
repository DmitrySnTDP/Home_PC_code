# from tkinter import*

# window = Tk()

# window.geometry('1280x720')
# window.title('Кликер')

# num = 0

# def next_color():
#     global num
#     info = Message(text=str(num), font=('Arial', 20))
#     info.place( x=615,y= 150)
#     if num >= 20:
#         click = Button(text='Клик',font=('Arial', 20),bg='orange',command = next_color)
#         click.place(width =100,x=585, y=250)
#     else:
#         click = Button(text='Клик',font=('Arial', 20),bg='white',command = next_color)
#         click.place(width =100,x=585, y=250)
#     num+=1

# label_title = Label(text = 'Кликер',font=('Arial', 30))
# label_title.place(width =1280,x=0,y=0)

# start = Button(text='Старт',font=('Arial', 20), bg='white',command = next_color)
# start.place(x=585, y=250)

# window.mainloop()


# задание 2

# from tkinter import*
# import time

# window = Tk()

# window.geometry('1280x720')
# window.title('Кликер')

# num = 0

# def next_color():
#     global num
#     info = Message(text=str(num), font=('Arial', 20))
#     info.place( x=615,y= 150)
#     if num >= 20:
#         click = Button(text='Клик',font=('Arial', 20),bg='orange',command = next_color)
#         click.place(width =100,x=585, y=250)
        
#     else:
#         click = Button(text='Клик',font=('Arial', 20),bg='white',command = next_color)
#         click.place(width =100,x=585, y=250) 
#     if num == 20:
#         time.sleep(2)
#     num+=1

# label_title = Label(text = 'Кликер',font=('Arial', 30))
# label_title.place(width =1280,x=0,y=0)

# start = Button(text='Старт',font=('Arial', 20), bg='white',command = next_color)
# start.place(x=585, y=250)

# window.mainloop()


# Задание3


from tkinter import*
import random

window = Tk()

window.geometry('1280x720')
window.title('Кликер')

num = 0
n_click1 = 0
n_click2 = 0

def next_color():
    global num

    info = Message(text=str(num), font=('Arial', 20),bg='white')
    info.place(width =1280,height=75,x=0,y= 150)

    back = Message(bg ='white')
    back.place(width=1280,height=495,x=0,y=225)

    click = Button(text='Клик',font=('Arial', 20),bg='white',command = next_color1)
    click.place(width =100,x=random.randint(0,1180), y=random.randint(250,645)) 
    n_click1

    click2 = Button(text='тоже клик',font=('Arial', 20),bg='white',command = next_color2)
    click2.place(width =200,x=random.randint(0,1080), y=random.randint(250,645))
    num+=1


def next_color1():
    global num, n_click1, n_click2

    info = Message(text=str(num), font=('Arial', 20),bg='white')
    info.place(width =1280,height=75,x=0,y= 150)

    back = Message(bg ='white')
    back.place(width=1280,height=495,x=0,y=225)

    n_click1+=1
    n_click2 = 0

    if n_click1>= 10:
        click2 = Button(text='Ну пожалуйста',font=('Arial', 20),bg='white',command = next_color2)
        click2.place(width =200,x=random.randint(0,1080), y=random.randint(250,645))

        click = Button(text='Клик',font=('Arial', 20),bg='white',command = next_color1)
        click.place(width =100,x=random.randint(0,1180), y=random.randint(250,645))

    else:
        click = Button(text='Клик',font=('Arial', 20),bg='white',command = next_color1)
        click.place(width =100,x=random.randint(0,1180), y=random.randint(250,645)) 
        n_click1

        click2 = Button(text='тоже клик',font=('Arial', 20),bg='white',command = next_color2)
        click2.place(width =200,x=random.randint(0,1080), y=random.randint(250,645))
    num+=1


def next_color2():
    global num, n_click1, n_click2

    info = Message(text=str(num), font=('Arial', 20),bg='white')
    info.place(width =1280,height=75,x=0,y= 150)

    back = Message(bg ='white')
    back.place(width=1280,height=495,x=0,y=225)

    n_click1 = 0
    n_click2+=1

    if n_click2>= 10:
        click = Button(text='Ну пожалуйста',font=('Arial', 20),bg='white',command = next_color1)
        click.place(width =200,x=random.randint(0,1180), y=random.randint(250,645))

        click2 = Button(text='тоже клик',font=('Arial', 20),bg='white',command = next_color2)
        click2.place(width =200,x=random.randint(0,1080), y=random.randint(250,645))

    else:
        click = Button(text='Клик',font=('Arial', 20),bg='white',command = next_color1)
        click.place(width =100,x=random.randint(0,1180), y=random.randint(250,645)) 
        n_click1

        click2 = Button(text='тоже клик',font=('Arial', 20),bg='white',command = next_color2)
        click2.place(width =200,x=random.randint(0,1080), y=random.randint(250,645))
    num+=1


label_title = Label(text = 'Кликер',font=('Arial', 30),bg='white')
label_title.place(width =1280,height=150, x=0,y=0)

start = Button(text='Старт',font=('Arial', 20), bg='white',command = next_color)
start.place(x=585, y=150)

window.mainloop()

