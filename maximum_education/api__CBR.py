import requests
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.today()
today = now.strftime('%d/%m/%Y')

payload = {'date_req=': today}

url = "https://www.cbr.ru/scripts/XML_daily.asp?"

responce = requests.get(url, params=payload)

xml = BeautifulSoup(responce.content, 'html.parser')

def getCourse(id):
    return xml.find('valute',{'id':id}).value.text
print(getCourse('R01239'), 'рублей за 1 евро') # руб за 1 евро сейчас
print(getCourse('R01235'), 'рублей за 1 доллар')
print(getCourse('R01090B'), 'рублей за 1 Белорусский рубль')
print(getCourse('R01335'), 'рублей за 1 Казахстанских тенге')
