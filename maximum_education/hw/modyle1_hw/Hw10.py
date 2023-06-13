# import requests
# from bs4 import BeautifulSoup

# lables = []
# # http://www.columbia.edu/~fdc/sample.html
# S = input('Введите ссылку на сайт: ')
# response = requests.get(S)
# response = response.content

# html = BeautifulSoup(response, 'html.parser')

# labe = html.find(id='contents')
# lables.append(labe.text)
# labe = html.find(id='basics')
# lables.append(labe.text)
# labe = html.find(id='syntax')
# lables.append(labe.text)
# labe = html.find(id='chars')
# lables.append(labe.text)
# labe = html.find(id='convert')
# lables.append(labe.text)
# labe = html.find(id='effects')
# lables.append(labe.text)
# labe = html.find(id='lists')
# lables.append(labe.text)
# labe = html.find(id='links')
# lables.append(labe.text)
# labe = html.find(id='tables')
# lables.append(labe.text)
# labe = html.find(id='viewing')
# lables.append(labe.text)
# labe = html.find(id='install')
# lables.append(labe.text)
# labe = html.find(id='more')
# lables.append(labe.text)
# labe = html.find(id='fluid')
# lables.append(labe.text)
# print(lables)




# import requests
# from bs4 import BeautifulSoup


# response = requests.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets')
# response = response.content

# html = BeautifulSoup(response, 'html.parser')
# inf = html.find(class_="row ecomerce-items ecomerce-items-ajax")
# print(inf.attrs['data-items'])




import requests
from bs4 import BeautifulSoup
import random

def free():
    response = requests.get('https://store.steampowered.com/genre/Free%20to%20Play/?offset=12')
    response = response.content

    html = BeautifulSoup(response, 'html.parser')
    fact =random.choice(html.find_all(class_='salepreviewwidgets_TitleCtn_1F4bc'))
    print(fact.a.attrs['href'])

def ranniy():
    response = requests.get('https://store.steampowered.com/genre/Early%20Access/')
    response = response.content

    html = BeautifulSoup(response, 'html.parser')
    fact =random.choice(html.find_all(class_='salepreviewwidgets_TitleCtn_1F4bc'))
    print(fact.a.attrs['href'])

def drive():
    response = requests.get('https://store.steampowered.com/tags/ru/%D0%93%D0%BE%D0%BD%D0%BA%D0%B8/?snr=1_4_4__125')
    response = response.content

    html = BeautifulSoup(response, 'html.parser')
    fact =random.choice(html.find_all(class_='salepreviewwidgets_TitleCtn_1F4bc'))
    print(fact.a.attrs['href'])

def indy():
    response = requests.get('https://store.steampowered.com/tags/ru/%D0%98%D0%BD%D0%B4%D0%B8/?snr=1_4_4__125')
    response = response.content

    html = BeautifulSoup(response, 'html.parser')
    fact =random.choice(html.find_all(class_='salepreviewwidgets_TitleCtn_1F4bc'))
    print(fact.a.attrs['href'])

def kazual():
    response = requests.get('https://store.steampowered.com/tags/ru/%D0%9A%D0%B0%D0%B7%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%B8%D0%B3%D1%80%D0%B0/?snr=1_4_4__125')
    response = response.content

    html = BeautifulSoup(response, 'html.parser')
    fact =random.choice(html.find_all(class_='salepreviewwidgets_TitleCtn_1F4bc'))
    print(fact.a.attrs['href'])

def MMO():
    response = requests.get('https://store.steampowered.com/tags/ru/%D0%9C%D0%9C%D0%9E/?snr=1_4_4__125')
    response = response.content

    html = BeautifulSoup(response, 'html.parser')
    fact =random.choice(html.find_all(class_='salepreviewwidgets_TitleCtn_1F4bc'))
    print(fact.a.attrs['href'])

def prikvel():
    response = requests.get('https://store.steampowered.com/tags/ru/%D0%9F%D1%80%D0%B8%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5/?snr=1_4_4__125')
    response = response.content

    html = BeautifulSoup(response, 'html.parser')
    fact =random.choice(html.find_all(class_='salepreviewwidgets_TitleCtn_1F4bc'))
    print(fact.a.attrs['href'])

def role():
    response = requests.get('https://store.steampowered.com/tags/ru/%D0%A0%D0%BE%D0%BB%D0%B5%D0%B2%D0%B0%D1%8F%20%D0%B8%D0%B3%D1%80%D0%B0/?snr=1_4_4__125')
    response = response.content

    html = BeautifulSoup(response, 'html.parser')
    fact =random.choice(html.find_all(class_='salepreviewwidgets_TitleCtn_1F4bc'))
    print(fact.a.attrs['href'])

def simulator():
    response = requests.get('https://store.steampowered.com/tags/ru/%D0%A1%D0%B8%D0%BC%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80/?snr=1_4_4__125')
    response = response.content

    html = BeautifulSoup(response, 'html.parser')
    fact =random.choice(html.find_all(class_='salepreviewwidgets_TitleCtn_1F4bc'))
    print(fact.a.attrs['href'])

def sport():
    response = requests.get('https://store.steampowered.com/tags/ru/%D0%A1%D0%BF%D0%BE%D1%80%D1%82%D0%B8%D0%B2%D0%BD%D0%B0%D1%8F%20%D0%B8%D0%B3%D1%80%D0%B0/?snr=1_4_4__125')
    response = response.content

    html = BeautifulSoup(response, 'html.parser')
    fact =random.choice(html.find_all(class_='salepreviewwidgets_TitleCtn_1F4bc'))
    print(fact.a.attrs['href'])

def strateg():
    response = requests.get('https://store.steampowered.com/tags/ru/%D0%A1%D1%82%D1%80%D0%B0%D1%82%D0%B5%D0%B3%D0%B8%D1%8F/?snr=1_4_4__125')
    response = response.content

    html = BeautifulSoup(response, 'html.parser')
    fact =random.choice(html.find_all(class_='salepreviewwidgets_TitleCtn_1F4bc'))
    print(fact.a.attrs['href'])

def ekshin():
    response = requests.get('https://store.steampowered.com/tags/ru/%D0%AD%D0%BA%D1%88%D0%B5%D0%BD/?snr=1_4_4__125')
    response = response.content

    html = BeautifulSoup(response, 'html.parser')
    fact =random.choice(html.find_all(class_='salepreviewwidgets_TitleCtn_1F4bc'))
    print(fact.a.attrs['href'])

while True:
    a = ['0 - выход, 1- Беспплатно, 2 - Ранний доступ, 3 - Гонки, 4 - Инди, 5 - Казуальная игра, 6 - ММО, 7 - Приключение, 8 - Ролевая игра, 9 - Симулятор, 10 - Спортивная игра, 11 - Стратегия, 12 - Экшен']
    print(*a)
    num = int(input())
    if num == 0:
        break
    elif num == 1:
        free()
    elif num == 2:
        ranniy()
    elif num == 3:
        drive()
    elif num == 4:
        indy()
    elif num == 5:
        kazual()
    elif num == 6:
        MMO()
    elif num == 7:
        prikvel()
    elif num == 8:
        role()
    elif num == 9:
        simulator()
    elif num == 10:
        sport()
    elif num == 11:
        strateg()
    else:
        ekshin()
    print('*'*20)