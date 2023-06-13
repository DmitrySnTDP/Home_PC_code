import vk_api
from cource import *
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard,VkKeyboardColor
from random import *
from wiki import *
from datetime import datetime



token='vk1.a.fobZKmf3kYaRLmUNO_yfikiwhw9Q5Ou65KfI7hkyGnq8-wpZi6bpofjGLOsP-pdgEsG-pL0t4t4Kz7GVByCKrE8vrbCSYKconj_tJ9MsYTHjdu_XthOMGHUJ6f8Sek_BGuNyP7vPr2vrPItVVdxuoK5PzQqjBA8AiGsJYbMABPLLfREHUQIKD5xr16N9mgTpRQvFebXAICcTkNBITxZulw'

keyboards = [
    ['австралийский доллар','азербайджанский манат','фунт стерлингов','армянских драмов','белорусский рубль','болгарский лев','бразильский реал','далее'],
    ['венгерских форинтов','вьетнамских донгов','гонконгский доллар','грузинский лари','датская крона','дирхам оаэ','назад','далее'],
    ['доллар сша','евро','египетских фунтов','индийских рупий','индонезийских рупий','казахстанских тенге','назад','далее'],
    ['канадский доллар','катарский риал','киргизских сомов','китайский юань','молдавских леев','новозеландский доллар','назад','далее'],
    ['норвежских крон','польский злотый','румынский лей','сингапурский доллар','таджикских сомони','таиландских батов','назад','далее'],
    ['турецких лир','новый туркменский манат','узбекских сумов','украинских гривен','чешских крон','шведских крон','назад','далее'],
    ['швейцарский франк','сербских динаров','южноафриканских рэндов','вон республики корея','назад','японских иен']
]

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

check_kourse = False
check_dat = False

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        check = True
        
        msg = event.text.lower()
        user_id = event.user_id
        random_id = randint(1,10**10)

        if msg == "команды":
            responce = 'Я умею:\n-Искать статью в Википедии по вашему запросу.\nКоманда: "вики ваш запрос"\nНапример: вики Россия\n-Искать курс валюты:\nкоманда: "курс валюты"'
        
        elif msg=="курс валюты":
            keyb = VkKeyboard(one_time=True)
            keyb.add_button('сегодня',VkKeyboardColor.SECONDARY)
            keyb.add_button('указать дату',VkKeyboardColor.SECONDARY)

            vk_session.method('messages.send', {'user_id':user_id,'random_id' : random_id,'message' : 'выберите дату за которую хотите найти курс','keyboard':keyb.get_keyboard()})

        elif msg=='далее':
            check = False
            page+=1

        elif msg=='назад':
            check = False
            page-=1

        elif msg=='указать дату':
            responce = 'Введите дату в формате дд.мм.гггг'
            check_dat = True
        
        elif check_dat:
            try:
                if len(msg) == 10:
                    d = str(msg[:2])
                    m = str(msg[3:5])
                    Y = str(msg[-4:])
                    int(d),int(m),int(Y) #проверка переменных на наличие в них символов отличных от цифр
                    dati = d+'/'+m+'/'+Y
                    check_dat = False
                    check = False
                    check_kourse = True
                    page = 1
                else:
                    raise Exception('')
                
            except:
                responce = 'дата указана некорректно, введите дату ещё раз'

        elif msg=='сегодня':
            check = False
            check_kourse = True
            dati = datetime.today().strftime('%d/%m/%Y')
            page = 1

        elif check_kourse:
            check_kourse = False
            Val = msg
            if Val=='фунт стерлингов':
                Val = 'фунт стерлингов соединенного королевства'
            responce = get_cource(Val,dati)


        elif msg.startswith("вики"):
            article = msg[5:]
            responce = get_wiki_article(article)

        else:
            responce = 'Я такого не умею\n Я умею:\n-Искать статью в Википедии по вашему запросу.\nКоманда: "вики ваш запрос"\nНапример: вики Россия\n-Искать курс валюты:\nкоманда: "курс валюты"'

        if check:
            vk.messages.send(user_id=user_id,random_id = random_id,message = responce)
            

        if not check:
            
            k = keyboards[page-1]
            keyb = VkKeyboard(one_time=True)

            for i in range(len(k)):
                if i==2 or i==4 or i==6:
                    keyb.add_line()
                keyb.add_button(k[i],VkKeyboardColor.SECONDARY)
            
            vk_session.method('messages.send', {'user_id':user_id,'random_id' : random_id,'message' : f'Валюты стр. {page}','keyboard':keyb.get_keyboard()})