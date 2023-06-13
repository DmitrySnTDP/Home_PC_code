import telebot
import requests
import random
from bs4 import BeautifulSoup

token = '5785117132:AAG_LmIWmp13bw5LLnNzy2IinazvPwjhbJo'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов, могу показать милых котиков, а ещё могу порекомендовать игры по жанру!    
    """
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("Песня")
    button2 = telebot.types.KeyboardButton("Стихотворение")
    button3 = telebot.types.KeyboardButton("Случайная фотография кота")
    button4 = telebot.types.KeyboardButton("Стикер")
    button5 = telebot.types.KeyboardButton("Рекомендация игр по жанру")
    keyboard.add(button1,button2,button3,button4, button5)
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    bot.send_message(message.chat.id, poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_url=telebot.types.InlineKeyboardButton('Перейти', url='https://stihi.ru/')
    keyboard.add(button_url)
    bot.send_message(message.chat.id, 'Больше по ссылке ниже', reply_markup=keyboard)

# @bot.message_handler(commands=['fact'])
# def send_fact(message):
#     response = requests.get('https://i-fakt.ru/').content
#     html = BeautifulSoup(response, 'html.parser')
#     fact = random.choice(html.find_all(class_='p-2 clearfix'))
#     fact_link =  fact.a.attrs['href']
#     bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_num = str(random.randint(1,9))
    cat_img = open('media_f/img/'+cat_num+'.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(commands=['music'])
def send_music(message):
    song = open('media_f/happy.mp3','rb')
    bot.send_audio(message.chat.id, song,timeout=60)

@bot.message_handler(commands='sticker')
def one_sticker(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG6IVjobxuNGFWETniKofQkvchbpUgyAAC1iUAAhrFEElbg3iHjtC_uiwE')

@bot.message_handler(commands=['recommend_game'])
def game(message):
    welcome_text = """
    Выбирай жанр игры, а я порекомендую игры в этом жанре.    
    """

    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("Экшен")
    button2 = telebot.types.KeyboardButton("Ролевая игра")
    button3 = telebot.types.KeyboardButton("Стратегия")
    button4 = telebot.types.KeyboardButton("Визуальная новелла")
    button5 = telebot.types.KeyboardButton("Симулятор")
    button6 = telebot.types.KeyboardButton("Гонки")
    button7 = telebot.types.KeyboardButton("Назад")
    keyboard.add(button1, button2, button3, button4, button5, button6,button7)
    bot.send_message(message.chat.id, welcome_text ,reply_markup=keyboard)

                                                            
    


@bot.message_handler(content_types=['text'])
def answer(message):
    # if message.text == 'Факт':
    #     send_fact(message)
    if message.text=='Песня':
        send_music(message)
    elif message.text =='Стихотворение':
        send_poem(message)
    elif message.text =='Случайная фотография кота':
        send_cat(message)
    elif message.text =='Стикер':
        one_sticker(message)
    elif message.text == 'Рекомендация игр по жанру':
        game(message)
    elif message.text == 'Назад':
        send_welcome(message)
    elif message.text == 'Экшен':
        bot.send_message(message.chat.id, '1. Elden Ring \n https://store.steampowered.com/app/1245620/ELDEN_RING/')
        bot.send_message(message.chat.id, '2. Hitman 3 \n https://store.steampowered.com/app/1659040/HITMAN_3/')
        bot.send_message(message.chat.id, '3. Rust \n https://store.steampowered.com/app/252490/Rust/')
    elif message.text == 'Ролевая игра':
        bot.send_message(message.chat.id, '1. Valheim \n https://store.steampowered.com/app/892970/Valheim/')
        bot.send_message(message.chat.id, '2. Project Zomboid \n https://store.steampowered.com/app/108600/Project_Zomboid/')
        bot.send_message(message.chat.id, '3. Disco Elysium - The Final Cut \n https://store.steampowered.com/app/632470/Disco_Elysium__The_Final_Cut/')
    elif message.text == 'Стратегия':
        bot.send_message(message.chat.id, '1. Cities: Skylines \n https://store.steampowered.com/app/255710/Cities_Skylines/')
        bot.send_message(message.chat.id, '2. RimWorld \n https://store.steampowered.com/app/294100/RimWorld/')
        bot.send_message(message.chat.id, '3. Stellaris \n https://store.steampowered.com/app/281990/Stellaris/')
    elif message.text == 'Визуальная новелла':
        bot.send_message(message.chat.id, '1. The Walking Dead: The Telltale Definitive Series \n https://store.steampowered.com/app/1449690/The_Walking_Dead_The_Telltale_Definitive_Series/')
        bot.send_message(message.chat.id, '2. Super Robot Wars 30 \n https://store.steampowered.com/app/898750/Super_Robot_Wars_30/')
        bot.send_message(message.chat.id, '3. Library Of Ruina \n https://store.steampowered.com/app/1256670/Library_Of_Ruina/')
    elif message.text == 'Симулятор':
        bot.send_message(message.chat.id, '1. The Forest \n https://store.steampowered.com/app/242760/The_Forest/')
        bot.send_message(message.chat.id, '2. Euro Truck Simulator 2 \n https://store.steampowered.com/app/227300/Euro_Truck_Simulator_2/')
        bot.send_message(message.chat.id, '3. Satisfactory \n https://store.steampowered.com/app/526870/Satisfactory/')
    elif message.text == 'Гонки':
        bot.send_message(message.chat.id, '1. SnowRunner \n https://store.steampowered.com/app/1465360/SnowRunner/')
        bot.send_message(message.chat.id, '2. Assetto Corsa \n https://store.steampowered.com/app/244210/Assetto_Corsa/')
        bot.send_message(message.chat.id, '3. iRacing \n https://store.steampowered.com/app/266410/iRacing/')

bot.polling()