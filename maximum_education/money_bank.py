from tkinter import*
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window=Tk()
window.title('Деньгобанк')
window.geometry('400x300+500+300')
window.resizable(width=False,height=False)
window.config(bg='#62e4e9')

url='http://www.cbr.ru/scripts/XML_daily.asp?'

today=datetime.today()
today=today.strftime('%d/%m/%Y')

payload={'date_req':today}

responce=requests.get(url, params=payload)

xml=BeautifulSoup(responce.content, 'html.parser')

def getCourse(id):
    return xml.find('valute', {'id':id}).value.text

img_logo=PhotoImage(file='logo.png')
logo= Label(window, image =img_logo,bg='#62e4e9')
logo.place(x=0,y=0)

course_info=Label(window, text='Курс рубля в банке \n составляет: ',bg='#62e4e9', font=('Arial 16'))
course_info.place(x=150,y=90)

dollar=Label(window, text='Доллар стоит: '+getCourse('R01235')+' рублей',bg='#62e4e9', font=('Arial 16'))
dollar.place(x=15,y=150)

eur=Label(window, text='Евро стоит: '+getCourse('R01239')+' рублей',bg='#62e4e9', font=('Arial 16'))
eur.place(x=15,y=200)

cny=Label(window, text='Китайский юань стоит: '+getCourse('R01375')+' рублей',bg='#62e4e9',font=('Arial 16'))
cny.place(x=15,y=250)

window.mainloop()