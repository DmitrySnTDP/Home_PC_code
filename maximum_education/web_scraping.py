import requests

url = "https://swapi.dev/api/"
responce = requests.get(url).json()
planet_api = responce.get('planets')

def check_planet(url):
    diametr_list=[]
    for i in range (1,60):
        answer = requests.get(f'{url}/{i}').json()
        diametr_list.append({answer.get('name'):answer.get('diameter')})
    print(diametr_list)
    d = 0
    for i in diametr_list:
        if int(i.values())>d:
            d = int(i.values())
    print(d)


check_planet(planet_api)




                                    #  hw

# import requests

# url = "https://swapi.dev/api/"

# response = requests.get(url).json()

# starships_api = response.get('starships')

# def check_starships(url):
#     max_speed_list=[]
#     max_speed_slovar={}
#     for i in range (2,36):
#         answer = requests.get(f'{url}/{i}').json()
#         if answer.get('max_atmosphering_speed')!='n/a' and answer.get('max_atmosphering_speed')!='1000km' and answer.get('max_atmosphering_speed')!=None :
#             max_speed_list.append(answer.get('max_atmosphering_speed'))
#         if answer.get('max_atmosphering_speed')!='n/a' and answer.get('max_atmosphering_speed')!='1000km' and answer.get('max_atmosphering_speed')!=None:
#             max_speed_slovar[answer.get('max_atmosphering_speed')]=answer.get('name')
#     max_speed=max(max_speed_list)
#     print(max_speed_slovar.get(str(max_speed)))

# check_starships(starships_api)

