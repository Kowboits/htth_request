import requests
# super_heros = ['Hulk', 'Captain America', 'Thanos']
# max_intellegence = 0
# smart_hero = ''
# for hero in super_heros:
#     url = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
#     intell = requests.get(url).json()['results']
#     for i in range(len(intell)):
#         if intell[i]['name'] in super_heros:
#             if int(intell[i]['powerstats']['intelligence']) > max_intellegence:
#                 max_intellegence = int(intell[i]['powerstats']['intelligence'])
#                 smart_hero = intell[i]['name']
# print(f'Самый умный {smart_hero}, интеллект = {max_intellegence}')

def smarted_super_hero(super_heros, url_fix = 'https://superheroapi.com/api/2619421814940190/search/'):
    max_intellegence, smart_hero = 0, ''
    for hero in super_heros:
        url = f'{url_fix}{hero}'
        intell = requests.get(url).json()['results']
        for i in range(len(intell)):
            if intell[i]['name'] in super_heros:
                if int(intell[i]['powerstats']['intelligence']) > max_intellegence:
                    max_intellegence = int(intell[i]['powerstats']['intelligence'])
                    smart_hero = intell[i]['name']
    return f'Самый умный {smart_hero}, интеллект = {max_intellegence}'

print(smarted_super_hero(['Hulk', 'Captain America', 'Thanos']))
