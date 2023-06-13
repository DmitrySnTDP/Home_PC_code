# message = vk.method('messages.getConversations',{'count':20,'filter':'unanswered'})

# while True:
#     messages = vk.method('messages.getConversations',{'count':20,'filter':'unanswered'})
#     if messages['count']>=1:

#         user_id = messages['items'][0]['last_message']['from_id']
#         message_id = messages['items'][0]['last_message']['id']

#         if messages['items'][0]['last_message']['text']=='курс':
#             vk.method('messages.send',{'peer_id':user_id, 'random_id':message_id,'message':get_cource('R01235')})

#         elif messages['items'][0]['last_message']['text']=='планеты':
#             url = "https://swapi.dev/api/"
#             responce = requests.get(url).json()
#             planet_api = responce.get('planets')

#             def check_planet(url):
#                 d = 0
#                 for i in range (1,60):
                    
#                     answer = requests.get(f'{url}/{i}').json()
#                     if answer.get('diameter')=='unknown':
#                         None
#                     elif int(answer.get('diameter'))>d:
#                         d = int(answer.get('diameter'))
#                         p= answer.get('name')
#                 vk.method('messages.send',{'peer_id':user_id, 'random_id':message_id,'message':f'самая большая планета: {p}, диаметр: {d}'})

#             check_planet(planet_api)

#         elif messages['items'][0]['last_message']['text']=='корабли':
#             url = "https://swapi.dev/api/"
#             response = requests.get(url).json()
#             starships_api = response.get('starships')

#             def check_starships(url):
#                 max_speed_list=[]
#                 max_speed_slovar={}
#                 for i in range (1,36):
#                     answer = requests.get(f'{url}/{i}').json()
#                     if answer.get('max_atmosphering_speed')!='n/a' and answer.get('max_atmosphering_speed')!='1000km' and answer.get('max_atmosphering_speed')!=None :
#                         max_speed_list.append(int(answer.get('max_atmosphering_speed')))
#                     if answer.get('max_atmosphering_speed')!='n/a' and answer.get('max_atmosphering_speed')!='1000km' and answer.get('max_atmosphering_speed')!=None:
#                         max_speed_slovar[answer.get('max_atmosphering_speed')]=answer.get('name')
#                 max_speed=max(max_speed_list)

#                 vk.method('messages.send',{'peer_id':user_id, 'random_id':message_id,'message':f'самый быстрый корабль: {max_speed_slovar.get(str(max_speed))}, его скорость: {max_speed}'})

#             check_starships(starships_api)

#         else:
#             vk.method('messages.send',{'peer_id':user_id, 'random_id':message_id, 'message':'Я такого не умею'})