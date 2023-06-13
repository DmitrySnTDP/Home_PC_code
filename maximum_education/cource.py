import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'


Val = []
Val_ids = []
today = datetime.today().strftime('%d/%m/%Y')
payload = {'date_req':today}

responce = requests.get(url,params=payload)

xml=BeautifulSoup(responce.content,'html.parser')

for i in range(1010,2000):
    if i==1020:
        id = 'R0'+str(i)+'A'
    elif i==1090:
        id = 'R0'+str(i)+'B'
    elif i==1585:
        id = 'R0'+str(i)+'F'
    elif i==1700:
        id = 'R0'+str(i)+'J'
    elif i==1710:
        id = 'R0'+str(i)+'A'
    elif i==1805:
        id = 'R0'+str(i)+'F'
    else:
        id = 'R0'+str(i)

    try:
        if str(xml.find("valute",{'id':id}).numcode.text)!='960':
            l = (str(xml.find("valute",{'id':id}).text))[7:]

            Val.append(l.lower())
            Val_ids.append(id)
    except:
        None
for k in range(11):
    for i in Val:
        if i[0]=='0':
            Val[Val.index(i)]=i[1:]
        elif i[-1]=='1' or i[-1]=='2' or i[-1]=='0' or i[-1]=='3' or i[-1]=='4' or i[-1]=='5' or i[-1]=='6' or i[-1]=='7' or i[-1]=='8'or i[-1]=='9'or i[-1]==',' :
            Val[Val.index(i)]=i[:-1]

def get_cource(currency,dat):
    global Val, Val_ids,xml
    payload = {'date_req':dat}

    responce = requests.get(url,params=payload)

    xml=BeautifulSoup(responce.content,'html.parser')

    try:
        n = Val.index(currency)
        return str(xml.find("valute",{'id':Val_ids[n]}).value.text)+' рублей за '+str(xml.find("valute",{'id':Val_ids[n]}).nominal.text)+' '+str(Val[n])
    except:
        return str('у меня нет сведений об этой валюте в тот день')

    